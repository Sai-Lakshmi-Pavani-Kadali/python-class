import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


SMTP_SERVER ="smtp.gamil.com"
SMTP_PORT = 586
SENDER_EMAIL = "kadalipavani61@gmail.com"
SENDER_PASSWORD = "vqbt puwt tzmq yuqq"

def send_email(to_email, subject,body,attachment=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))


        if attachment:
            for file_path in attachment:
                if os.path.exists(file_path):
                    with open(file_path,"rb")as f:
                        mine_base = MIMEBase("application","octet-stream")
                        mine_base.set_payload(f.read())
                        encoders.encode_base64(mine_base)
                        mine_base.add_header(
                            "Conent-Disposition",
                            f"attachment; filename={os.path.basename}"
                                                                            )

