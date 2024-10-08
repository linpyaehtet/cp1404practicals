# Question 1
name = input("Enter your name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open('name.txt', 'r')
name_from_file = in_file.read().strip()
print(f"Hi {name_from_file}!")
in_file.close()

# Question 3
with open('numbers.txt', 'r') as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
    print(number_1 + number_2)


# Question 4
total = 0
with open('numbers.txt', 'r') as in_file:
    for number in in_file:
        total += int(number)
    print(total)