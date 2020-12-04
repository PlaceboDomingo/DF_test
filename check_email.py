import email
import imaplib
import ctypes
import getpass

mail = imaplib.IMAP4_SSL('imap.cox.net', 993)
username = raw_input("Login : ")
password = getpass.getpass("Password : ")
mail.login(username,password)
mail.select("INBOX")
def loop():
	mail.select("INBOX")
	n=0
	(retcode,messages)=mail.search(None,'(UNSEEN)')
	if retcode == 'OK':
		for num in messages[0].split():
			n=n+1
		print n 
		typ, data = mail.fetch(num, '(RFC822)')
		for respone_part in data:
			if isinstance (respone_part,tuple):
				original = email.message_from_string(respone_part[1])
			print original['From']
			data = original['Subject']
			print data
			typ, data = mail.store(num, '+FLAGS','\\Seen')

	print n
if __name__ == '__main__':
	try:
		while True:
			loop()
	finally:
		print "Thank you"
?
