# Mẫu: Nhật ký thử nghiệm

**Bàn:** ______ · **Thẻ đã bốc:** ___ *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`.)*

*Yêu cầu: ít nhất 3 lần chạy, mỗi lần đổi một thứ, có mã lần chạy và khoảng tin cậy.*

Nguyên liệu có sẵn: mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Việc của đội là điền cột
"Đổi MỘT thứ gì" (tham số `--note`) và cột "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | base · base | (baseline, chưa có cổng) | | | | | |
| 2 | | Sx · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | | | | | |
| 3 | | Sx · after | | | | | | |
| 4 | | base · after | (kiểm không regression) | | | | | |

Mọi con số trong báo cáo go/no-go phải trỏ về một dòng ở đây.
