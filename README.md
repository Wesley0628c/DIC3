# Food Guardian — DIC4: Overleaf Draft for Conference using MCP and OpenSpec

物聯網數據分析與應用：DIC4 Conference Paper Draft using OpenSpec & Overleaf Sync。
本儲存庫為獨立研究與論文工作區，專注於規格驅動開發（OpenSpec）、IEEE/ICEB 會議論文初稿（Overleaf 同步）與 CI 自動化驗證，不包含實體系統實作與未經證實之實驗結果。

## 作業要求與文件索引

| 要求 | 文件與目錄 |
| --- | --- |
| 1. 安裝 OpenSpec、規格驅動開發 | [操作與驗證流程](docs/openspec-workflow.md) |
| 2. A–F、5 cores、3 trade-offs、10 details | [研究提案整理](docs/proposal-strengthening.md) |
| 3. DESIGN → OpenSpec workflow | [DESIGN.md](DESIGN.md)、[規格庫](openspec/specs/)、[001 變更提案](openspec/changes/archive/2026-11-25-001-refactor-project-proposal/) |
| 4. Introduction refactor | [緒論](docs/introduction.md) |
| 5. Related Work refactor | [相關研究](docs/related-work.md)、[References](docs/references.md) |
| **DIC4. IEEE / ICEB 論文手稿 (Overleaf)** | [ICEB paper/](ICEB%20paper/)、[main.txt](ICEB%20paper/main.txt)、[main.tex](ICEB%20paper/main.tex)、[模組化章節](ICEB%20paper/sections/)、[references.bib](ICEB%20paper/references.bib) |
| **DIC4. A2Z SOP 研究方法論與參考庫** | [myRef/](myRef/)、[A2Z 參考標準](myRef/A2Z%20outline%20example.md)、[A2Z SOP 手冊](myRef/A2Z-SOP-reference.md) |
| **DIC4. 模組化 OpenSpec 規格變更 (000–006)** | [000-abstract](openspec/changes/000-abstract/)、[001-introduction](openspec/changes/001-introduction/)、[002-related-work](openspec/changes/002-related-work/)、[003-proposed-design](openspec/changes/003-proposed-design/)、[004-experiment](openspec/changes/004-experiment/)、[005-conclusion](openspec/changes/005-conclusion/)、[006-reference](openspec/changes/006-reference/)、[write-iceb-paper](openspec/changes/write-iceb-paper/) |
| **DIC4. GitHub Actions CI 自動化驗證** | [.github/workflows/openspec-validate.yml](.github/workflows/openspec-validate.yml) |

## Overleaf ↔ GitHub 雙向自動同步使用方式

本專案支援透過 GitHub 直接同步至 Overleaf：
1. 進入 [Overleaf](https://www.overleaf.com/) $\rightarrow$ **New Project** $\rightarrow$ **Import from GitHub**。
2. 選擇本儲存庫 `Wesley0628c/DIC3`。
3. 在 Overleaf 專案設定中，**Main document** 選擇 `ICEB paper/main.tex`（或將 `ICEB paper/main.txt` 重命名為 `main.tex`）。
4. 本機每次修改推送至 GitHub 後，在 Overleaf 點擊左上角 **Menu** $\rightarrow$ **Git** $\rightarrow$ **Pull from GitHub** 即可雙向同步。

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
