numbers = [3, 5, 7, 5, 8, 1]
numbers2 = []
for number in numbers:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)