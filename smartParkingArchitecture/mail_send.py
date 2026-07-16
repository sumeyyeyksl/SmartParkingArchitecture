import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "YOUR_EMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD"

    subject = "Park Süresi Uyarısı"
    body = "Park süreniz 1 saati geçti. Lütfen aracınızı alınız."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)  # <-- HATA BURADA DÜZELTİLDİ
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("E-posta gönderildi.")
    except Exception as e:
        print(f"E-posta gönderimi başarısız oldu: {str(e)}")

