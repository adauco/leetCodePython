import smtplib

smtp_o = smtplib.SMTP('smtp.google.com', 587)

smtp_o.ehlo()
print("HOLA")
