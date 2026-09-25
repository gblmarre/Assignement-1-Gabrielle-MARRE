def coke_machine():
    x=int(input("How many coke do you want ? "))
    return coin (x)


def coin(x):
    due=x*50
    i=0
    give=0
    while due>0:
        print("Amount due:",due,"cents")
        give=int(input("Insert a coin:"))
        if give==25 or give==10 or give==5:
            due=due-give
    return bye(due)

def bye(x):
    if x==0:
        print("Thank you! Enjoy your coke(s)!")
    else:
        print("Thank you! Your change:", abs(x),"cents")

coke_machine ()
