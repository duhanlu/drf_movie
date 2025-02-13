import smtplib

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'freyadu99@gmail.com'
EMAIL_HOST_PASSWORD = 'nucpmzunazigixhp'

# Establish connection
try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()  # Upgrade connection to secure
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print("Authentication successful!")
    server.sendmail(
        EMAIL_HOST_USER,
        "hd2367@nyu.edu.com",
        "Subject: Test Email\n\nThis is a test email from Python."
    )
    print("Email sent successfully!")
    server.quit()
except Exception as e:
    print(f"Error: {e}")
