# get number phone input from user and cast the input as an integer
num = int(input())

#create an empty dictionary and call it phone book
phone_book = {}

"""create entries in the dictionary based on the number of input from the value of the num = int(input())
entry will get key/values of the dictionary from the user and store it into the "phone book dictionary"
"""

for i in range(0, num):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = entry

""" Check to see the name from the input of the user is in the dictionary """

for j in range(0, num):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + '=' + str(phone))
    else:
        print("Not found")

