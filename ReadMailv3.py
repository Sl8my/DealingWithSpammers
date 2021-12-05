#modules
import imaplib
import email
import re

#credentials
username ="serravalledomenico@hotmail.com"

#generated app password
app_password= "qauxzqzxfcpciytr"

# https://www.systoolsgroup.com/imap/
gmail_host= 'imap-mail.outlook.com'

#set connection
mail = imaplib.IMAP4_SSL(gmail_host)

#login
mail.login(username, app_password)

#select inbox
mail.select("JUNK")

#match = re.findall(r'[\w.+-]+@in.[\w-]+\.eu', email_message["from"])

regex = "info@in.palicuh.eu"

#select specific mails
_, selected_mails = mail.search(None, 'ALL')

#total number of mails from specific user
print("Total Messages from info@in.palicuh.eu:" , len(selected_mails[0].split()))

counter = 0
for num in selected_mails[0].split():
    _, data = mail.fetch(num , '(RFC822)')
    _, bytes_data = data[0]

    #convert the byte data to message
    email_message = email.message_from_bytes(bytes_data)
    print("\n===========================================")
    counter = counter + 1
    print("Num = " + str(counter))

    print("Subject: ",email_message["subject"])
    print("From: ",email_message["from"], file=open("output.txt", "a"))
    print("Date: ",email_message["date"])