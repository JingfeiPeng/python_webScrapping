import smtplib
from credentials import gmailMailPassword


def send_mail(subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("pengjefferbms@gmail.com", gmailMailPassword)

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "pengjefferbms@gmail.com",
        "jf2peng@edu.uwaterloo.ca",
        msg
    )
    print("Email sent")
    server.quit()