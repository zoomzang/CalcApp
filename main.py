import sys

exinput = "( ( a b c ) d e f ) ( ( g h i ) j k )"
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

inputStack = exinput.split(' ')
inPos = 0
inLen = inputStack(len)
