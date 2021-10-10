from django.shortcuts import render
from .form import *


import smtplib, ssl
import datetime as dt
import time

from apscheduler.schedulers.blocking import BlockingScheduler

def EmailSh(request):
    if request.method =='POST':
        fm = EmailSender(request.POST)
        if fm.is_valid():
            receiver_email= fm.cleaned_data['receiver_email']
            SUBJECT= fm.cleaned_data['SUBJECT']
            TEXT= fm.cleaned_data['TEXT']
            day= fm.cleaned_data['date']
            hr= fm.cleaned_data['hour']
            min= fm.cleaned_data['minute']
            sender_email = "ahmadsayyed66@gmail.com"
            password = "oxsujuvkrjswbszs" # genrate passord from gmail app password genrator
            port = 587 
            smtp_server = "smtp.gmail.com" 
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            context = ssl.create_default_context()
            def email_sender():
                with smtplib.SMTP(smtp_server, port) as email:
                    email.starttls(context=context)
                    email.login(sender_email, password)
                    email.sendmail(sender_email, receiver_email, message)
                    print('mail send')
            scheduler = BlockingScheduler()
            scheduler.add_job(email_sender, 'cron', day = day, hour=hr, minute=min)
            scheduler.start()
            
            
    

   
    else:
        fm = EmailSender()
    return render(request,'mail.html', {'form':fm},)
    
