import smtplib
from email.message import EmailMessage

# Email content
msg = EmailMessage()
msg['Subject'] = 'Hello from Python'
msg['From'] = 'akhmadkhanovabdulvadud@gmail.com'
msg['To'] = 'akhmadkhanovabdulvadud2@gmail.com'
msg.set_content('This is a test email sent from a Python script!')

# Sending the email
try:
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('your_email@gmail.com', 'your_app_password')
    smtp.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
  print("Error:", e)
