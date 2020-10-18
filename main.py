import sys
from collections import deque

#reference field
#exinput = "( ( 3 + 4 ) * 5 ) + ( ( 5 * 4 ) + 4 )"
#exinput = "4 + 18 / ( 9 - 3 )"
exinput = "sin ( max ( 2 , 3 ) ÷ 3 × 3.1415 )"
accepted_func = {"sin", "cos", "tan", "cot", "ln", "log10"}
accepted_op = {"+","-","*","/", "^"}  
operatorDictionary = {
    "+": {
        "prescedent": 2,
        "associativity": "Left"
    },
    "-": {
        "prescedent": 2,
        "associativity": "Left" 
    },
    "*": {
        "prescedent": 3,
        "associativity": "Left"
    },
    "/": {
        "prescedent": 3,
        "associativity": "Left"
    },
    "^": {
        "prescedent": 4,
        "associativity": "Right"
    }

}
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
    #return result
#return the appropriate decorated class if it is a function, otherwise return null
def isFunc(token):
    return token in accepted_func
def isOp(token):
    try:
        return accepted_op.issuperset(token)
    except:
        return false
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
#implement the wikipediax BRILLIANT pseudocode
#       as needed, add enumerators and decorated python functions
#celebrate as you only now need to build a gui
isNum("345")
isNum("apples")
isNum("-34.6")
inputStack = exinput.split(' ')
inputPos = 0
opStackPos = 0
numTokens = len(inputStack)
opStack = []
outputqueue = list()

print(operatorDictionary["^"]["prescedent"])
while(inputPos < numTokens):
    #placeholder so the code compiles.
    token = inputStack[inputPos]
    if(isNum(token)):
        outputqueue.append(token)
    elif(isFunc(token)):
        opStack.append(token)
    elif(isOp(token)):
        print("hello")
        #while there are operators on the stack with greater presedence, p
        tokenPres = operatorDictionary[token]["prescedent"]
        opStackTop = len(opStack) - 1
        while(opStackTop >=0 and isOp(opStack[opStackTop]) and tokenPres < operatorDictionary[opStack[opStackTop]]["prescedent"]):
            print("loop")
            outputqueue(opStack.pop()) #pop operators from the stack onto the outputqueue
        opStack.append(token)
    elif(token == "("):
        opStack.append(token)
    elif(token ==")"):
        while(opStack[len(opStack)-1] != "("): #note this is an inefficient way to get the top of the stack
            outputqueue.append(opStack.pop())
    inputPos+= 1
while(len(opStack)>0):
    outputqueue.append(opStack.pop())



print("done")
print(outputqueue)


#https://en.wikipedia.org/wiki/Shunting-yard_algorithm
#https://brilliant.org/wiki/shunting-yard-algorithm/

#you got this. 
# just implement the shunting-yard algo, make notes and then find ways to
#  calc. add to process flow later vs now. you got this!
