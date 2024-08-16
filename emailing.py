# Não esqueça de configurar na conta do goole gmail:
# Manage you google account > Security > Turn on 2-step verification
# Manage you google account > Security > App passwords > Select app > Other (custom name) > "Webcam3" > Salvar password
# gerado

import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "PASSWORD_GERADO_NO_GMAIL"
SENDER = "EMAIL QUE SERÁ ENVIADO PARA OUTRO(app8flask@gmail.com)"
RECEIVER = "EMAIL QUE IRÁ RECEBER (app8flask@gmail.com)"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email()
