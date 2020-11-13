


levelOne = 60/11
levelTwo = 60/16
levelThree = 60/18
levelFour = 60/22
levelFive = 60/30

timeStartInput = (input("What time did you start?  Use military time."))

lengthOfTime = len(timeStartInput)

if lengthOfTime == 5:
    timeStartHour = int(timeStartInput[0]+timeStartInput[1])
    timeStartMinutes = int(timeStartInput[3]+timeStartInput[4])/60
elif lengthOfTime == 4:
    timeStartHour = int(timeStartInput[0])
    timeStartMinutes = int(timeStartInput[2]+timeStartInput[3])/60
else:
    print("Error.")
    quit()




timeStart = timeStartHour + timeStartMinutes

print(timeStart)

timeOwed = 0
timePaid = 0

while True:
    currentTimeInput = (input("What time is it?"))
    lengthOfTime = len(currentTimeInput)
    currentTimeLength = len(currentTimeInput)

    checkFlag = True
    if lengthOfTime == 0:
        checkFlag = False
    elif lengthOfTime == 5:
        currentTimeHour = int(currentTimeInput[0]+currentTimeInput[1])
        currentTimeMinutes = int(currentTimeInput[3]+currentTimeInput[4])/60
    elif lengthOfTime == 4:
        currentTimeHour = int(currentTimeInput[0])
        currentTimeMinutes = int(currentTimeInput[2]+currentTimeInput[3])/60
    else:
        print("Error.")
        quit()

    if checkFlag == True:
        currentTime = currentTimeHour + currentTimeMinutes


    orderDone = input("What level did you finish?")

    if orderDone == "1":
        timePaid += 60/11
    elif orderDone == "2":
        timePaid += 60/16
    elif orderDone == "3":
        timePaid += 60/18
    elif orderDone == "4":
        timePaid += 60/22
    elif orderDone == "5":
        timePaid += 60/30

    
    
    timeOwed = (currentTime - timeStart)*60
    print("You owe "+ str(timeOwed)+ "minutes in total.")
    print("You've paid back "+ str(timePaid))
    
    
