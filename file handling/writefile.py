# writing a string to a file
'''with open('description.txt', 'w') as file:
    file.write("Iam Bhargavi")'''
# writing multiple lines to a file
'''lines = ["First line\n", "Second line\n", "Third line\n"]

with open('description.txt', 'w') as file:
    file.writelines(lines)'''
# appending to a file
with open('description.txt','a') as file:
    file.write("Appending this line.\n")
