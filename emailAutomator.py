import smtplib
email = "abc@gmail.com"
password = 1234

def automateMessage(email,to_email,message):
    if email.contains("@gmail.com"):
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.starttls()
        gmail.login(email, password)

        # sending email
        gmail.sendmail(email, to_email, message)

        # quit the session
        gmail.quit()

    if email.contains("@outlook.com"):
        outlook = smtplib.SMTP('smtp.outlook.com', 587)
        outlook.starttls()
        outlook.login(email, password)

        # sending email
        outlook.sendmail(email, to_email, message)

        # quit the session
        outlook.quit()

    if email.contains("@apple.com"):
        apple = smtplib.SMTP('smtp.apple.com', 587)
        apple.starttls()
        apple.login(email, password)

        # sending email
        apple.sendmail(email, to_email, message)

        # quit the session
        apple.quit()


