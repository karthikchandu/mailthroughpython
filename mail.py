# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 09:11:10 2020

@author: KARTHIK
"""
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("dontmailme1999@gmail.com", "karthiktc@123")
server.sendmail("dontmailme1999@gmail.com", "vandukaaru2001@gmail.com","I love you")
server.quit()

