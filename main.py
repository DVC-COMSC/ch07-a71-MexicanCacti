
numbers = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
avg = sum/len(numbers)
for i in range(len(numbers)):
    numbers[i] = abs(avg - numbers[i])
    print (f'{numbers[i]:.2f}', end=' ')



# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
