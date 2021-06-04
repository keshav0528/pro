sum=0
while(True):
    userinput=input("enter the price  or press q for quit\n")
     
    if (userinput!='q'):
        sum=sum + int(userinput)
        print(f"order total so far {sum}  ")
    else:
        print(f"your total bill {sum},thanks you for coming ")
        break
