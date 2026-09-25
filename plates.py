def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    plate=s
    if len(plate)<2 or len(plate)>6:
        return False       #max 6 characters and min 2.
    elif plate[0].isalpha() is False or plate[1].isalpha() is False:
        return False       #start with 2 letters.
    elif numbers(plate):
        return False       #verify if the numbers are at the end and don't start with 0
    elif plate.isalnum() is False:
        return False       #If there is any periods, spaces, or punctuation (if it's only alphanumeric)
    else:
        return True

def numbers(s):
    for i in range (len(s)):
        if s[i].isdigit():
            if s[i]=="0":  #looking if the first number is 0
                return True

            if s[i:].isdigit() is False:   #looking if all the characters after teh first number are numbers
                return True
            return False
        return False

main()







