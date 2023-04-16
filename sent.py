import smtplib

# Set up your email account details
sender_email = 'yourmail@gmail.com'
sender_password = 'yourpassword'
receiver_email = 'sender_mail@gmail.com'

# Create the message
message = 'Have a good day'

# Set up the SMTP server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(sender_email, sender_password)
print("Login Successful")

# Send the email
smtp_server.sendmail(sender_email, receiver_email, message)
print("Email Sent")

# Close the SMTP server
smtp_server.quit()
