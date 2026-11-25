# A2Z SOP Methodology: 26-Letter Academic Research & Paper Framework

> 本文件為《A2Z outline example.pdf》之 26 字母學術論文與專案提案標準架構，作為 Food Guardian 論文寫作、OpenSpec 規格設計與評估驗證的最高綱領。

---

## 1. 26 字母結構定義與 Food Guardian 內容映射表

| 字母 | A2Z SOP 項目定義 | 論文章節映射 | Food Guardian 具體落實與內容映射 |
| :---: | :--- | :--- | :--- |
| **A** | **Attention Getter**：動機與引題 | Abstract & Intro | 引用 UNEP 2024 與 UN SDG 12.3 (2025)，全球消費端年食物浪費達 10.5 億噸，凸顯家庭食材管理急迫性。 |
| **B** | **But**：挑戰與現有不足 | Abstract & Intro | FDA 報告指出消費者對日期標示（Best-by vs. Use-by）混淆，純 LLM 生成食譜存在幽靈食材與單位換算缺失。 |
| **C** | **Cure**：提出的創新解藥 | Abstract & Intro | 提出 **Food Guardian**：結合 LLM 意圖推理與確定性 SQLite 庫存、保存規則檢索之混合式 Domain AI Agent。 |
| **D** | **Development**：方法設計依據 | Abstract & Method | 結合 LLM 規劃協調、SQLite 批次庫存、Python 確定性份量換算、FoodSafety.gov 冷藏保存規則引擎。 |
| **E** | **Experiments**：評估規劃 | Abstract & Eval | 規劃 20–30 種食材、20–30 道食譜，設計 30 組情境（充足、缺料、臨期、資訊不足、偏好衝突），對照 B0/B1/P。 |
| **F** | **Findings**：預期成果（無虛構） | Abstract & Concl | 預期達到食譜可行率提高、零未揭露缺料、100% 遵守已定義食安硬限制，不宣稱未經真實家庭實測之浪費下降數據。 |
| **G** | **General**：領域大背景現況 | Introduction | 智慧家庭、永續生活與智慧冰箱管理市場發展，數位化庫存追蹤具有減廢與節能潛力。 |
| **H** | **However**：深層技術與應用瓶頸 | Introduction | 傳統手動盤點負擔重且難以持續，通用 LLM 缺乏物理庫存約束與真實冷鏈感知，容易產生虛構建議。 |
| **I** | **In literature**：文獻發展梳理 | Related Work | 梳理 Vision-to-Recipe (Liu et al. WACV 2025)、食品文字檢索 (Vavken et al. 2026)、LLM-RAG 飲食品質推薦 (Wang et al. 2026)。 |
| **J** | **Judgement**：各方法優劣點評析 | Related Work | 影像轉食譜忽略實體剩餘量；食品檢索未處理動態批次；通用 LLM 無事務機制易導致狀態脫節。 |
| **K** | **Keypoint**：設計精神與核心貢獻 | Intro & Design | 提出「對話式自然語言入口 + 外部確定性工具核量 + 規則式臨期排序 + 使用者確認後扣料」之核心架構。 |
| **L** | **List organization**：文章結構導覽 | Introduction | 依序規劃摘要、緒論、相關文獻、系統架構與流程、Algorithm 1、實驗評估設計、討論與界線、結論與未來展望。 |
| **M** | **Methods**：既有文獻方法分類 | Related Work | 分類為「多模態生成」、「結構化資料庫檢索轉換」、「營養指標導向 RAG」與「確定性冷鏈規則」。 |
| **N** | **New proposed**：本專案創新技術 | Architecture | 「LLM Planner + SQLite Batch Inventory + Rule-based Expiration Filter + ACID Transactional Confirmation」。 |
| **O** | **Organize**：文獻比較與歸納表 | Related Work | 建立包含 5 類文獻之 **Table I: Summary of Related Work and Boundaries**，精確標定 Research Gap。 |
| **PA** | **Aim**：研究目標陳述 | Section III | 打造降低家庭食材盤點負擔、具可解釋性、零幻覺扣料與食安硬限制守門之領域智慧代理人。 |
| **PB** | **Based on**：依託基礎與背景 | Section III | 依託 FDA 食品浪費指引、FoodSafety.gov 官方冷藏保存表、SQLite ACID 交易機制與 OpenSpec 2.1.0 規範。 |
| **PC** | **Cure / Cause**：機制有效的原因 | Section III | 透過確定性換算消除 LLM 數量計算黑盒；透過主動澄清機制（Clarification Loop）消除保存與單位模糊。 |
| **PD** | **Design**：系統架構設計 | Section III | 典範轉移：從「使用者逐欄填寫庫存」轉變為「AI Agent 理解需求、檢索庫存並由外部工具執行硬限制核量」。 |
| **PE** | **Paper Element**：模組元件清單 | Section III | 嚴格拆解 ① 使用者情境、② 需求輸入、③ Planner Agent、④ 庫存/食譜檢索、⑤ 日期與份量分析、⑥ 保存規則庫、⑦ 規則驗證、⑧ 候選輸出、⑨ 交易更新。 |
| **PF** | **Formulation**：功能與數學形式 | Section III | 定義份量縮放公式 $Q_{need} = Q_{recipe} \times N / N_{base}$、同維度單位換算函數及布林硬限制篩選邏輯。 |
| **PG** | **Graph**：架構圖與流程圖 | Section III | 提供 System Architecture 方塊圖與含主動追問、硬限制篩選及交易確認之決策流程圖 (Flowchart)。 |
| **PH** | **How**：如何達成設計目標 | Section III | 透過唯讀 Agent 檢索庫存、確定性排序臨期批次、核對缺料與過敏原、等待使用者確認後發起 SQL Transaction。 |
| **PI** | **Implementation**：虛擬碼落實 | Section III | 具行號之 **Algorithm 1: Proposed Food Guardian Workflow**（包含 Clarification 與 Rollback 邏輯）。 |
| **PJ** | **Jump to an example**：情境範例展示 | Section III/IV | 「我有 3 顆雞蛋、半顆洋蔥與 200g 臨期番茄，2 人份晚餐」之端到端檢索、換算、排序與扣料範例。 |
| **PK** | **Key points contribution**：核心貢獻總結 | Conclusion | 條列四大貢獻：可操作繁中 Agent 原型、OpenSpec 規格可追溯性、來源可解釋性、以及 B0/B1/P 重現評估架構。 |
| **PL** | **Later simulation**：後續模擬評估規劃 | Section IV | 規劃 30 組基準情境之獨立三次執行、Feasibility 與 Match 統計分析，以及未來家庭場域試驗規劃。 |
| **PM** | **Math proof / Logic**：邏輯檢驗 | Section III/IV | 庫存扣減之守恆性、幂等操作 ID 防重覆扣料邏輯、以及硬限制不可被使用者偏好覆蓋之形式化證明。 |
| **Q** | **Quality & Quantity**：指標與評估量 | Section IV | 定義 $R_{feas}$（食譜可行率）、$A_{inv}$（庫存匹配率）、$P_{exp}$（臨期提醒率）、$V_{rule}$（規則違反率）、$C_{clar}$（澄清率）與 $S_{cov}$（解覆蓋率）。 |
| **R** | **Related method to compare**：比較基準 | Section IV | 建立三組對照實驗：B0 (無庫存通用 LLM)、B1 (同資料文字提示之 LLM)、P (Food Guardian 工具管線)。 |
| **S** | **Simulation Setup**：實驗環境設定 | Section IV | 20–30 種食材庫存快照、20–30 道標準食譜、固定模型溫度 ($T=0.2$) 與參考日期。 |
| **T** | **Tuning parameters**：調優參數 | Section IV | 臨期天數閾值、單位模糊判定閾值、提示詞溫度、最大候選輸出數（Top-3）。 |
| **U** | **Useful results**：預期有用產出 | Section IV/VI | 產生可執行食譜清單、精確缺料明細、即將到期食材清單與可追溯之審計日誌。 |
| **V** | **Verify**：有效性驗證 | Section IV | 驗證 Food Guardian 是否能達到 100% 攔截過期食材、零未揭露缺料，且可行率顯著高於純 LLM。 |
| **W** | **What proposed**：回顧總結 | Conclusion | 總結為解決家庭食材管理盲點與 LLM 幻覺推薦的架構設計。 |
| **X** | **eXcel**：專精情境與優勢 | Discussion | 專精於「家庭多批次管理」、「臨期優先消化」與「零幻覺實體扣料」場景。 |
| **Y** | **Yields**：預期最終交付物 | Handover | 交付 IEEE 雙欄論文 LaTeX 套件、Overleaf 壓縮包、GitHub 儲存庫、完整 DESIGN.md 與 OpenSpec 規格。 |
| **Z** | **Zen**：反思、邊界與未來展望 | Discussion | 坦承日期提醒不等於實驗室生化安全保證，未來須結合物聯網感測與在地法規資料庫。 |
