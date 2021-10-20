# The following code downloads an excel file attachment from a specific email in an outlook inbox, then uses that file to create a new excel file based on a new combination of data requirements.

import win32com.client
import pandas as pd
import os
from datetime import datetime, timedelta

# Create an object for outlook
outlook = win32com.client.Dispatch('outlook.application').GetNamespace("MAPI") 

# Create an object to access the inbox, get all messages in inbox, and select first message
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
message = messages.GetFirst()

# Iterate through inbox emails and break when correct email is found based on email title content and email sender
for message in messages:
  if "PRE ALERT NOTICE" in message.Subject and message.SenderEmailAddress == "person@company.com":
    break
  message = messages.GetNext()

# Download attachment to specified location
attachments = message.Attachments
x=1
for attachment in attachments:
  attachment = attachments.Item(x)
  attachment_name = str(attachment)
  attachment.SaveASFile('C:\outlook-downloads'+ '\\' + attachment_name)
  x = x+1

# Create 2 dataframes, one for each sheet in the excel file
Company_pre_alert_file_1 = pd.read_excel('C:\outlook-downloads'+ '\\' + attachment_name)
Company_pre_alert_file_2 = pd.read_excel('C:\outlook-downloads'+ '\\' + attachment_name, sheet_name=1)

# Create output dataframe
Company _pre_alert_file_1.insert(0,'Customer','Company')
Company _pre_alert_file_1['Case'] = Company_pre_alert_file_1.iat[0,5]
Company _pre_alert_file_1['Tracking'] = Company_pre_alert_file_2.iat[2,4]
Company _pre_alert_file_1['SKU'] = 12345 6789 0
Company _pre_alert_file_1['Attention'] = 'Person LastName'
Company _pre_alert_file_1['Address'] = '1234 MAIN ST SAN DIEGO, CA 92122'
Company _pre_alert_file_1['email'] = 'person2@company2.com'

# Save output dataframe as excel file
Company_pre_alert_file_1.to_excel('C:\outlook-output'+ '\\' + attachment_name, index = False)
