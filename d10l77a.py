import art
def add(n1,n2):
    return n1+n2

#TODO: Write out the other 3 functions - subtract, multiply and divide
def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

# print(div(4,2))

#TODO: Add these functions into a dictionary as the values. Keys = "+", "-", "*", "/"
dictionary_op = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

#Todo : use the dictionary operations to perform calculations. Multiplu 4*8 using the dictionary.
def calculator():
    print(art.logo)
    newnr=True
    a=float(input("what is the first number"))
    while newnr:
        for sym in dictionary_op:
            print(sym)
        op=input("choose the operations")
        b=float(input("what is second number"))
        newn=dictionary_op[op](a,b)
        print(newn)
        choice=input('type "y" for continue with this output or type "n" for start with new input ')
        if choice=="y":
            a=newn
        else:
            newnr==False
            calculator()

calculator()