for x in xrange(1, 21):
    print(x)

numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)

mult_numbers = []
for value in range(3, 31):
    mult_number = value * 3
    mult_numbers.append(mult_number)
for mult_number in mult_numbers:
    print(mult_number)

print("---------------------")

third_power_nums = []
for num in range(1, 11):
    third_power_num = num ** 3
    third_power_nums.append(third_power_num)
for third_power_num in third_power_nums:
    print(third_power_num)

print("---------------------")

cubes = [num ** 3 for num in range(1, 11)]
print(cubes[0:3])
print(cubes[4:7])
print(cubes[-3:])

print("---------------------")

pizzas = ['bbq chken', 'pesto chicken', 'italian']

friend_pizzas = pizzas[:]

pizzas.append("vage pizza")
friend_pizzas.append("pinapple pizza")
print("my favorite pizza:")
for my_pizza in pizzas:
    print(my_pizza)

print("my friens's favorite pizza:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

    # for number in numbers:
    #	print (number)