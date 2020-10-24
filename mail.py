import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Global configuration
FROM_ADDRESS = "<PUT THE FROM ADDRESS HERE>"
GOOGLE_EMAIL = "<PUT YOUR GOOGLE SIGN-IN EMAIL HERE>"
GOOGLE_PASSWORD = "<PUT YOUR GOOGLE PASSWORD HERE>"
SEND_TO_SELF = False # If True, a copy of the email will be sent to yourself



# Message configuration
emailRecipient = "<RECIPIENT>"
emailSubject = "<SUBJECT>"
emailBody = \
	"""
	PUT EMAIL BODY HERE
	"""




def sendEmail(message, email, subject):
	"""
	Send an email to a specified address using the global configuration
	parameters.

	:param message: The message to be sent to the recipient
	:param email: The email address the message should be sent to
	:param subject: The subject-line of the email
	:return: None
	"""


	print(f"To: {email}")
	print(f"From: {FROM_ADDRESS}")
	print(f"Subject: {subject}")

	# Setup email header
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = FROM_ADDRESS
	msg['To'] = email

	# Create email
	text = MIMEText(message)
	msg.attach(text)

	# Setup SMTP
	s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	s.login(GOOGLE_EMAIL, GOOGLE_PASSWORD)

	# Send email
	s.sendmail(FROM_ADDRESS, [email] + ["gavin@gavinmccabe.com"] if
	SEND_TO_SELF else [email], msg.as_string())
	s.quit()

	print(f"Email sent to {email}")

if __name__ == "__main__":
	sendEmail(emailBody, emailRecipient, emailSubject)