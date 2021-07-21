#INTERNSHIP TASK 
#Name : Sampath Ganesh Kandregula

#TASK 1 IN PYTHON 

"""1. Write a Python program which asks the user to enter a number 'n' and then iterates the integers from 1 to 'n'.
 For multiples of three print "3n" instead of the number and for the multiples of five print "5n". 
 For numbers which are multiples of both three and five print "your-name".
"""

n = int(input("please enter a number"))#input function 
for i in range(1,n):
  if i % 3 == 0 and i % 5 == 0:#if divisible by both 3 and 5 
    print("your-name")
    continue
  elif i % 3 == 0:#if divisible by 3
    print(3*n)
    continue
  elif i % 5 == 0:#if divisible by 5 
    print(5*n)
    continue
  print(i)# if not divisible by both 3 and 5 print the integer


#TASK 2 IN PYTHON 

"""2. Hitting a GET request to the following URL endpoint https://jsonplaceholder.typicode.com/todos/1  gives
{
        "userId": 1,
        "id": 1,
        "title": "aut consectetur in blanditiis deserunt quia sed laboriosam",
        "completed": true
    }
   
    as the response, If we just change the userId parameter(todos/1 or todos/2) in the URL endpoint and hit the GET request again at  https://jsonplaceholder.typicode.com/todos/2 we recieve a different response with the same structure having userId, id, title and completed key value pairs.
   
    Now write a Python program to send GET requests 5 times for 5 different userIds(1,2,3,4&5) and append the title from response to a common list. Finally print the list.
"""

import requests
for i in (1,2,3,4,5):#looping over id's
  url = 'https://jsonplaceholder.typicode.com/todos/' + str(i) # conacetnating the link and the number 
  r  = requests.get(url)
  answers = r.text
  common_list = []
  common_list.append(answers)
  print(common_list)