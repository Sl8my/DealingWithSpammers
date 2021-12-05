import win32com.client as win32
import math
import time

# my_file = open("output_clean.txt", "r")
# content_list = my_file.readlines()

# print(len(content_list))

with open('output_clean.txt') as f:
    for line in f:
        pass
    last_line = line

print("Sending 300 email to " + line + "...")

for x in range(1, 275):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Subject = 'CANCELLATE LA MIA MAIL'
    print(x)
    mail.To = line
    mail.Body = 'Message body'
    mail.HTMLBody = '<h1>Ne ho abbastanza è stato bello ma ora CANCELLATE LA MIA MAIL PF, BASTA DAI</h1>'
    mail.Send()
    time.sleep(1)

print("Dovrebbe essere ok, controlla posta inviata")

# counter = 0
# for mail in content_list:
#     counter = counter + 1
#     print("Num = " + str(counter))
#     print(mail)
    # mail.To = str(mail)
    # mail.Subject = 'CANCELLATE LA MIA MAIL'
    # mail.Body = 'Message body'
    # mail.HTMLBody = '<h1>Ne ho abbastanza è stato bello ma ora CANCELLATE LA MIA MAIL PF, BASTA DAI</h1>'
    # mail.Send()


# To attach a file to the email (optional):
# attachment  = "Path to the attachment"
# mail.Attachments.Add(attachment)

