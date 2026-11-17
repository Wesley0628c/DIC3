"""Unit tests of Gemini graph without real API or downloading embeddings."""
from datetime import date, timedelta
from langchain_core.messages import AIMessage
from src.agent.gemini_graph import GeminiFoodAgent
from src.database.db_manager import DatabaseManager
from src.services.inventory_service import InventoryService

class FakeBoundModel:
    def invoke(self, messages):
        from langchain_core.messages import ToolMessage
        if any(isinstance(m,ToolMessage) for m in messages):
            return AIMessage(content='已使用工具查詢資料。')
        return AIMessage(content='', tool_calls=[{'name':'query_active_inventory_tool','args':{},'id':'call01'}])
class FakeModel:
    def bind_tools(self, tools):
        self.tools=tools
        return FakeBoundModel()

def test_graph_executes_inventory_tool(tmp_path):
    db=DatabaseManager(str(tmp_path/'v3.db')); db.initialize_database()
    inv=InventoryService(db)
    inv.add_item({'name':'番茄','category':'vegetable','quantity':2,'unit':'piece',
       'purchase_date':date.today().isoformat(),
       'expiry_date':(date.today()+timedelta(days=1)).isoformat(),
       'date_label_type':'best_before','opened_date':None,'storage_location':'refrigerator'})
    agent=GeminiFoodAgent(inv,model=FakeModel())
    result=agent.process_query('我有哪些食材？')
    assert '已使用工具' in result
    assert len(agent.last_trace)==1
    assert '番茄' in agent.last_trace[0]['result']

def test_tools_do_not_mutate_db(tmp_path):
    db=DatabaseManager(str(tmp_path/'v3.db'));db.initialize_database()
    inv=InventoryService(db)
    agent=GeminiFoodAgent(inv,model=FakeModel())
    assert all(not any(w in t.name for w in ('delete','update','add_item')) for t in agent.tools)

def test_evaluation_reference_date_reaches_tools():
    import json
    from evaluation.run_evaluation import fixture_inventory, TODAY
    class Fixture:
        def get_items(self, **kwargs):
            return fixture_inventory(TODAY)
    agent = GeminiFoodAgent(Fixture(), model=FakeModel(), reference_date=TODAY)
    tools = {tool.name: tool for tool in agent.tools}
    near = json.loads(tools['query_expiring_items_tool'].invoke({'days_ahead':3}))
    assert {item['name'] for item in near} == {'番茄','菠菜','雞胸肉'}
    status = json.loads(tools['validate_inventory_safety_tool'].invoke({'item_name':'雞胸肉'}))
    assert status['items'][0]['status'] == 'eligible'
    recipes = json.loads(tools['recommend_recipes_for_servings_tool'].invoke({'servings':2,'mode':'ready_now'}))
    assert recipes[0]['title'] == '高麗菜炒蛋' and recipes[0]['can_make_now']
