# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:20:07 2023

Script to scrape birthday wishes from a website and send them via email.

@author: suley
"""

from smtplib import SMTP
import time
from bs4 import BeautifulSoup  # For data processing
import requests  # For data fetching

# Fetch the content from the website
url = "https://www.southernliving.com/holidays-occasions/birthday/happy-birthday-wishes"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml", from_encoding='UTF-8')

# Extract the relevant content from the website
results = soup.find("div", attrs={"class": "col-lg-12 col-12"}).text
results = str(results[1210:])
results = results.split('.')

# Prepare the email configuration
subject = "Birthday Wishes"
sender_email = "tunabozki..@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "tunabozki..@gmail.com"
smtp_password = "password"

# Loop through the birthday wishes and send them via email
for index, message in enumerate(results):
    # Prepare the email content
    email_content = f"Subject: {subject}\n\n{message}.."
    
    # Connect to the SMTP server
    with SMTP(smtp_server, smtp_port) as mail:
        mail.ehlo()  # Connecting to the server
        mail.starttls()  # Start TLS for secure communication
        mail.login(smtp_username, smtp_password)  # Login to the email account
        mail.sendmail(sender_email, sender_email, email_content.encode("utf-8"))  # Send the email
    
    # Pause for 60 seconds before sending the next email
    time.sleep(60)





