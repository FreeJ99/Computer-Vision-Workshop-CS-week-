import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
import Dice_Solver_C1
import Dice_Solver_C2
import Dice_Solver_C3
import Dice_Solver_C4
import Dice_Solver_C5
import Dice_Solver_C6

solutions = np.asarray([[9,2,4,10,2,5],
 [9,8,8,10,7,5],
 [9,8,9,8,9,9],
 [9,4,8,8,8,8],
 [9,2,4,10,2,5],
 [9,9,3,5,8,5],
 [8,8,8,8,5,5,5,9,3,3,6,3,3,8,2,2,10,5,11,11,12,7,5,5,5,8,8,8,8,8]])

challenge = int(input("Unesi broj izazova: "))
test = int(input("I broj grupe test primera: "))

if test < 1 or test > 6 or challenge < 1 or challenge >6:
    print("Zar ni broj ne mozes da pogodis? :( ")
    sys.exit()

if challenge == 1:
    for i in range(len(solutions[test-1])):
        img = cv2.imread("Pictures/Challenge_" +str(test) + "/" +  str(i) + ".jpg",cv2.IMREAD_COLOR)
        number = Dice_Solver_C1.my_function(img)
        print(str(i) + "   " + str(number) + "/" + str(solutions[test-1][i]))

elif challenge == 2:
    for i in range(len(solutions[test-1])):
        img = cv2.imread("Pictures/Challenge_" +str(test) + "/" + str(i) + ".jpg",cv2.IMREAD_COLOR)
        number = Dice_Solver_C2.my_function(img)
        print(str(i) + "   " + str(number) + "/" + str(solutions[test-1][i]))

elif challenge == 3:
    for i in range(len(solutions[test-1])):
        img = cv2.imread("Pictures/Challenge_" +str(test) + "/" + str(i) + ".jpg",cv2.IMREAD_COLOR)
        number = Dice_Solver_C3.my_function(img)
        print(str(i) + "   " + str(number) + "/" + str(solutions[test-1][i]))

elif challenge == 4:
    for i in range(len(solutions[test-1])):
        img = cv2.imread("Pictures/Challenge_" +str(test) + "/" + str(i) + ".jpg",cv2.IMREAD_COLOR)
        number = Dice_Solver_C4.my_function(img)
        print(str(i) + "   " + str(number) + "/" + str(solutions[test-1][i]))

elif challenge == 5:
    for i in range(len(solutions[test-1])):
        img = cv2.imread("Pictures/Challenge_" +str(test) + "/" + str(i) + ".jpg",cv2.IMREAD_COLOR)
        number = Dice_Solver_C5.my_function(img)
        print(str(i) + "   " + str(number) + "/" + str(solutions[test-1][i]))

elif challenge == 6:
    for i in range(len(solutions[test-1])):
        img = cv2.imread("Pictures/Challenge_" +str(test) + "/" + str(i) + ".jpg",cv2.IMREAD_COLOR)
        number = Dice_Solver_C6.my_function(img)
        print(str(i) + "   " + str(number) + "/" + str(solutions[test-1][i]))
