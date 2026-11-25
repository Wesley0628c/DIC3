# 第三部分：Food Guardian IEEE 風格英文摘要

**Title—Food Guardian: An Inventory-Aware AI Agent for Household Food Management and Waste Reduction**

**Abstract—** Household food waste motivates the development of tools that connect available ingredients with practical meal planning. However, generated recipes require verification against ingredient quantities, storage information, and user constraints before they can support actionable decisions. This study proposes Food Guardian, an inventory-aware artificial intelligence agent that combines natural-language interaction with database retrieval, food-storage rules, and usage analysis. A large language model coordinates tool calls and generates candidate meals, while deterministic modules check ingredient availability, enforce defined constraints, and prioritize eligible ingredients by relevant dates. Missing storage information triggers clarification, and inventory changes require user confirmation. The prototype will use Python, Streamlit, SQLite, Pandas, and a source-documented rule base. Evaluation will employ 20–30 ingredient types, 20–30 recipes, and 30 scenarios covering sufficient inventory, shortages, date-related conditions, incomplete information, and preference conflicts. Comparisons will include a general language model and an inventory-conditioned model receiving the same inventory and rule information as Food Guardian. Assessment will measure recipe feasibility, inventory matching, date-reminder accuracy, rule violations, clarification behavior, and feasible-solution coverage. The expected contributions are an explainable prototype, traceable decision records, and a reproducible evaluation procedure for studying the integration of language-model planning with explicit inventory constraints. No experimental results are claimed at the proposal stage; effects on actual household food waste will require subsequent field evaluation.

**Index Terms—** Artificial intelligence agents, household food waste, inventory management, recipe recommendation, food-storage rules, tool calling.

---

本文件依課堂範例提供英文標題、單段摘要及關鍵字，未套用特定期刊投稿模板。摘要與[第二部分研究補強](proposal-strengthening.md)使用相同研究範圍及評估設定；正式投稿前再依目標期刊核對字數與格式。
