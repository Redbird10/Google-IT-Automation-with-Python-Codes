#!/usr/bin/env python3
import shutil, psutil
import socket
import emails, os
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."


if psutil.cpu_percent(1)>80:
  #if arg(1) not supplied, the first run of psutil.cpu_percent() results 100 due to former commands
  subject = "Error - CPU usage is over 80%"
  message = emails.generate_email(sender, receiver, subject, body, 0)
  emails.send_email(message)


if psutil.disk_usage('/')[3]>80:
  subject = "Error - Available disk space is less than 20%"
  message = emails.generate_email(sender, receiver, subject, body, 0)
  emails.send_email(message)


if psutil.virtual_memory()[1]<524288000:
  #500MB=524,288,000Byte
  subject = "Error - Available memory is less than 500MB"
  message = emails.generate_email(sender, receiver, subject, body, 0)
  emails.send_email(message)


if socket.gethostbyname('localhost') != "127.0.0.1":
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  message = emails.generate_email(sender, receiver, subject, body, 0)
  emails.send_email(message)
