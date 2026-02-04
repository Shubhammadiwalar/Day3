#message = "Hello, World!"
#print(message.strip())
#print(message.upper())
#print(message.replace("World", "Python"))

text = "  python programming  "
print(text[::-1])
print(text[:6])
print(text[7:])
print(text[0::3])

text = "python programming is high level language"
print(text.split())
b=text.split()
for i in b:
    print(i[::-1])