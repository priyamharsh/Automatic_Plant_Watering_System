def send_mail():
	import smtplib

	gmail_user = 'kumarshubham19019019@gmail.com'
	gmail_password = 'open my account'

	sent_from = gmail_user
	to = ['20233@iiitu.ac.in']
	subject = 'Watering of Plants'
	body = 'Your plants have been watered!'

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	try:
	    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    smtp_server.ehlo()
	    smtp_server.login(gmail_user, gmail_password)
	    smtp_server.sendmail(sent_from, to, email_text)
	    smtp_server.close()
	    print ("Email sent successfully!")
	except Exception as ex:
	    print ("Something went wrong….",ex)