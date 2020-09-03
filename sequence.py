# Algorithm:
# input a number as the length of the sequence
# loop from 1 to number
# if first is 1, current is 1
# if second is 2, current is 2
# if third is 3, current is 3
# else current is the addition of first second and third
# and first is second, second third and third is current
# print current 
n = int(input("Enter the length of the sequence: ")) # Do not change this line
for i in range(1, n+1):
    if i == 1:
        first = i
        current = first
    elif i == 2: 
        second = i
        current = second
    elif i == 3:
        third = i
        current = third
    else:
        current = first + second + third
        first = second
        second = third
        third = current
    print(current)
