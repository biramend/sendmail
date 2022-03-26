import smtplib
import email_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email_destinataire, object, message):
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = object
    multipart_message["From"] = email_config.config_email
    multipart_message["To"] = email_destinataire
    multipart_message.attach(MIMEText(message, "plain"))
    serveur_mail = smtplib.SMTP(email_config.config_server, email_config.config_server_port)
    serveur_mail.starttls()
    serveur_mail.login(email_config.config_email,  email_config.config_password)
    serveur_mail.sendmail(email_config.config_email, email_destinataire, multipart_message.as_string())
    print(f"Message envoyé à {email_destinataire} avec succès")
    serveur_mail.quit()


destinataire = input("A ")
objet = input("Objet ")
content_message = input("Le corps du message")
if destinataire.__contains__("@gmail.com") and content_message != "":
    send_mail(destinataire, objet, content_message)
else:
    print("Destinataire invalide")
