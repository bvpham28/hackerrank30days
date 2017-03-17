#Get number input from user
number = int(input())

#Set result and maximum to 0 so you can increment them

result = 0
max = 0

"""check to see if number is not empty and if it's not empty,
 check to see if the number input can be divided by 2 and the reminder is 1
 if the reminder is 1, add 1 to 'results', however if results greater than max, set max to results"""

while number > 0:
    if number % 2 == 1:
        result += 1
        if result > max:
            max = result
# if result isn't bigger than max, result = 0 and divide the number by 2
    else:
        result = 0

    number //= 2

print(max)