import sys
from collections import deque

exinput = "( ( a b c ) d e f ) ( ( g h i ) j k )"
accepted_func = {"sin", "cos", "tan", "cot", "ln", "log10"}
accepted_op = {""}
#take in string, return true if string token is readable to a number.
def isNum(testingString):
    try:
        result = float(testingString)
        #print("was a valid number: " + testingString)
        return True
    except:
        print("not a valid number" + testingString)
        result = testingString
        return False
    r#eturn result
#return the appropriate decorated class if it is a function, otherwise return null
def isFunc(token):

    return 
def isOp(token):

    return
#make order the text in the order it should be executed: abc ghi def jk

#python decorators can pass equations very easily
#   maybe use cases for this
#operator prescedet Associativity
#  ^        4	    Right
#  ×        3	    Left
#  ÷        3	    Left
#  +        2	    Left
#  −        2	    Left
# ( or )    none    when ) is input, pop until (

#I will be implementing the shunting-yard algorithm as found on wikipedia

#TODO (implementing wikipedia pseudocode):
#add dictionary of operator-precedence-associativity
#add operator stack  stack = deque() is a good option--constant time
#implement the wikipedia pseudocode
#       as needed, add enumerators and decorated python functions
#celebrate as you only now need to build a gui
isNum("345")
isNum("apples")
isNum("-34.6")
inputStack = exinput.split(' ')
inPos = 0
inLen = len(inputStack)
opStack = deque()
opStack.append("a")
opStack.append("b")
opStack.append("c")

peek = opStack[0]
outputqueue = list()

for x in range(3):
    print(opStack.pop())


while(inPos < inLen):
    inPos+= 1 #placeholder so the code compiles.
    token = inputStack[inPos]
    if(isNum(token)):
        outputqueue.append(token)
    elif(isFunc(token)):
        opStack.append(token)
    elif(isOp(token)):








#you got this. just implement the shunting-yard algo, make notes and then find ways to calc. add to process flow later vs now. you got this!