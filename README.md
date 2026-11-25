# Food Guardian — DIC3

物聯網數據分析與應用：Project Proposal Refactor using OpenSpec。
本儲存庫依本次作業整理研究提案及規格，不包含系統實作與實驗結果。

## 作業要求與文件

| 要求 | 文件 |
| --- | --- |
| 1. 安裝 OpenSpec、規格驅動開發 | [操作與驗證流程](docs/openspec-workflow.md) |
| 2. A–F、5 cores、3 trade-offs、10 details | [研究提案整理](docs/proposal-strengthening.md) |
| 3. DESIGN → OpenSpec workflow | [DESIGN.md](DESIGN.md)、[規格](openspec/specs/)、[變更提案](openspec/changes/001-refactor-project-proposal/) |
| 4. Introduction refactor | [緒論](docs/introduction.md) |
| 5. Related Work refactor | [相關研究](docs/related-work.md)、[References](docs/references.md) |
| **IC4. IEEE Conference Draft for Overleaf** | [論文目錄](paper/)、[main.tex](paper/main.tex)、[模組化章節](paper/sections/)、[references.bib](paper/references.bib)、[Overleaf 匯入包](paper/ieee-food-guardian-overleaf.zip) |
| **IC4. 模組化 OpenSpec 規格變更 (000–006)** | [000-abstract](openspec/changes/000-abstract/)、[001-introduction](openspec/changes/001-introduction/)、[002-related-work](openspec/changes/002-related-work/)、[003-proposed-design](openspec/changes/003-proposed-design/)、[004-experiments](openspec/changes/004-experiments/)、[005-conclusion](openspec/changes/005-conclusion/)、[006-references](openspec/changes/006-references/) |

## 課堂三部分材料

- 第一部分：[NotebookLM 解析筆記](docs/source-notes.txt)、[A4 資訊圖表 PNG](assets/Food_Guardian_A4_Infographic.png)／[PDF](assets/Food_Guardian_A4_Infographic.pdf)。
- 第二部分：[A–F 與研究補強](docs/proposal-strengthening.md)、[約 300 字中文摘要](docs/abstract-300zh.md)。
- 第三部分：[IEEE 風格英文標題、摘要及關鍵字](docs/abstract-ieee.md)。

解析筆記與舊圖表保留為課堂材料，其中未核實的文獻不作正式論據；正式引用及設計以本版相關研究與 DESIGN 為準。所有實驗數量均為規劃，未宣稱已取得結果。

## OpenSpec 驗證

使用 Node.js >=22.20.0：

```bash
npm ci --prefix tooling
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec status --all
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec validate --all --strict --no-interactive
```
