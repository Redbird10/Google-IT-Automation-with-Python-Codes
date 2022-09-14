#!/usr/bin/env python3
import os
import datetime
import reports
import emails
#2 Self-made modules


attachment="/tmp/processed.pdf"
date = datetime.datetime.now().strftime("%B %d,%Y")
title=f"Processed Update on {date}"


path = "./supplier-data/descriptions/"
files = os.listdir(path)
paragraph=""
for file in files:
  with open(path+str(file)) as f:
    content=f.read().splitlines()
    paragraph=paragraph+"name: "+content[0]+"<br/>"+"weight: "+content[1]+"<br/><br/>"


def main():
  reports.generate_report(attachment, title, paragraph)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main()
