# Mẫu điền cho LAB 10

Các mẫu này để học viên điền trong buổi lab. Mỗi mẫu là **một bước làm thật** của đề hoặc của thẻ sự cố, không phải phụ lục.
Chúng phỏng theo hai nguồn, viết lại bằng tiếng Việt trên tình huống LogiX-VN, **không chép nguyên văn**.
## Mẫu phỏng theo worksheet Google PAIR Guidebook (https://pair.withgoogle.com/guidebook)

Nguyên tắc: chỉ dùng worksheet ở chỗ nó giúp bàn làm bước đó tốt hơn. Mỗi mẫu giữ đúng cách làm của bài tập gốc; chỗ nào LAB 10
đổi hoặc thêm thì ghi rõ trong mẫu.

| Mẫu | Worksheet · bài tập gốc (bản lưu) | Là bước nào | Ai điền |
|---|---|---|---|
| `pair-success-criteria.md` | User Needs + Defining Success · "Define success criteria" (tr. 9–10) | Câu 1.6, ngay trước khi ký Bản tiêu chí | mọi bàn |
| `pair-data-map.md` | Data Collection + Evaluation · "Get to know your data" (tr. 2–3) | Câu 2.2 (ví dụ drift lấy từ dòng "thế giới thật"); mở lại ở thẻ S1, S3, S5 | mọi bàn |
| `error-audit.md` | Errors + Graceful Failure · "Error audit" (tr. 2–4) | Câu 2.5 (một lỗi của bộ nền) và câu 3.1 của **mọi thẻ** | mọi bàn |
| `pair-control-map.md` | Feedback + Control · "User expectations for control" (tr. 2–3) | Phiếu riêng của thẻ **S2**; ở thẻ **S8** chỉ điền dòng "hoàn trên hạn mức" | bàn bốc S2, S8 |
| `pair-mental-models.md` | Mental Models · "Existing vs. new mental models analysis" (tr. 2–4) | Phiếu riêng của thẻ **S6** | bàn bốc S6 |
| `pair-trust-calibration.md` | Explainability + Trust · "Trust calibration" (tr. 2–5) | Phiếu riêng của thẻ **S7** (người đặt, người nhận) và thẻ **S8** (nhân viên duyệt, trưởng ca đứng tên) | bàn bốc S7, S8 |

**Bài tập PAIR cố ý không dùng** (để khỏi gượng ép):

| Worksheet · bài tập | Vì sao bỏ |
|---|---|
| User Needs · Evidence of user need, Augmentation vs automation, Design your reward function | Là việc của giai đoạn trước PoC; LAB 10 bắt đầu ở Bước đánh giá 1, khi các lựa chọn đó đã xong |
| Data Collection · Speak with a domain expert, Data collection matrix, Data labelers + task design | Lab không thu thập hay gán nhãn dữ liệu mới |
| Data Collection · Data disaster/diligence headlines | Trùng vai với pre-mortem và fault tree; thêm vào chỉ tốn phút mà không đổi kết quả phân tích |
| Errors · Quality assurance | Phần theo dõi sau triển khai đã được câu 1.4 (telemetry) và ô "phát hiện" của grader phủ |
| Feedback + Control · Feedback audit, Validate feedback mechanisms | Trợ lý trong lab không có kênh phản hồi của người dùng cuối |
| Mental Models · Creating onboarding | Không có giao diện để viết onboarding |
| Explainability + Trust · Explanation strategy, Test with user research | Không có giao diện giải thích và không có người dùng thật trong buổi |
| Feedback + Control, Mental Models, Explainability + Trust ở các thẻ S1, S3, S4, S5 | Nguyên nhân của các thẻ này nằm ở dữ liệu, ở hành động của tool, hoặc ở con số vận hành và kinh doanh; ba worksheet đó không giúp tìm ra nhánh nào |

## Mẫu theo khung CMU MLiP và deck học viên

| Mẫu | Dùng ở | Nguồn ý tưởng |
|---|---|---|
| `measure-data-operationalization.md` | Câu 1.3, 1.4; metric monitor ở khối 3 | Ba ô Measure / Data / Operationalization của đề CMU MLiP Midterm 1 F25 (tr. 2–3) |
| `hazop.md` | Vòng 1 (kể cả phần mở rộng ra ngoài kỹ thuật) và câu 3.1, mọi thẻ | Năm guideword cho thành phần ML trong bài giảng rủi ro của CMU MLiP |
| `fault-tree.md` | Câu 3.4 và 3.7, mọi thẻ | Fault tree và thứ tự câu rủi ro của đề CMU (tr. 6–7); bài tập I2 |
| `pre-mortem-risk-register.md` | Pre-mortem bốn lăng kính: vòng 1, mọi bàn; mở lại ở vòng 2. Dòng Risk register: mọi thẻ | Pre-mortem dự án của Gary Klein (HBR 2007); cột Risk register theo deck trang 58 |
| `runbook.md` | Vòng 1 (phần 1–3) và vòng 2 (phần 4–5), mọi bàn; vai Vận hành và pháp lý cầm bút | Bốn câu hỏi: ai chịu trách nhiệm, nhìn gì, ngưỡng nào, làm gì; viết riêng cho LogiX-VN |
| `golive-checklist-9-groups.md` | Câu 2.6 (lần đầu), câu 3.7 (cập nhật) | Checklist go-live 9 nhóm việc, deck trang 61 |
| `gate1-decision.md` | Phút 100–115 (v1), 185–200 (v2) | Bốn quyết định ở deck trang 21–22; ba câu hỏi Go/No-Go của CMU |
| `experiment-log.md` | Suốt buổi | Deck trang 35 và 64 |

**Bản quyền:** tài liệu khoá CMU MLiP là CC BY-SA 4.0, sách là CC BY-NC-ND 4.0. Mọi mẫu ở đây chỉ phỏng theo cách làm, tự viết lại, và ghi tên worksheet cùng nguồn ở đầu mẫu.

"Pre-mortem dự án" ở đây là kiểu của Klein. CMU có một bài "pre-mortem làm việc nhóm" khác hẳn; LAB 10 không dùng bài đó.
