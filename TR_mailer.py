# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 01:11:03 2020

@author: shrey.arora
"""

import pandas as pd
import psycopg2
import os
import numpy as np
from datetime import datetime
from datetime import timedelta
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import smtplib

recipient = 'shrey.arora@happay.in'

msg = MIMEMultipart('mixed')
msg['Subject'] = 'Ready to boost your brand to new heights? 💪'
msg['From'] = 'shreyarora150@gmail.com'
msg['To'] = recipient
msg_body = MIMEMultipart('alternative')

BODY_HTML = '''<html><body>    
           <p> <strong  style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;"> We have got something for you! </strong> </p> 
           <a href = "https://thetaperecorder.in/" > <img src="https://i.ibb.co/khC91fB/Emailer-1.png" ></a>
           <p><strong> Stalk us at : </strong></p>
           <br>
           <div class="icon-bar">
          
           <a href="https://www.facebook.com/pg/thetaperecorder.in" > <img src ="https://68ef2f69c7787d4078ac-7864ae55ba174c40683f10ab811d9167.ssl.cf1.rackcdn.com/facebook-icon_32x32.png"> </a>
           <a href="https://www.instagram.com/thetaperecorder.in/" > <img src ="https://68ef2f69c7787d4078ac-7864ae55ba174c40683f10ab811d9167.ssl.cf1.rackcdn.com/instagram-icon_32x32.png"> </a>
           <a href="https://twitter.com/TapeRecorderIn" > <img src ="https://68ef2f69c7787d4078ac-7864ae55ba174c40683f10ab811d9167.ssl.cf1.rackcdn.com/twitter-icon_32x32.png"> </a>
           <a href="https://www.linkedin.com/company/tape-recorder" > <img src ="https://68ef2f69c7787d4078ac-7864ae55ba174c40683f10ab811d9167.ssl.cf1.rackcdn.com/linkedin-icon_32x32.png"> </a>
           
          
          </div>
          
          
          </body></html>'''       
      

CHARSET = "UTF-8"
##msg_body = MIMEMultipart('alternative')  
# Encode the text and HTML content and set the character encoding. This step is
# necessary if you're sending a message with characters outside the ASCII range.
htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
# Add the text and HTML parts to the child container.
# Define the attachment part and encode it using MIMEApplication.
att = open('Tape Recoder - Pitch Deck.pdf', 'rb')

#att = MIMEApplication(open('Tape Recoder - Pitch Deck.pdf', 'rb').read())

msg.attach(htmlpart)
    
# Add the attachment to the parent container.
#msg.attach(att)


payload = MIMEBase('application', 'octate-stream')
payload.set_payload(att.read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Disposition', "attachment; filename= Tape Recoder - Pitch Deck.pdf " ) 
 
msg.attach(payload)



server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

server.login('shreyarora150@gmail.com','jnavasruptfserhj')
server.sendmail('shreyarora150@gmail.com', 'shrey.arora@happay.in', msg.as_string())
server.close()


