import threading
import time
def walk_dog():
    time.sleep(3)
    print("you finish walking street")
def take_out_trash():
    time.sleep(5)
    print("take out the trash") 
def get_mail(name):
    time.sleep(1)
    print(f"{name}get an email")   
function1=threading.Thread(target=walk_dog)
function1.start()

function2=threading.Thread(target=take_out_trash  )
function2.start()

function3=threading.Thread(target=get_mail, args=("ayesha ",))
function3.start()

function1.join()
function2.join()
function3.join()