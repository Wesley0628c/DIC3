# DESIGN → OpenSpec Workflow

## 1. 安裝

使用 Node.js >=22.20.0，於專案根目錄執行：

```bash
npm ci --prefix tooling
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec --version
```

使用 OpenSpec 2.1.0。本機已完成初始化；不需重建現有規格。

## 2. 本次規格驅動流程

1. 依作業整理 A–F、五個核心、三項取捨與十個細節。
2. 在 DESIGN.md 定義需求、資料流、架構、流程與演算法。
3. 將設計轉成 openspec/specs/ 的 SHALL 需求及 WHEN／THEN 情境。
4. 在 changes/refactor-project-proposal/ 建立 proposal、design、spec deltas 及 tasks。
5. 重構 Introduction、Related Work，核對引用與研究缺口。
6. 驗證規格與文件對應；本次範圍為提案重構，不包含系統程式開發。

## 3. 對應範例

DESIGN 的「取消不更新庫存」→ food-guardian-workflow 的 Confirmed updates → Cancellation 情境。這使設計成為可檢查的需求，而非只有描述。

proposal-documentation 規格則要求 A–F、5／3／10、緒論、相關研究、比較表與引用。規格格式通過不等於研究結論已經實驗證實。

## 4. 檢查命令

```bash
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec status --change refactor-project-proposal
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec validate --all --strict --no-interactive
```

驗證範圍為 2 份主規格與 1 份變更提案。原先本機 Node 22.14.0 可執行 CLI，但低於套件要求，重現時應使用上述支援版本。

本次驗證：2 份主規格及 1 份變更提案均通過 strict 驗證，文件內部連結檢查通過。
