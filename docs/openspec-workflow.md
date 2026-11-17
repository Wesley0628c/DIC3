# OpenSpec：從 DESIGN 到可驗證工作流程
本機使用 OpenSpec CLI 2.1.0。規格採 spec-driven schema；保留提案 change 供老師檢查，不自動 archive。

## 作業對照
| 課程要求 | 交付 |
| --- | --- |
| 安裝與熟悉 OpenSpec | 專案內 CLI、package-lock、驗證報告與下列操作 |
| A–F、5 核心、3 取捨、10 細節 | proposal-strengthening.md、deep-research.md |
| design.md → workflow | 根目錄 DESIGN.md → specs → change artifacts → tasks → tests |
| Introduction refactor | introduction.md |
| Related Work refactor | related-work.md、references.md |

## 安裝及重現
```bash
npm ci --prefix tooling
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec --version
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec status --change implement-food-guardian
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec validate --all --strict --no-interactive
```
CLI 2.1.0 套件要求 Node >=22.20.0；本機 Node 22.14.0 能執行本次驗證但有 engine 警告，重現建議使用符合要求版本。初始化已執行 init --tools none --scope project；沒有改寫全域 AI 設定。

## 文件角色與驗收
- DESIGN.md：整體設計、研究假設、實作對應及限制。
- openspec/specs/*/spec.md：目前功能需求，使用 SHALL 與 Given/When/Then。
- openspec/changes/implement-food-guardian/proposal.md：為何改、範圍與影響。
- change/design.md：具體決策與替代方案。
- change/specs：本次新增規格的 delta。
- change/tasks.md：完成項目與待辦；研究 Live 驗證另追蹤，不填假完成。

例：庫存更新需求 → inventory-ledger「Atomic confirmed recording」→ test_cancel_and_idempotency／test_concurrent_consumption → 原型庫存頁確認按鈕。需求格式驗證通過不等於執行語意正確，仍需 Python 測試。

## 後續變更示範
```bash
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec new change add-storage-context
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec instructions proposal --change add-storage-context
```
先寫 proposal、design、spec delta 與 tasks，再修改程式及驗證。新增保存規則前需取得適用條件與人工核實來源，不能直接採模型生成期限。
