# Eval results - Notebook chat vs traditional RAG (10 questions, fictional AQ-200 docs)

| # | Type | Ground truth | RAG (flash-lite, top-5) | RAG s | Notebook chat | NB s |
|---|---|---|---|---|---|---|
| Q1 | lookup | Airflow blocked by packaging: plastic bag not removed from a new filter (shows in first 30 min). Unplug, remove the bag, reinstall, restart. | ❌ False refusal: E03 row is split across chunks by PDF table extraction; top-1 chunk had the code but not the fix | 6.974 | ✅  | 11.7 |
| Q2 | lookup | 450 m3/h; 38-55 m2. | ✅  | 6.551 | ✅  | 12.7 |
| Q3 | multi-step | FL-200H main filter, $39 (or 2-pack FL-200H-2 $70); hold Filter Reset 3 s. | ✅ Did not mention the 2-pack | 5.062 | ✅ Also offered the FL-200H-2 2-pack | 9.7 |
| Q4 | multi-step | Every 4 months -> 3 x FL-200P $59 = $177 + UV-200 $35 = $212/year. | ❌ False refusal: maintenance (4 months) and price chunks not both in top-5 | 5.536 | ✅ 3 x $59 + $35 = $212 | 10.7 |
| Q5 | aggregation | 3,790 units (Lite 1,245 + AQ-200 1,890 + Pro 655). | ✅ 3,790 with per-month sums | 6.865 | ❌ Monthly totals correct (1,240/1,180/1,370) but stated grand total 3,490 instead of 3,790 - arithmetic error | 9.6 |
| Q6 | aggregation | March 2026, 47 tickets; firmware 2.3 Wi-Fi reconnect issue (E11), fixed by 2.3.1 on 28 March. | ✅  | 5.775 | ✅  | 13.8 |
| Q7 | numeric cross-doc | 3,285 units x $349 = $1,146,465. | ❌ False refusal: price list chunk not retrieved together with sales table | 5.098 | ✅ $1,146,465 with breakdown | 9.7 |
| Q8 | lookup-filter | E08 (VOC sensor failure) and E13 (UV-C lamp fault). | ✅  | 5.218 | ✅  | 10.7 |
| Q9 | faq | No - not where humidity is above 80% or it can be splashed. | ❌ False refusal: safety-note chunk not in top-5 | 5.834 | ✅  | 10.7 |
| Q10 | unanswerable | Not in the documents (should refuse / say not found). | ✅ Refused correctly | 5.169 | ✅ Said sources do not contain AQ-300; offered web research | 8.7 |

**Summary:** RAG 6/10 correct (0 invented facts, 4 false refusals), median 5.775 s, total $0.00621. Notebook 9/10 correct (1 arithmetic error, 0 refusals), median 10.7 s. Both cite sources.
