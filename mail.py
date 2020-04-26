# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 09:11:10 2020

@author: KARTHIK
"""
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("examplefrom@gmail.com", "karthiktc@123")
server.sendmail("examplefrom@gmail.com", "exampleTo@gmail.com","I love you")
server.quit()

