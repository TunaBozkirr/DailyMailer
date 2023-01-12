# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:20:07 2023

@author: suley
"""

from smtplib import SMTP
import time
from bs4 import BeautifulSoup #veri işleme
import requests # veri çekme
from selenium import webdriver
import re

r=requests.get("https://www.osevio.com/sayfa/sevgiliye-mesajlar")
soup=BeautifulSoup(r.content, "lxml", from_encoding='UTF-8') #or html.parser
results = soup.find("div", attrs={"class": "col-lg-12 col-12"}).text
results = str(results[1210:])
results=results.split('.')   
list=[]
for index,i in enumerate(results):
   subject=".."
   message=i+".."
   content="subject: {0} {1}".format(subject,message)
   sender="tunabozkir@gmail.com"
   mail=SMTP("smtp.gmail.com",587) 
   mail.ehlo() #connecting server
   mail.starttls() #crypto
   mail.login("tunabozkir@gmail.com","password")
   mail.sendmail(sender,sender ,content.encode("utf-8"))
   time.sleep(60)
   


