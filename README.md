# Bản tin sáng TP.HCM

Trang công khai: https://anhtuandlitc.github.io/ban-tin-sang/

- `index.html`: bản tin của ngày gần nhất (file duy nhất, font nhúng sẵn).
- `template/template.html`: khung HTML, chỗ trống `{{JOBS}}`, `{{TIME}}`, `{{FONT_*}}`.
- `template/build.py`: `python3 template/build.py "HH:MM"` ghép font và danh sách việc làm vào khung, ghi ra `index.html`. Nội dung tin, thời tiết sửa trực tiếp trong `template.html`.
- Không đưa nội dung Gmail, thông báo bảo mật hay dữ liệu cá nhân vào trang này vì ai cũng đọc được.
