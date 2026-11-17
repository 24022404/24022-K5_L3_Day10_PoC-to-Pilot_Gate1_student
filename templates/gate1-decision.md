# Mẫu: Bản ghi quyết định Bước đánh giá 1 (Gate 1) · v1 và v2

**Bàn:** ______ · **Thẻ đã bốc:** ___ *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

*Bốn quyết định và quy tắc "chỉ Tiếp tục khi mọi chỉ số bắt buộc đều đạt" theo deck LEC 10, trang 21–22. Ba câu hỏi tự vấn
mượn ý từ phần Go/No-Go của CMU MLiP. Ba dòng bắt buộc lấy cảm hứng từ câu rủi ro của đề CMU MLiP Midterm 1 F25.*

**Khung tư duy.** Gate 1 "đạt" khi **quyết định khớp bằng chứng và khớp tiêu chí đã ký trước**. Tiếp tục, Thu hẹp, Cải tiến
thêm, Dừng đều có thể là quyết định đạt. Quyết định không đạt là quyết định mà con số trong report không đỡ được.

Ba câu tự vấn trước khi viết: (1) Rủi ro còn lại có chấp nhận được như hiện trạng không? (2) Cần thêm biện pháp nào, tốn
bao nhiêu thời gian? (3) Có phần nào của dự án không nên làm tiếp?

| | **v1** (phút 105–115, TRƯỚC khi nhận thẻ sự cố) | **v2** (phút 185–200, SAU sự cố) |
|---|---|---|
| Hash Bản tiêu chí đã ký (8 ký tự) | | phải giống v1 |
| Hash chốt cổng vòng 1 (8 ký tự, lệnh `lab10.checkpoint` in ra) | | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | bộ nền, mốc base: ________ · bộ nền với cổng vòng 1: ________ | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | | |
| Bằng chứng 2 | | |
| Bằng chứng 3 | | |
| Khớp dòng nào trong `decision_rule` đã ký? | | |
| Nếu Thu hẹp: cắt phần nào, vì sao | | |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | | |
| Nếu Dừng: bài học ghi lại | | |
| Ngày quyết định lại (trừ khi Dừng) | | |
| PIC ký | | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Nếu chọn Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu: …
- **Ba dòng bắt buộc**
 1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
 2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
 3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
