fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Fruits tuple:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print("First three fruits:", fruits[0:3])

print("Number of fruits:", len(fruits))

print("All fruits:")
for fruit in fruits:
    print(fruit)

if "Mango" in fruits:
    print("Mango is available!")

more_fruits = ("Pineapple", "Cherry")
all_fruits = fruits + more_fruits
print("After adding more fruits:", all_fruits)
