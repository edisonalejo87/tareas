# text="Mi lenguaje favorito es Python"
# print("Python" in text)

# #slicing
# print(text[0])
# print(len(text))

# size=len(text)
# print(text[size-1])
# print(text[1])

# #print(text[0:0:0])
# print(text[0:11])
# print(text[3:])
# print(text[::-1])

import random
numbers =[1,2,3,4,5]
fruits =["manzana","pera","banana"]
new_list = numbers + fruits
# print(type(numbers))
# print(numbers[0])
# print(numbers[0:3])
# print(numbers[-1])

numbers[0] ="Banana"

# numbers.append("700")
# numbers.insert(3,0)

index = numbers.index(3)
numbers[index] ="change"

print("my arreglo es",numbers)

#remueve del random
numbers.pop()
numbers.remove()

my_random = random.choice(fruits)

print(random.choice(fruits))

# print(numbers)

# print(new_list)











