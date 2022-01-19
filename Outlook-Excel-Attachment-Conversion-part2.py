# This is an improvement on my previous code. This version takes data from the email body and includes it in the output.

import win32com.client
import pandas as pd
import html2text
import re

# Create an object for outlook email
outlook = win32com.client.Dispatch('outlook.application').GetNamespace("MAPI")

# Access inbox, get all messages, select first message
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
message = messages.GetFirst()

# Find correct email based on email title content and sender
for message in messages:
   if "PRE ALERT NOTIFY" in message.Subject and message.SenderEmailAddress == customer@client.com:
      break
   message = messages.GetNext()

# Download attachment to specified location
attachments = message.Attachments
x = 1
for attachment in attachments:
   attachment = attachments.Item(x)
   attachment_name = str(attachment)
   attachment.SaveASFile('C:\outlook-downloads'+ '\\' + attachment_name)
   x = x+1

# Obtain tracking numbers from email body
body_content_html = message.HTMLBody
body_content = html2text.html2text(body_content_html)
body_content_lst = body_content.split("|")

L = []
for item in body_content_lst:
   new_item = re.sub("[^0-9]", "", item)
   L.append(new_item)

case1 = L[17]
tracking1 = L[20]
PO_number = L[16]

export_name = "PRE ALERT NOTIFY " + PO_number

# Create dataframe from Excel data
Client_pre_alert_file_1 = pd.read_excel(
    'C:\outlook-downloads' + '\\' + attachment_name)

# Create output dataframe
Client_pre_alert_file_1.insert(0,'Customer','Client_1')
Client_pre_alert_file_1['Case'] = Client_pre_alert_file_1.iat[0, 5]
Client_pre_alert_file_1['Tracking'] = tracking1
Client_pre_alert_file_1['SKU'] = '1234 5678 9'
Client_pre_alert_file_1['Atte'] = 'Adam Smith'
Client_pre_alert_file_1['Address'] = '1234 Main St, CA 92101'
Client_pre_alert_file_1['email'] = 'Adam.Smith@Client.com'

# Save output dataframe as excel file
Client_pre_alert_file_1.to_excel('C:\outlook-output'+ '\\' + export_name +'.xls', index = False)
