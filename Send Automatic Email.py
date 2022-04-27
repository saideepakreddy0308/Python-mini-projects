import os
import random
import smtplib

def automatic_email():
    user = input("Enter your name : ")
    email = input("Enter your email : ")
    message = (f"Dear {user}, Welcome ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail"," Your Password")
    s.sendmail('&&&&&&&&&',email,message)
    print('Email sent successfully')

automatic_email()