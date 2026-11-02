import os
import sys

try:
    import qrcode
    from PIL import Image
except ImportError:
    os.system(f"{sys.executable} -m pip install qrcode pillow")
    import qrcode
    from PIL import Image

# 🔗 3단계에서 생성된 진짜 인터넷 웹 주소를 아래에 넣어주세요!
web_url = "https://your-username-antioxidant-app.streamlit.app"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(web_url)
qr.make(fit=True)

img = qr.make_image(fill_color="#4A403A", back_color="#FDFBF7")
img.save("스마트폰실행_헬스케어_QR.png")

print(
    "🎉 성공! 스마트폰으로 찍으면 앱이 진짜 터치로 구동되는 '스마트폰실행_헬스케어_QR.png'가 완성되었습니다."
)