# Question 1
name = input("Enter your name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open('name.txt', 'r')
name_from_file = in_file.readline().strip()
print(f"Hi {name_from_file}!")
in_file.close()