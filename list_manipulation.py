# -*- coding: utf-8 -*-
"""

johnwoates
CPSC 223P-01
Thu Jan 28, 2021
joates@fullerton.edu

"""

fruits = ["grape", "mango", "nectarine", "pineapple", "banana", 
          "apple", "orange", "pear", "strawberry", "avocado"]

vegetables = ["zucchini", "asparagus", "kale", "spinach", "broccoli",
              "celery", "beets", "bok choy", "brussels sprouts", "arugula"]

newList = fruits + vegetables
print("There are",len(newList),"elements in the combined list")
newList.sort()
for food in newList:
  if food.startswith(("a","b","c","d","e","f","g","h","i","j","k","l","m")):
    print(food)
reverseList=newList[::-1]
print(reverseList)
