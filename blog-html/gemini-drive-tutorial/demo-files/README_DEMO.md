# HƯỚNG DẪN CHUẨN BỊ TỆP DEMO (FILE CONVERSION GUIDE)

Để các kịch bản trong Blog hoạt động đúng với giao diện Gemini (File Viewer, Side panel), bạn hãy chuyển đổi các tệp `.txt` và `.csv` sang định dạng Google Workspace như sau:

| Tên tệp gốc | Chuyển đổi thành định dạng | Mục đích sử dụng |
| :--- | :--- | :--- |
| `AI_Quest_Proposal_Final_v2.txt` | **Google Docs** | Tìm kiếm bản đề xuất mới nhất (Kịch bản 1) |
| `Technical_Spec_v1.0.txt` | **PDF** | Tóm tắt đặc tả & câu hỏi tồn đọng (Kịch bản 2) |
| `Project_Plan_V1.txt` | **Google Docs** | Làm dữ liệu gốc để so sánh (Kịch bản 3) |
| `Budget_Sheet_V2.csv` | **Google Sheets** | Dữ liệu ngân sách để so sánh (Kịch bản 3) |
| `Meeting_Notes_2026-03-24.txt` | **Google Docs** | Trích xuất Action Items (Kịch bản 4) |
| `Marketing_Plan_Q4.txt` | **Google Slides** | Chiến dịch Marketing (Kịch bản 5) |
| `Ad_Spend_Q4.csv` | **Google Sheets** | Tổng hợp ngân sách quảng cáo (Kịch bản 5) |
| `Compliance_Guide.txt` | **PDF** | Tìm kiếm chi tiết tuân thủ ISO 27001 (Kịch bản 6) |
| `Project_Timeline.txt` | **Google Slides** | Lộ trình dự án (Bổ trợ Kịch bản 1) |

## Danh sách câu Prompt (Query) để Copy & Test:

| Kịch bản | Tên tệp tham chiếu | Câu Prompt (Hãy Copy đoạn này) |
| :--- | :--- | :--- |
| **1. Tìm file mới nhất** | `AI_Quest_Proposal_Final_v2` | `@Gemini Drive Tutorial Find the latest project proposal for AI Quest that was recently updated with a new budget.` |
| **2. Tóm tắt PDF** | `Technical_Spec_v1.0.pdf` | `@Gemini Drive Tutorial Summarize this PDF tech spec and list 5 open technical questions that haven't been resolved yet.` |
| **3. So sánh tài liệu** | `Project_Plan_V1` & `Budget_Sheet_V2` | `@Gemini Drive Tutorial Compare @Project_Plan_V1 and @Budget_Sheet_V2. What is the main difference in costs?` |
| **4. Trích xuất Action Items** | `Meeting_Notes_2026-03-24` | `@Gemini Drive Tutorial Identify all action items and assignees mentioned in these meeting notes.` |
| **5. Tổng hợp đa nền tảng** | `Marketing_Plan_Q4` & `Ad_Spend_Q4` | `@Gemini Drive Tutorial Summarize the Q4 marketing plan. What is the total ad spend across all channels?` |
| **6. Tìm chi tiết kỹ thuật** | `Compliance_Guide.pdf` | `@Gemini Drive Tutorial @Compliance_Guide What are the specific requirements for data encryption according to ISO 27001?` |

*Lưu ý: Bạn có thể gõ câu hỏi bằng Tiếng Việt, nhưng Gemini trong Drive hiện tại hoạt động ổn định nhất khi dùng Tiếng Anh cho các tác vụ phân tích sâu.*
