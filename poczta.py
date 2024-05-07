import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyotp

# Twój sekretny klucz aplikacji uwierzytelniającej
secret_key = "klucz"  # do wygenerowania

# Twój identyfikator konta Google
email_address = "twoj_mail@gmail.com" # do wprowadzenia

# Inicjalizacja obiektu aplikacji uwierzytelniającej
totp = pyotp.TOTP(secret_key)

try:
    # Połączenie z serwerem SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # Tworzenie wiadomości e-mail
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = "@gmail.com"  #mail odbiorcy
        msg['Subject'] = "TeSt"
        body = "Treść wiadomości"
        msg.attach(MIMEText(body, 'plain'))

        # Logowanie z użyciem aplikacji uwierzytelniającej
        app_password = totp.now()
        smtp.login(email_address, app_password)

        # Wysłanie wiadomości
        smtp.send_message(msg)

    print("Wiadomość została wysłana pomyślnie.")
except smtplib.SMTPException as e:
    print("Wystąpił błąd podczas wysyłania wiadomości:", e)
