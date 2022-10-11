import os, sys

start_WebCAM = "sudo service motion start"
stop_WebCAM = "sudo service motion stop"
restart_WebCAM = "sudo service motion restart"

os.system(start_WebCAM)

while True:
    webcam = int(input("If you want stop the streaming : 1, Restart is : 2 : "))
    if webcam == 1 :
        os.system(stop_WebCAM)
        print(stop_WebCAM)

    elif webcam == 2 :
        os.system(restart_WebCAM)
        print(restart_WebCAM)

    else :
        os.system(stop_WebCAM)
        print(stop_WebCAM)
        exit()