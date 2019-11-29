total = 0

file = open('name.txt', 'w')
name = input('Please enter your name')
file.write(name)
file.close()


file = open('name.txt', 'r')
name = file.read().strip()
file.close()
print("Your name is", name)

file = open('numbers.txt', 'r')
for x in range(2):
    lines = int(file.readline())
    total += lines
print(total)

file = open('numbers.txt', 'r')
for x in file:
    lines = int(x)
    total += lines
print(total)