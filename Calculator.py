def IsNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def IsOperator(s):
    if s == "+" or s == "-" or s == "/" or s == "*" or s == "**" :
        return True
    else:
        return False

        



while True:

    Error = False

    Operation = input ("What is the mathmatical operation you are performing? : ")

    if not IsOperator (Operation):
        print ("That isn't an operator you moron. Go back to kindergarten or try again. >:P ")
    else:
        Number_1 = (input ("What is your first number? : "))
        if not IsNumber (Number_1):
            print ("That isn't a number you moron. Go back to kindergarten or try again. >:P ")
        else:
            Number_2 = (input ("What is your second number? : "))
            
            if not IsNumber (Number_2):
                print ("That isn't a number you moron. Go back to kindergarten or try again. >:P ")
            else:


                Number_2 = float(Number_2)
                Number_1 = float(Number_1)

                if Operation == "+" : 
                    Solution = Number_1 + Number_2

                elif Operation == "-" :
                    Solution = Number_1 - Number_2

                elif Operation == "*" :
                    Solution = Number_1 * Number_2
                
                elif Operation == "**" :
                    Solution = Number_1 ** Number_2

                elif Operation == "/" :
                        if Number_2 == 0:
                            print ("You can't divide by 0, silly.")
                            Error = True
                        else:
                            Solution = Number_1 / Number_2
                if not Error:
                    Message = str (Number_1) + " " + Operation + " " + str (Number_2) + " = " + str (Solution)

                    print (Message)

"""Something else creative"""