# submission/ · Bài nộp của bàn

Mọi thứ bàn nộp nằm trong thư mục này. Một team chấm tự động sẽ chấm **sau buổi học**; tại lớp không ai cho điểm.

## Làm ba bước

**Bước 1. Điền `submission.json`** (mẫu có sẵn, mở bằng trình soạn thảo bất kỳ):

| Trường | Điền gì | Ví dụ |
|---|---|---|
| `team` | Tên bàn, giống hệt trong Bản tiêu chí đã ký | `"ban-07"` |
| `members` | Họ tên các thành viên | `["Nguyễn A", "Trần B"]` |
| `incident` | Số thẻ bàn bốc được | `"S4"` |
| `decision_v1` | Quyết định Gate 1 bản v1 | `"Tiếp tục"` |
| `decision_v2` | Quyết định Gate 1 bản v2 | `"Thu hẹp"` |
| `three_lines.environment_assumption` | Một giả định về môi trường mà thiết kế của bàn dựa vào, có thể sai ngoài thực tế | một câu |
| `three_lines.reduce_or_prevent` | Cổng của bàn chỉ GIẢM khả năng hay NGĂN hẳn tác hại, vì sao | một câu |
| `three_lines.measure_in_pilot` | Vì dữ liệu ở đây là giả, cần đo lại gì khi chạy thử thật | một câu |

Quyết định chỉ nhận một trong bốn giá trị: `Tiếp tục`, `Thu hẹp`, `Cải tiến thêm`, `Dừng`.

**Bước 2. Gom file và kiểm:**

```bash
python3 -m lab10.check_submission --collect
```

Lệnh này tự chép vào đây: code cổng vòng 1 và vòng 2, config cổng, tiêu chí đã ký, báo cáo tự kiểm tra cùng ba mốc, và các phiếu bàn đã điền trong `templates/`. Sau đó nó in danh sách `ĐỦ` / `THIẾU`.

**Bước 3. Sửa chỗ `THIẾU`, chạy lại lệnh tới khi thấy `ĐỦ THÀNH PHẦN`.** Rồi nộp nguyên thư mục `submission/` theo cách Lab Coach hướng dẫn. Nếu Lab Coach không nói cách khác:

```bash
git add submission
git commit -m "LAB 10: bài nộp"
git push
```


## Bài nộp gồm gì

| Trong `submission/` | Là gì | Ai tạo |
|---|---|---|
| `submission.json` | Tên bàn, thành viên, số thẻ, quyết định v1 và v2, ba dòng bắt buộc | Bàn điền |
| `code/guards_round1.py` | Cổng phòng ngừa vòng 1, bản đã chốt | Lệnh gom |
| `code/guards.py`, `code/monitors.py` | Cổng sau khi sửa ở vòng 2, chỉ số theo dõi | Lệnh gom |
| `config/operating_gates.round1.json`, `config/operating_gates.json` | Cổng kinh doanh, vận hành, pháp lý: bản vòng 1 và bản hiện tại | Lệnh gom |
| `config/acceptance_criteria.json`, `.lock` | Bản tiêu chí đã ký và hash | Lệnh gom |
| `config/round1.lock`, `config/switches.json` | Dấu chốt vòng 1, công tắc | Lệnh gom |
| `runs/grade-report.json`, `.md` | Báo cáo tự kiểm tra gần nhất | Lệnh gom |
| `runs/<mã lần chạy>/report.json` | Ba mốc: base, prepared, after | Lệnh gom |
| `docs/gate1-decision.md` | Quyết định v1 và v2, có dòng `Thẻ đã bốc` | Bàn điền trong `templates/` |
| `docs/golive-checklist-9-groups.md` | Checklist 9 nhóm việc, mỗi dòng có người chịu trách nhiệm | Bàn điền trong `templates/` |
| `docs/runbook.md` | Runbook vận hành | Bàn điền trong `templates/` |
| `docs/pre-mortem-risk-register.md`, `docs/hazop.md` | Pre-mortem và HAZOP | Bàn điền trong `templates/` |
| `docs/fault-tree.md`, `docs/error-audit.md`, `docs/experiment-log.md` | Không bắt buộc | Bàn điền trong `templates/` |
| `manifest.json` | Danh sách file kèm dấu vân tay, mã lần chạy | Lệnh gom |

Bàn điền phiếu ngay trong thư mục `templates/`. Đừng sửa các bản chép trong `submission/docs/`: lần gom sau sẽ ghi đè.
