numbers =[12,45,12,13,15,19]
nums={12,45,12,13,15,19}
nums_tuple=12,45,12,13,15,19
marks = {'physics':12, 'chemistry':45, 'math': 56}
# total = sum(numbers)
total = 0

# for i in numbers:
#     # print(i)
#     total = total+i  
# print(total)

# for num in nums:
#     total+=num
# print(total)

# for num in nums_tuple:
#     total += num
# print(total)

# for mark in marks:
#     val = marks[mark]
#     print(mark, val)
#     # print(val)
# print(total)

# for subject,mark in marks.items():
#     print(subject, mark)

for i, num in enumerate(numbers):
        print(i, num) 
