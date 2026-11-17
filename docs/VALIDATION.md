# 本機驗證報告
日期：2026-11-17（Asia/Taipei）。此報告來自 DIC3 本機執行；未沿用參考 repo 的 Live 成績。

## 執行環境
macOS arm64、Python 3.11.13、專案內 .venv。完整套件快照見 [requirements-tested.txt](../requirements-tested.txt)；pip check 回報沒有相依衝突。
OpenSpec 2.1.0；Node 22.14.0。OpenSpec 套件要求 Node >=22.20.0，本機安裝有 engine 警告，但以下命令確實執行成功；乾淨環境應使用符合要求的版本。

## 實際結果
| 檢查 | 結果 | 證據 |
| --- | --- | --- |
| Python 測試 | **54 passed、1 skipped** | [pytest.txt](../evaluation/results/local-2026-11-17/pytest.txt) |
| OpenSpec strict | **4/4 通過**：3 specs、1 change，無 issues | [openspec.json](../evaluation/results/local-2026-11-17/openspec.json) |
| 離線評估 | **25 PASS、5 NOT_RUN**，共 30 組 | [summary.json](../evaluation/results/local-2026-11-17/summary.json)、[逐題 CSV](../evaluation/results/local-2026-11-17/offline_results.csv) |
| 套件相依 | No broken requirements found | [pip-check.txt](../evaluation/results/local-2026-11-17/pip-check.txt) |
| 本機服務 | 127.0.0.1:8501，health endpoint 回傳 ok | 本次啟動；停止服務後需重新啟動 |

## 測試涵蓋
- 有限正數、資料欄位、有效批次與歷史快照。
- 並行扣料防超額、事件失敗回滾、重複 operation ID 去重、變更 payload 拒絕、過時餘量拒絕。
- 日期今日／門檻邊界、缺日期 review、逾期 Use By blocked、Best Before review。
- 人數縮放、質量／容量內換算、包與重量不可推定、排序不掩蓋缺額、排除食材。
- Agent 白名單、複合意圖及 mock 模型工具調度，唯讀庫存。
- 固定參考日期傳入 Gemini 工具；避免 fixture 日期與系統日期漂移造成誤判。
- Streamlit AppTest 跑過五頁：空庫存與 25 筆示範庫存；開啟／取消新增、取消使用、確認使用與統計頁更新。這是程式化介面驗證，非真實使用者研究或瀏覽器截圖驗收。

## 不能據此推論的結果
1 skipped 是選用 ChromaDB 的 mock-embedding 測試；本機未安裝 RAG 套件，未下載 embedding，也未驗證真正語意檢索。五題 RAG 評估的 PASS 僅為來源欄位／靜態文件檢查。五題 multi_tool 為 NOT_RUN，沒有呼叫雲端模型。

54 項測試通過不代表 54 個真實家庭或模型回答正確。未執行 Live API、人工 groundedness／任務完成度評分、B0／B1／P 控制實驗或減廢實地試驗。參考 repo 的人工審核模板仍待實際填寫。

## 重現
```bash
.venv/bin/python -m pytest tests -q
.venv/bin/python evaluation/run_evaluation.py --output evaluation/results/my-run
.venv/bin/python -m pip check
OPENSPEC_TELEMETRY=0 tooling/node_modules/.bin/openspec validate --all --strict --no-interactive
```
requirements-ai.txt 支援 mock Gemini graph 測試；完整 RAG 測試需 requirements-rag.txt。請使用新 output 路徑保留各輪原始結果。模型工具調度目前以 mock 驗證，不以環境有套件就宣稱雲端測試成功。
