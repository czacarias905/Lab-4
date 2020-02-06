#this asks users the current time and how long do they want to wait
currentTimeStr = input("What is the current time (in hours 0-23)?")
  
#list of variable
currentTimeInt = int(currentTimeStr)

if (currentTimeInt>23)or (currentTimeInt<0):
    print("ERROR")
else:
    print(currentTimeStr)

    waitTimeStr = input("How many hours do you want to wait?")

    waitTimeInt = int(waitTimeStr)

    finalTimeInt = currentTimeInt + waitTimeInt %24
    print(finalTimeInt)
