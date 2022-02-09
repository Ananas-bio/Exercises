# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:41:42 2022

@author: Patricia

Matthew Funcke Skillshare class
Python Mini-Projects - a Maths Quiz Game
"""
LB = int(input("Give a lower Bound value: "))
UB = int(input("Give an upper bound value (has to be bigger than lower bound): "))
if LB > UB:
    raise Exception("Lower Bound bigger than Upper Bound")
    
def calculateAnswer(lhs, rhs, operator):
    if(operator == "-"):
        return lhs - rhs
    if(operator == "+"):
        return lhs + rhs
    if(operator == "*"):
        return lhs * rhs
    if(operator == "/"):
        return lhs / rhs
    if(operator == "**"):
        return lhs**rhs
       
    raise  Exception("Unknown Operator")

from random import randint 
def generateQ(LB, UB):
    """generates the questions using numbers within an estabilished numbers"""
    lhs = randint(LB, UB)
    rhs = randint(LB, UB)
    ops = ["/","*","-","+","**"]
    opsindex = randint(0,len(ops)-1)
    operator =ops[opsindex]
    while (rhs == 0 and operator =="/"): #prevents division by 0 answers
        rhs = randint(LB,UB)
    return lhs, rhs, operator

def isAccurateEnough(givenAns, correctAns, tolerance = 0.1):
    difference = abs(float(givenAns)-float(correctAns))
    return difference <= tolerance

def numgame():
    numberQ = int(input("How many questions do you want? "))
    c = 0
    countC = 0
    while c < numberQ:
        
        question = generateQ(LB, UB)
        correctAnswer = calculateAnswer(question[0], question[1], question[2])
        playerAnswer = input("{0} {2} {1} = ".format(question[0], question[1], question[2]))
        if playerAnswer == "QUIT":
            break
        c += 1
        if isAccurateEnough(playerAnswer, correctAnswer):
            print("Correct!")
            countC += 1
        else:
            print("Wrong. Correct answer = " + str(correctAnswer))
    print("Here's how many correct answers you had: {0} of {1}".format(countC, c))
    
numgame()