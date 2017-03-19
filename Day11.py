arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

#Set the range of the 2D Array
maximum = -9 * 9

#Check for values inside the 2D Array
for i in range(6):
    for j in range(6):
        if j + 2 < 6 and i + 2 < 6:
            #Set your hourglass.
            result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            #find the max
            if result > maximum:
                maximum = result

print(maximum)