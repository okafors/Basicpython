import smtplib #calling on the SEND MAIL TRANFER PROTOCOL library 
c = False

sender_email= "lisaedd24@gmail.com" #THIS IS EMAIL THAT IS GOING TO BE USED TO SEND THE SUBCRIBE CONFIRMATION
password = "Project1!"
reciever_email = " "
print ("WELCOME TO FOOTBALL FIXTURE PLUS ")



server = smtplib.SMTP('smtp.gmail.com', 587)#CONNETING TO THE GMAIL SERVER 
server.starttls()
def severinfo():
    server.login(sender_email, password)
    print ("You have sucessfully logined into the account")
    server.sendmail(sender_email, reciever_email, msg)
    print("YOUR SUBCRIPTION CONFIRMATION EMAIL HAS BEEN SENT TO", reciever_email)

ans=True
while True:
    print("""
    TO SUBCRIBE PRESS 1
    TO UNSUBCRIBE PRESS 2
    """)
    a = input(str(" TO SUBCRIBE YOUR TO FOOTBALL FIXTURE PLUS ENTER '1' \n  TO UNSUBCRIBE YOUR TO FOOTBALL FIXTURE PLUS ENTER '2' ")) #GIVING THE OPTION TO SUBCRIBE OR UNSUBCRIBE
    ch = ""
    if a=="1":
        print("\n Subscribe")
        ch = "Subscribed"
    elif a=="2":
        print("\n Unsubscribe")
        ch = "Unsubscribed"
    print ("WELCOME, YOU HAVE " + ch + " to FOOTBAL FIXTURES PLUS")
    reciever_email = input(str("PLEASE ENTER YOUR EMAIL: ")) #TO ADD THE EMAIL TO THE SUBSCRIBE OR UNSUBSCRIBE 
    while c != True:
        if "@gmail.com" in reciever_email:
            c = True
        else:
            print('please input an email ending in @gmail.com')
        break
    msg= "YOU HAVE SUBCRIBED TO FOOTBALL FIXTURE PLUS" # THE MESSAGE THAT THE RECIVER WILL RECIEVE 
    if ch== "Unsubscribed":
        msg= "you have been unsubscribed"
        while c != True:
            if "@gmail.com" in reciever_email:
                c = True
            else:
                print('please input an email ending in @gmail.com')
        msg = "YOU HAVE UNSUBCRIBED TO FOOTBALL FIXTURE PLUS" # THE MESSAGE SENT TO THE USER LETTING THEM KNOW THEY HAVE BEEN SUBCRIBED
    severinfo()
