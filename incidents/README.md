# incidents/ · Gói sự cố (chưa có gì ở đây cho tới phút 125)

Thư mục này cố ý để trống lúc đầu buổi. Đây là chỗ các **gói sự cố** sẽ xuất hiện.

**Phút 125**, sau giờ nghỉ, Lab Coach phát thẻ sự cố cho cả lớp cùng lúc. Khi Lab Coach báo "đã phát":

1. Chạy lệnh sau từ thư mục repo của bàn:

   ```bash
   git pull --no-rebase --no-edit
   ```

   Phải gõ đủ phần `--no-rebase --no-edit`. Nếu bàn đã lưu bài bằng `git commit`, lệnh `git pull` trơn sẽ báo `fatal: Need to specify how to reconcile divergent branches`. Nếu máy báo `Please tell me who you are`, làm bước 2b ở mục 2 của `README.md` rồi chạy lại.

2. Bạn sẽ thấy 8 thư mục mới `incidents/S1/` … `incidents/S8/`, và một file mới `incident-cards.md` nằm cạnh `README.md`.
3. Mỗi **cặp bàn** (Lab Coach đã ghép sẵn) cử một người lên **bốc số**; hai bàn trong cặp làm cùng một thẻ. Số bốc được là một trong S1–S8. Lab Coach ghi số đó vào sổ.
4. Bàn **chỉ làm đúng thẻ đã bốc**. Mở `incidents/Sx/card.md` (thay `Sx` bằng số của bàn) và đọc mặt trước.
5. Ghi số đó vào dòng `Thẻ đã bốc:` ở đầu hai phiếu `templates/gate1-decision.md` và `templates/experiment-log.md`.
6. Chạy ngay `python3 -m lab10.grade --incident Sx`, khi chưa sửa gì, để xem cổng bàn dựng ở vòng 1 đỡ được bao nhiêu.

Mỗi thư mục `incidents/Sx/` sẽ có:

| File | Nó là gì |
|---|---|
| `card.md` | Thẻ sự cố: mặt trước là tin nhắn báo sự cố, mặt sau là nhiệm vụ và luật |
| `tickets.jsonl` | Các ticket của sự cố, kèm kết quả đúng |
| `world_patch.json` | Dữ liệu bổ sung của sự cố (đơn hàng, phê duyệt, sổ cái có sẵn…) |
| `card.json` | Hai lệnh chạy và tự kiểm tra của thẻ |

Không sửa các file này: chúng bị khoá, lệnh tự kiểm tra sẽ phát hiện.

Nếu chạy lệnh tự kiểm tra (`python3 -m lab10.grade`) trước khi `git pull`, bạn sẽ thấy dòng `TỪ CHỐI KIỂM TRA: chưa có gói sự cố …`. Đó là đúng thiết kế, không phải lỗi máy.
