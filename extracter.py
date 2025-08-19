import os
import re
import email
import csv
from datetime import time
from bs4 import BeautifulSoup
import schedule
import parser

eml_dir = r'C:/Melanie/schedule-builder-emails'

csv_file = "emails1.csv"

email_data = []

for filename in os.listdir(eml_dir):
    if filename.endswith(".eml"):
        with open(os.path.join(eml_dir, filename), "r", encoding="utf-8") as eml_file:
            msg = email.message_from_file(eml_file)

            date = msg["Date"]

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        body += part.get_payload()
                    elif content_type == "text/html":
                        body += part.get_payload(decode=True).decode("utf-8", errors='ignore')

            else:
                body = msg.get_payload(decode=True).decode("utf-8")
            
            soup = BeautifulSoup(body, "html.parser")
            text_body = soup.get_text()

            res = re.findall(r'\S+', text_body)
            firstname = res[0]
            lastname = res[1]

            times = parser.find_times(text_body)
            #print(times)

            free = parser.available(times)
            #print(free)


            email_data.append([firstname, lastname, text_body, date])


# with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(["First Name", "Last Name", "Email Body (Text)", "Date & Time"])
#     csv_writer.writerows(email_data)

