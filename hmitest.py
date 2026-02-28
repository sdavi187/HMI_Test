
def check_string (string_to_check):

    big_size = 99

    if string_to_check.isalpha():
        return ("The string is all letters")
    elif string_to_check.isdigit():
        
       
        string_to_check = int(string_to_check)

        if string_to_check > big_size:
            print ("THe number is big")
        else:
            print("The number is small")

        return ("The string is all numbers")

    else:
        return ("The string is mixed")
    
while (True):
    input_string = input ("Enter a string for evaluation: ")

    if input_string != "":
        print (check_string(input_string, 400, 6))
        break
    else:
        print ("You must enter something.")