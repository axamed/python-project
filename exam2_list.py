import time,os
seconds=30

count=3
pin=1234
pink=int(input("soo geli pin: "))
os.system("cls")

while count>=1:
    if pin==pink:
        print("welcome ")
        break
    else:
        count-=1
        if count==0:
            print(f"waxaa laga xanibay {seconds}")
            for i in range(seconds):
                os.system("cls")
                print(f"waxaa laga xanibay{seconds-i}")
                time.sleep(1)
            seconds*=seconds
            count=2


    pink=int(input(f"fadlan geli pin sax waxaa ku haray {count}: "))
    os.system("cls")