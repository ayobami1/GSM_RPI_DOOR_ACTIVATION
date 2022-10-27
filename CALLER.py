from callerID import*
# import serial
# import os, time , sys
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)

# GPIO.setup(26, GPIO.OUT) # door 1+2 OPEN
# GPIO.setup(21, GPIO.OUT)
# GPIO.setup(20, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)


# relay1 = 21
# delay1 = 10 # pico reboot relay
# delay2 = 30 # ignore calls
# delay3 = .1 # hangup
# ser = serial.Serial( "/dev/ttyUSB0", baudrate=115200, timeout=1)
"WRITE YOUR CODE TO DECODE INCOMING NUMBER, UNCOMMENT AND COMMENT EACH CODE IN THE WHILE TRUE LOOP TO KNOW HOW THEY WORKS"
while True:
    incomingID = '+35799157415' # We assume this is calling Number we put it in Telephone_98, use your code to Decode the Incoming Call
    try:
        """________________CASE1 1_____________________________________
        USE THIS LINE OF CODE TO PRINT OUT ALL THE PHONE BOOK CALLAR ID 
        TO BE SURE YOU KNOW WHAT YOU ARE DOING"""
        # for phoneNumber in CallerID_Dict:
        #     print(f"{phoneNumber} is == {CallerID_Dict[key]}")


        """________________CASE1 2_____________________________________ 
        TO ACCESS EACH OF THE CALLER_ID DURING INCOIMING CALL AT RANDOM
        IF YOU ARE NOT SURE AND TO SAVE YOU STRESS LET THE CODE SEARCH FOR YOU USE 
        THIS LINE OF CODE WE PROVIDE incomingID   """



        for phoneNumber in CallerID_Dict:
            if incomingID == CallerID_Dict[phoneNumber]:

                #"  PUT CODE HERE WHAT YOU WANT IT TO DO AND DELETE THE NEXT TWO LINE OF CODE"
                Caller=CallerID_Dict[phoneNumber]

                print(f"Now i detect the Phone calling me and it is {phoneNumber} The Number IS {Caller}\nI Think it is Mr. Stelios' Number\nSo what do you want me to do !")
        
        """________________CASE1 3_____________________________________
        OR IF YOU PREFER TO CHOOSE ANY CALLER ID FROM THE DICTIONARY SO THAT YOU CAN 
        ATTACHED AN ARGUEMENT TO IT  USE THIS CODE WE PROVIDE incomingID
        """
       
        # for phoneNumber in CallerID_Dict:
        #     if incomingID == CallerID_Dict["Telephone_98"]:
            #"  PUT CODE HERE WHAT YOU WANT IT TO DO AND DELETE THE NEXT TWO LINE OF CODE"
        #         print("It is Correct !!")
        #         break
        #    elif incomingID == CallerID_Dict["Telephone_2"]:
        #     #DO SOMETHING
        #     pass

        #    elif incomingID == CallerID_Dict["Telephone_4"]:
        #     #DO SOMETHING
        #     pass
        
        #    elif incomingID == CallerID_Dict["Telephone_5"]:
        #     #DO SOMETHING
        #     pass
        #    else:

        #       pass

        break # Remove this Break for real project so it kept running and running i put it here for you to test the code is working
    except KeyboardInterrupt as e:
        print(e)
       