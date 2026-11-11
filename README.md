# Food Guardian

智慧食材管理與家庭食物浪費減量 AI Agent 研究企劃。

本專案提出結合 AI Agent、食品領域知識與資料分析的智慧食材管理系統，整合庫存查詢、臨期食材排序、食譜推薦及保存風險檢查，協助家庭將現有食材轉化為可行餐點。

目前內容為研究摘要、企劃來源筆記及 A4 資訊圖表。系統實作與實驗評估尚屬規劃，預期成果不代表已完成驗證。

## 文件

- [專業摘要（A–F）](docs/abstract.md)
- [原始來源筆記](docs/source-notes.txt)
- [A4 資訊圖表 PDF](assets/Food_Guardian_A4_Infographic.pdf)
- [A4 資訊圖表 PNG](assets/Food_Guardian_A4_Infographic.png)

![Food Guardian A4 資訊圖表](assets/Food_Guardian_A4_Infographic.png)

## 規劃技術

| 項目 | 技術或方法 |
| --- | --- |
| 系統開發 | Python |
| 使用者介面 | Streamlit |
| 資料儲存 | SQLite |
| 資料分析 | Pandas |
| 推薦與規劃 | 具 Tool Calling 能力的 LLM Agent |
| 食品保存知識 | JSON 知識庫與規則檢查 |

## 實驗規劃

建立 20–30 種常見食材、20–30 道基本食譜與 30 組測試情境，與未整合真實庫存的一般 LLM 食譜推薦進行比較。評估食譜可行率、庫存匹配率與日期提醒準確率，並分析食材使用量、丟棄量及浪費比例。

## 資料說明

文件由提供的摘要、文字筆記及圖表整理而成。原始筆記保留原貌；摘要中的統計與文獻敘述尚未於本儲存庫逐項查證，正式論文需補齊可追溯的引用資料。摘要保留提供內容，篇幅未另行縮寫為 500 字。
