from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage					
from email.mime.text import MIMEText
import smtplib
#for hidden password input
import getpass

#create message instance
msg=MIMEMultipart()

#sender's password
password = str(getpass.getpass())

msg['From']="junechatbot@gmail.com"
inn = input("Enter receiver's email id:  ")
msg['To'] = str(inn)
sub = input("Subject: ")
msg['Subject'] = str(sub)

#sending text message
message = str(input("Enter the message: "))
msg.attach(MIMEText(message,'plain'))


#sending stored image 	
with open("my.jpg", 'rb') as fp:
	img = MIMEImage(fp.read())
	msg.attach(img)
			
server = smtplib.SMTP('smtp.gmail.com: 587')
#start the mail sending service TLS
server.starttls()

#logging in gmail
server.login(msg['From'], password)

#sending email
server.sendmail(msg['From'], msg['To'],msg.as_string())

print("Your message has been sent!")

server.quit()
