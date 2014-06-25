#!/usr/bin/python
import smtplib

fromaddr = 'sajin.geo@gmail.com'
toaddrs  = 'trigger@ifttt.com'
#toaddrs = 'coolsajin@gmail.com'

msg = """From: Sajin George<sajin.geo@gmail.com>
To: trigger <trigger@ifttt.com>
Subject:#light

#light
"""

# Credentials (if needed)
username = 'sajin.geo@gmail.com'
password = '******'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
