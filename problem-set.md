# LAB 10 · Đề xuyên suốt: Hồ sơ Gate 1 cho trợ lý hoàn tiền LogiX-VN

> **Lấy cảm hứng từ CMU MLiP** (Machine Learning in Production, Midterm 1 F25, tr. 1–9):
> chỉ mượn **cấu trúc ba khối** (đo lường → kiểm thử →
> rủi ro với một tác hại cụ thể cho bên thứ ba) và kiểu câu trả lời theo ô. Tình huống, câu chữ, số liệu đều viết mới cho LogiX-VN;
> không dùng kịch bản của đề gốc.
>
> **Không chấm điểm tại lớp.** Bài được một team chấm tự động chấm sau buổi học. Trong buổi, lệnh `lab10.grade` chỉ để bàn
> **tự kiểm tra**; Lab Coach hỗ trợ và hỏi soi lúc demo, không cho điểm. Bàn nộp thư mục `submission/` (xem phần D).

## Hai vòng, ba mốc

| Vòng | Bàn làm gì | Mốc để so sánh |
|---|---|---|
| **Vòng 1** (phút 15–115), chưa biết sự cố | Mục tiêu và thước đo → viết Bản tiêu chí → **ký tiêu chí TRƯỚC khi chạy đánh giá lần nào** (phút 45–50) → đo mốc base → pre-mortem, HAZOP, checklist 9 nhóm việc → **code 2–3 cổng phòng ngừa** và đặt cổng kinh doanh, vận hành, pháp lý → **chốt cổng vòng 1** → quyết định **v1** | **base**: chưa có cổng nào |
| **Vòng 2** (phút 125–200), sau khi `git pull` và bốc thẻ | **Chạy tự kiểm tra trước, chỉ với cổng vòng 1** → phân tích → sửa → quyết định **v2** | **prepared**: chỉ có cổng vòng 1 · **after**: sau khi sửa |

Demo cuối buổi so sánh ba mốc **base · prepared · after**: cổng bàn chuẩn bị trước đỡ được gì, phần nào phải sửa sau.

## Thời gian

| Phần | Phút trên đồng hồ lab | Thời lượng |
|---|---|---|
| Mở đầu, chia vai | 0–15 | 15' |
| Khối 1 · Mục tiêu và đo lường (viết xong Bản tiêu chí) | 15–45 | 30' |
| **Ký tiêu chí** (trước khi chạy đánh giá lần nào) | 45–50 | 5' |
| Khối 2A · Tìm rủi ro trước khi nó xảy ra | 50–75 | 25' |
| Khối 2B · Cổng phòng ngừa | 75–100 | 25' |
| Chốt cổng vòng 1 · quyết định v1 | 100–115 | 15' |
| Nghỉ | 115–125 | 10' |
| Khối 3 · Sự cố (git pull, bốc thẻ, mốc prepared, phân tích, sửa) | 125–185 | 60' |
| Quyết định v2 · runbook · gom bài nộp | 185–200 | 15' |
| Demo ba mốc | 200–230 | 30' |
| Tổng kết | 230–240 | 10' |

## Ba vai trong bàn (4–5 người; vai nào cũng có việc ở cả hai vòng)

| Vai | Cầm bút ở vòng 1 | Cầm bút ở vòng 2 | File chính |
|---|---|---|---|
| **Kỹ sư cổng** (1–2 người) | Chạy mốc base, dò trace, behavioral test, code 2–3 cổng phòng ngừa | Dò trace sự cố, sửa cổng, thêm chỉ số theo dõi, chạy ba mốc | `lab10/guards.py`, `lab10/monitors.py` |
| **Sản phẩm và kinh doanh** (1–2 người) | Mục tiêu, thước đo, bản đồ dữ liệu, lăng kính kinh doanh của pre-mortem, cổng `business`, tiêu chí để ký | Đọc chi phí mỗi ticket, ROI, trần tiền; quyết định phạm vi pilot; viết quyết định v2 | `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`, `templates/gate1-decision.md` |
| **Vận hành và pháp lý** (1 người) | HAZOP mở rộng, checklist 9 nhóm việc có PIC, cổng `operations` và `legal`, runbook phần 1–3 | Đọc hàng chờ người duyệt, số người trực, bên thứ ba bị ảnh hưởng; runbook phần 4–5; gom bài nộp | `config/operating_gates.json` mục `operations` và `legal`, `templates/runbook.md`, `templates/golive-checklist-9-groups.md`, `submission/` |

Mọi quyết định (v1, v2) do cả bàn chốt. Người không viết code vẫn đọc trace cùng Kỹ sư cổng và chỉ ra ticket nào còn hỏng.

---

# PHẦN A · VÒNG 1 (phát đầu buổi)

## Tình huống

LogiX-VN đã chạy PoC trợ lý xử lý yêu cầu hoàn tiền giao trễ. Trợ lý đọc ticket, tra đơn và tracking, áp chính sách hoàn tiền, ghi sổ cái, ghi lỗi cho hãng vận chuyển chịu trách nhiệm, báo cho hãng và trả lời khách. Bàn của bạn là nhóm chuẩn bị **hồ sơ Bước đánh giá 1**: có đáng chạy thử với người dùng thật ở 2 depot không (deck trang 20).

Bạn có: eval card và PRD v1.1 từ Lab 9; codebase Day 10 với bộ nền 22 ticket × 5 seed; MockLLM tất định nên mọi lần chạy tái lập được. Mỗi lần chạy còn cho các con số kinh doanh và vận hành: tỉ lệ chuyển người duyệt, thời gian chờ người duyệt, số ca bị ùn, chi phí mỗi ticket so với làm tay, ROI, tổng tiền hoàn so với trần.

Câu trả lời phải bám tình huống LogiX và dữ kiện trong code. Trả lời chung chung không đạt.

## Khối 1 · Mục tiêu và đo lường (30 phút, phút 15–45), rồi ký (phút 45–50)

**Đặt luật trước, xem số sau.** Trong khối này bàn **chưa chạy trợ lý lần nào**. Bàn viết xong Bản tiêu chí rồi ký ở phút 45–50; chỉ sau khi ký mới được chạy `lab10.eval`. Nếu chạy sớm, lệnh sẽ từ chối và nhắc bàn ký trước. Câu 1.5 cho sẵn một kết quả để tập đọc khoảng tin cậy; đó không phải lần chạy của bàn.

> **Khung tư duy: Thước đo → Dữ liệu → Cách tính (CMU) cho câu 1.3–1.4; Define success criteria (worksheet PAIR User Needs) cho câu 1.6**
> - Câu hỏi dẫn dắt: thành công nhìn từ ai? Con số nào, tính thế nào, để hai người độc lập ra cùng kết quả? Điều gì phải viết ra trước khi xem bằng chứng?
> - Ví dụ mẫu: xem `templates/measure-data-operationalization.md` và `templates/pair-success-criteria.md`.

| Câu | Nội dung | Phút | Vai cầm bút | Công cụ hướng dẫn |
|---|---|---|---|---|
| **1.1** | Nêu **một mục tiêu cấp hệ thống** của trợ lý (không cần thước đo). Phải khác "model trả lời đúng" | 2 | Sản phẩm và kinh doanh | PRD v1.1 §3 |
| **1.2** | Nêu **một mục tiêu nhìn từ chị Oanh, kế toán đối soát** (người không dùng trợ lý nhưng phải khớp sổ với hãng và shop mỗi tuần), và **một mục tiêu nhìn từ chị Hạnh, trưởng ca CSKH** (người phải duyệt những ca trợ lý chuyển sang) | 3 | Vận hành và pháp lý | PRD v1.1 §2 (phạm vi), §6 (rủi ro mở); `data/world.json` → `staff` |
| **1.3** | Chọn **MỘT bước** của agent (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Thiết kế **một offline metric** cho riêng bước đó: Thước đo · Dữ liệu (lấy gì, ở đâu, ai gán nhãn) · Cách tính | 7 | Kỹ sư cổng | `templates/measure-data-operationalization.md`; eval card Lab 9 |
| **1.4** | Thiết kế **telemetry production** để biết trợ lý có đang gây thiệt hại cho bên ngoài LogiX không. Cùng ba ô, thêm **khung thời gian** và **ngưỡng báo động**. Không có nhãn trong production | 5 | Vận hành và pháp lý | `templates/measure-data-operationalization.md` |
| **1.5** | Đọc kết quả sau rồi chọn MỘT kết luận đúng và giải thích một câu: bản X trên bộ nền có pass_rate 0,9909 (109/110 lần chạy), khoảng tin cậy 95% [0,9727; 1,0]. Bản Y có pass_rate 1,0 (110/110). (a) Y tốt hơn X có ý nghĩa thống kê. (b) Chưa đủ căn cứ nói Y tốt hơn X; chênh 1 lần chạy nằm trong khoảng tin cậy của X. (c) X và Y chắc chắn như nhau. (d) Phải chạy thêm seed thì X mới đạt. *(Số cho sẵn để tập đọc; bàn không tự chạy đánh giá ở khối này.)* | 3 | Cả bàn | deck: "một lần chạy chưa đủ; cần khoảng tin cậy" |
| **1.6** | **Viết Bản tiêu chí** theo `templates/pair-success-criteria.md`: (a) viết mỗi chỉ số bắt buộc thành một câu "Nếu … thì chúng tôi sẽ …"; (b) soát bốn câu hỏi (có ý nghĩa với mọi bên? ai thiệt? ngày 1? ngày 1.000?); (c) chép ngưỡng và hành động vào `config/acceptance_criteria.json`: 5 ngưỡng bắt buộc, 1 nên có, **nhóm `business_ops`** (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa), điều kiện dừng, `decision_rule` cho cả bốn quyết định. **Viết xong thì ký ngay ở phút 45–50, trước khi chạy đánh giá lần nào** | 10 | Sản phẩm và kinh doanh | worksheet PAIR User Needs "Define success criteria" (mẫu trên); `config/acceptance_criteria.example.json` (đừng chép ngưỡng) |

Ghi chú 1.5: số 0,9909, [0,9727; 1,0] và 110 lần chạy là số thật của mốc base trên bộ nền. Đề cho sẵn để dạy cách đọc khoảng tin cậy. Bàn sẽ tự chạy ra đúng các số này ở câu 2.4, sau khi đã ký.

### Ký tiêu chí (5 phút, phút 45–50)

1. Soát lại `config/acceptance_criteria.json` lần cuối: tên bàn, đủ ngưỡng, `decision_rule`, điều kiện dừng.
2. Chạy `python3 -m lab10.criteria sign`. Đọc 8 ký tự hash cho Lab Coach ghi sổ.
3. Từ lúc này **không sửa tiêu chí**. Mọi báo cáo về sau đều in hash; hash khác sổ là bài không được tính.

Bàn chưa chạy đánh giá lần nào cho tới bước này. Đó là chủ ý: ngưỡng phải được viết khi chưa ai biết trợ lý đạt hay trượt.

## Khối 2A · Tìm rủi ro trước khi nó xảy ra (25 phút, phút 50–75)

> **Khung tư duy: pre-mortem bốn lăng kính (kỹ thuật, kinh doanh, con người và vận hành, pháp lý); HAZOP (CMU) mở rộng ra ngoài code; hai bước làm bằng worksheet PAIR: Get to know your data (câu 2.2) và Error audit (câu 2.5)**
> - Câu hỏi dẫn dắt: ba tháng sau pilot phải tắt trợ lý, vì sao? Thứ gì hết trước khi lượng việc tăng gấp ba: máy, tiền, hay người? Dữ liệu của ai rời hệ thống mà họ không biết?
> - Ví dụ mẫu: xem bảng "Mở rộng ra ngoài kỹ thuật" trong `templates/hazop.md`.

Ba vai làm song song 15 phút đầu, rồi cả bàn làm pre-mortem 10 phút.

| Câu | Nội dung | Phút | Vai cầm bút | Công cụ hướng dẫn |
|---|---|---|---|---|
| **2.4** | **Lần chạy đánh giá đầu tiên của bàn (tiêu chí đã ký).** Chạy mốc **base**: `python3 -m lab10.eval --suite base --stage base --note "baseline"`, rồi `python3 -m lab10.gate --run runs/<mã>/report.json`. Ghi **mã lần chạy**. Đọc cả khối "kinh doanh và vận hành" ở cuối. Nêu lý lẽ chính ủng hộ và phản đối việc để cổng này **tự chặn** một bản phát hành (so với người duyệt), rồi khoanh khuyến nghị: tự chặn / người duyệt / kết hợp | 7 | Kỹ sư cổng | đề CMU tr. 5 (ý: ưu, nhược rồi chọn); deck "Bước đánh giá" |
| **2.5** | Dò `python3 -m lab10.trace --suite base --ticket T-002 --seed 55`. **Điền `templates/error-audit.md` cho lỗi này** (ghi lỗi + loại lỗi, tìm nguồn, hướng xử lý) | 8 | Kỹ sư cổng | worksheet PAIR Errors "Error audit" (mẫu trên) |
| **2.2** | **Điền `templates/pair-data-map.md`** (trường then chốt, nguồn sự thật hay bản sao, thế giới thật làm lệch ở đâu). Rút ra **một ví dụ drift cụ thể** trong 3 tháng tới: cái gì đổi, đổi ngày nào, trường nào cho thấy, con số nào của Bản tiêu chí bị ảnh hưởng. Gợi ý: mở `data/world.json` phần `policies`, `orders[].parcels`, `ops_limits`, `ops_facts` | 15 | Sản phẩm và kinh doanh | worksheet PAIR Data Collection "Get to know your data" (mẫu trên); khái niệm drift theo đề CMU tr. 4 |
| **2.6** | **HAZOP mở rộng** (`templates/hazop.md`): một vòng trên một tool ghi (≥ 3 dòng), cộng **ít nhất hai dòng ngoài kỹ thuật** (người duyệt, ngân sách, phạm vi pilot, dữ liệu gửi bên thứ ba). Rồi điền **checklist 9 nhóm việc lần 1**: trạng thái, bằng chứng, và **PIC có tên** cho từng dòng | 15 | Vận hành và pháp lý | `templates/hazop.md`; `templates/golive-checklist-9-groups.md` |
| **2.7** | **Pre-mortem bốn lăng kính** (`templates/pre-mortem-risk-register.md`): cả bàn, 8–10 phút. Lăng kính nào trống thì viết thêm. Chọn **2–3 lý do** sẽ thành cổng phòng ngừa ngay hôm nay | 10 | Cả bàn | pre-mortem của Gary Klein (xem mẫu) |

## Khối 2B · Cổng phòng ngừa (25 phút, phút 75–100)

> **Khung tư duy: biện pháp cấp hệ thống nằm ngoài model và prompt (CMU); rò rỉ dữ liệu, behavioral test**
> - Câu hỏi dẫn dắt: cổng này chặn trước lệnh ghi nào? Nó dựa vào nguồn sự thật nào? Nó có làm hỏng ticket đang đúng không? Con số nào không cần code, chỉ cần một người có thẩm quyền quyết?

| Câu | Nội dung | Phút | Vai cầm bút | Công cụ hướng dẫn |
|---|---|---|---|---|
| **2.8** | **Code 2–3 cổng phòng ngừa** trong `lab10/guards.py`, mỗi cổng ứng với một lý do của pre-mortem hoặc một dòng HAZOP. Chạy `python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."` và `python3 -m unittest discover -s tests`. Cổng không được làm hỏng ticket đang đúng của bộ nền | 20 | Kỹ sư cổng | hướng dẫn ở đầu `lab10/guards.py`; `lab10/helpers.py`; README phụ lục C |
| **2.1** | Bàn đang chỉnh cổng cho tới khi 22 ticket của bộ nền xanh hết. Nêu **2 bước cụ thể** để tránh rò rỉ dữ liệu (chỉnh trên chính bộ dùng để chấm). Gắn với thứ có thật trong lab: bộ nền, gói sự cố, bài kiểm tra ẩn | 3 | Kỹ sư cổng | đề CMU tr. 4 (ý: tách dữ liệu phát triển và dữ liệu chấm) |
| **2.3** | Viết **một behavioral test**: phát biểu tính chất (một câu), rồi viết **2 ticket mới** kiểm tính chất đó và chạy bằng `python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx`. Dán kết quả. Giữ 2 ticket này làm "ticket hiểm" cho phần demo | 7 | Kỹ sư cổng cùng một người không viết code | đề CMU tr. 5 (ý: kiểm tính chất, tự tạo dữ liệu thử) |
| **2.9** | **Đặt cổng kinh doanh** trong `config/operating_gates.json` mục `business`: trần tiền hoàn tự động mỗi ngày, ngân sách chi phí mỗi ticket, phạm vi pilot (tất cả / kho nào / bao nhiêu phần trăm), ngưỡng ROI. Mỗi con số kèm một câu lý do, lấy từ `data/world.json` → `ops_limits`, `ops_facts` | 12 | Sản phẩm và kinh doanh | README mục 5 "Cổng trong config"; pre-mortem lăng kính kinh doanh |
| **2.10** | **Đặt cổng con người, vận hành, pháp lý** trong `config/operating_gates.json` mục `operations` và `legal`: PIC, người duyệt, số người trực mỗi ca, công suất duyệt mỗi giờ, thời gian chờ tối đa, điều kiện dừng, kênh báo tin; trường dữ liệu cá nhân không gửi cho bên thứ ba; ghi lỗi cho hãng phải có nguyên nhân trong tracking. Viết **runbook phần 1–3** (`templates/runbook.md`) khớp với các con số đó | 20 | Vận hành và pháp lý | README mục 5; `templates/runbook.md` |

## Chốt · quyết định v1 (15 phút, phút 100–115)

Tiêu chí đã ký từ phút 45–50; ở đây không ký nữa. Làm đúng thứ tự:

1. **Chốt cổng vòng 1:** `python3 -m lab10.checkpoint`. Lệnh chụp lại `lab10/guards.py` và `config/operating_gates.json` thành mốc **prepared**. Đọc 8 ký tự lệnh in ra cho Lab Coach ghi sổ. Sau khi chốt, bàn vẫn sửa tiếp hai file gốc ở vòng 2; không sửa hai bản chụp.
2. **Quyết định v1:** chạy bộ nền ở mốc prepared (`python3 -m lab10.eval --suite base --stage prepared`), so với tiêu chí đã ký (`python3 -m lab10.gate --run runs/<mã>/report.json`), rồi điền cột **v1** của `templates/gate1-decision.md`: một trong bốn quyết định, ba dòng bằng chứng có mã lần chạy, dòng `decision_rule` tương ứng, ngày quyết định lại. Lưu một bản commit (lệnh ở README mục 7). Sau mốc này v1 không sửa được.

> **Khung tư duy: ba câu tự vấn Go/No-Go (CMU)** · Rủi ro còn lại chấp nhận được như hiện trạng? Cần thêm biện pháp nào, tốn bao lâu? Có phần nào không nên làm tiếp?

---

# PHẦN B · VÒNG 2 · SỰ CỐ (khối 3) · thẻ tới ở phút 125

## Cách tung

- Phút 125: Lab Coach báo "đã phát thẻ". Mỗi bàn chạy `git pull --no-rebase --no-edit` để tải về thư mục `incidents/S1…S8/` và file `incident-cards.md` (trước mốc này repo của bàn chưa có hai thứ đó). Mỗi **cặp bàn** cử một người lên **bốc số** (S1–S8). Bàn **chỉ làm đúng thẻ có số bốc được**: `incidents/Sx/card.md`.
- Ghi số đã bốc vào dòng `Thẻ đã bốc:` ở đầu `templates/gate1-decision.md` và `templates/experiment-log.md`.
- **Việc đầu tiên, trước khi sửa bất cứ thứ gì:** `python3 -m lab10.grade --incident Sx`. Lần chạy này cho mốc **base** và mốc **prepared** của bàn trên sự cố: cổng vòng 1 đỡ được gì, còn dòng "vượt trần" nào. Ghi mã lần chạy.
- Lab Coach đọc một câu: *"Đây là tin nhắn bàn nhận được sáng nay. Bản tiêu chí đã ký giữ nguyên. Sau 60 phút, bàn cho tôi biết quyết định Gate 1 còn đứng được không."*
- **Thẻ sự cố chính là khối 3.** Tám thẻ, mỗi thẻ một tác hại cho một bên cụ thể. Năm thẻ có nguyên nhân chính ở kỹ thuật; ba thẻ có nguyên nhân chính ở **kinh doanh hoặc con người** (lượng việc tăng làm hàng chờ ngập, chi phí mỗi ticket cao hơn làm tay, nhân viên không tin trợ lý). Ở các thẻ đó, cách sửa nằm nhiều ở phạm vi, nhân sự, giải thích, quy trình hơn là ở code.

## Khối 3 · Một tác hại cụ thể, nhiều nguyên nhân (60 phút, phút 125–185)

> **Khung tư duy: phân tích hazard (HAZOP) → fault tree → specification vs giả định môi trường → biện pháp ngoài model, giảm hay bảo đảm → cập nhật fault tree (CMU)**
> - Câu hỏi dẫn dắt: tác hại cho ai, đo bằng gì? Ngoài model còn nhánh nào dẫn tới nó: dữ liệu, quyền hạn, tiền, người? Cổng đặt ở tầng nào: phát hiện, chặn, giới hạn thiệt hại, hay vận hành? Nó giảm khả năng hay ngăn hẳn?
> - Ví dụ mẫu: ô Khung tư duy riêng trên từng thẻ; `templates/fault-tree.md`.

| Câu | Nội dung | Phút | Vai cầm bút | Công cụ hướng dẫn |
|---|---|---|---|---|
| **3.0** | **Mốc prepared.** Chạy `python3 -m lab10.grade --incident Sx` khi chưa sửa gì. Ghi: cổng vòng 1 đỡ được ô nào; khối kinh doanh và vận hành có dòng nào vượt trần; sự cố này có nằm trong pre-mortem của bàn không | 8 | Cả bàn | report của `lab10.grade`; `templates/pre-mortem-risk-register.md` (phần vòng 2) |
| **3.1** | **Phân tích hazard.** Dò ≥ 2 ticket hỏng theo kiểu khác nhau. Điền **bảng soát lỗi** (≥ 2 lỗi có nguồn khác nhau, ≥ 1 lỗi chìm). Làm **phiếu riêng của thẻ** ghi ở mặt sau thẻ. Nêu tác hại: cho ai, đo bằng gì, bao nhiêu ở mốc base | 8 | Kỹ sư cổng (trace) · Vận hành và pháp lý (phiếu riêng) | `templates/error-audit.md`; phiếu riêng của thẻ; `templates/hazop.md` |
| **3.2** | Viết **một specification** mà nếu bị vi phạm thì gây ra tác hại trên thẻ. Kiểm được bằng code hoặc bằng một con số trong report | 3 | Sản phẩm và kinh doanh | `templates/fault-tree.md` bảng dưới cây |
| **3.3** | Nêu **một giả định về môi trường** mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế | 3 | Vận hành và pháp lý | như trên |
| **3.4** | Vẽ **fault tree trước khi sửa**: sự kiện đỉnh là tác hại; ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report) | 6 | Cả bàn | `templates/fault-tree.md` |
| **3.5** | **Sửa, đúng chỗ cho từng nguyên nhân.** Code: `lab10/guards.py`. Con số và quy trình: `config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Chạy `--stage after`, rồi `python3 -m lab10.grade --incident Sx`. Ghi rõ từng biện pháp **giảm khả năng** hay **ngăn hẳn** | 25 | Kỹ sư cổng (code) · Sản phẩm và kinh doanh (`business`) · Vận hành và pháp lý (`operations`, `legal`) | thẻ sự cố, mục Nhiệm vụ |
| **3.6** | Thêm **chỉ số theo dõi** trong `lab10/monitors.py` bắt được sự cố (kỹ thuật, vận hành, hay kinh doanh đều được) | (trong 3.5) | Kỹ sư cổng | `templates/measure-data-operationalization.md` |
| **3.7** | **Cập nhật fault tree** sau khi sửa (cổng nằm ở nhánh nào, tầng nào, nhánh nào còn hở). Thêm ≥ 1 dòng Risk register. Cập nhật checklist 9 nhóm việc (cột PIC). Viết **runbook phần 4–5** | 7 | Vận hành và pháp lý | `templates/fault-tree.md`, `golive-checklist-9-groups.md`, `runbook.md` |

**Report tự kiểm tra cho bàn biết gì.** Sáu mục kiểm (file khoá, tiêu chí, gói sự cố, bài kiểm tra ẩn, bộ nền, chỉ số theo dõi); bảng **kinh doanh · vận hành · pháp lý** ở ba mốc (thời gian chờ, số ca ùn, tỉ lệ chuyển người duyệt, chi phí mỗi ticket, ROI, tổng tiền hoàn so với trần, lộ dữ liệu cá nhân, lỗi oan cho hãng); và một dòng kết: **được phép cân nhắc "Tiếp tục"** hay **không đủ căn cứ**. Bài kiểm tra ẩn (đơn khác, khách khác, cách viết khác) do team chấm chạy sau buổi học.

## Quyết định Gate 1 · v2 (15 phút, phút 185–200)

Điền cột **v2** của `templates/gate1-decision.md`: quyết định, đổi hay giữ so với v1 và vì con số nào, mã lần chạy của ba mốc, và **ba dòng bắt buộc**:

1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế.
2. Cổng của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại, và vì sao.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2.

**Quy tắc quyết định (điều kiện để bài qua):** quyết định phải khớp bằng chứng và khớp tiêu chí đã ký.
- Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký chưa đạt, là quyết định không đạt.
- **Thu hẹp** (ghi rõ cắt kho nào, còn bao nhiêu phần trăm, mấy người trực, ticket bị cắt đi đâu), **Cải tiến thêm** (giả thuyết cụ thể, có hạn), **Dừng** (bài học ghi lại) có lý do và có số thì đều là quyết định đạt.

---

# PHẦN C · DEMO BA MỐC (phút 200–230)

Hai bàn cùng thẻ ghép cặp, mỗi bàn 5 phút, rồi 2–3 bàn trình bày trước lớp. Mỗi bàn chiếu **ba cột base · prepared · after** của report và trả lời:

1. Cổng vòng 1 nào đã đỡ được sự cố này trước khi bàn biết nó? Cổng nào bàn không nghĩ tới, và nó thuộc lăng kính nào?
2. Phần sửa ở vòng 2 là code, là con số, hay là người? Vì sao đúng chỗ đó?
3. Quyết định v2, và con số nào đỡ cho nó.
4. Bàn kia đưa một ticket hiểm (câu 2.3) hoặc đổi một con số trong `config/operating_gates.json` (ví dụ bớt một người trực): chạy trực tiếp, đọc kết quả.

Lab Coach hỏi soi theo phiếu thẻ. Không cho điểm.

---

# PHẦN D · NỘP BÀI (không chấm tại lớp)

Bài nộp là thư mục `submission/`. Cách làm và danh sách đầy đủ: `submission/README.md`.

1. Điền `submission/submission.json`: tên bàn, thành viên, số thẻ, quyết định v1 và v2, ba dòng bắt buộc.
2. Chạy `python3 -m lab10.check_submission --collect`. Lệnh gom: code cổng vòng 1 (bản chốt) và vòng 2, config cổng kinh doanh + vận hành + pháp lý (bản vòng 1 và bản hiện tại), tiêu chí đã ký kèm hash, mã lần chạy và report của ba mốc, quyết định v1/v2, checklist 9 nhóm việc, runbook, pre-mortem, HAZOP.
3. Sửa các dòng `THIẾU` tới khi lệnh in `ĐỦ THÀNH PHẦN`. Commit và push.

Lệnh này chỉ kiểm **đủ thành phần**. Team chấm sẽ chấm sau buổi học theo ba lớp: phần máy đo (bài kiểm tra ẩn, chỉ số kinh doanh và vận hành, mức chuẩn bị ở mốc prepared, hash, không làm hỏng ca đang đúng); phần người đọc (pre-mortem và HAZOP có phủ kinh doanh, con người, pháp lý; checklist có PIC; runbook; ba dòng bắt buộc; câu trả lời lúc demo); và điều kiện qua (quyết định khớp bằng chứng và tiêu chí đã ký).

---

## Phụ lục · Đối chiếu cấu trúc với đề CMU (để kiểm phạm vi mượn)

| Đề CMU MLiP Midterm 1 F25 | Đề này |
|---|---|
| Câu 1 (21đ): mục tiêu hệ thống; mục tiêu từ một bên liên quan gián tiếp; offline metric cho một prompt (3 ô); đo trong production có khung thời gian (3 ô); đọc một kết quả ý nghĩa thống kê | Khối 1: câu 1.1–1.5, thêm 1.6 (tiêu chí, có nhóm kinh doanh và vận hành) |
| Câu 2 (18đ): tránh rò rỉ dữ liệu; ví dụ drift; behavioral test; CI (lý lẽ ủng hộ, phản đối, chọn) | Khối 2A–2B: câu 2.1–2.4, thêm 2.5 (error audit), 2.6–2.7 (HAZOP mở rộng, pre-mortem bốn lăng kính), 2.8–2.10 (cổng phòng ngừa bằng code và bằng config) |
| Câu 3 (18đ): một tác hại cho bên thứ ba; các bước phân tích hazard; một software specification; một giả định môi trường; một biện pháp ngoài model (giảm hay ngăn); cập nhật fault tree cho sẵn | Khối 3: câu 3.0–3.7, khác ở chỗ biện pháp phải **chạy được**, có mốc prepared để so với cổng viết trước, fault tree do bàn tự vẽ, tác hại khác nhau theo thẻ, và ba thẻ có nguyên nhân chính nằm ngoài kỹ thuật |

Điểm và thứ tự câu của đề CMU: theo bản đọc PDF tr. 2–7. Mọi câu chữ ở đây viết mới. Trọng số chấm của đề này không in ở đây vì không chấm tại lớp; team chấm có rubric riêng.
