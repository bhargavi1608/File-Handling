# reading the entire file
'''with open('description.txt','r') as file:
    content = file.read()
print(content)'''
# Reading a File Line by Line
'''with open ('description.txt','r') as file:
    for line in file:
        print(line, end='')'''
# Reading all lines into a list
'''with open('description.txt','r') as file:
    lines=file.readlines()
for line in lines:
    print(line,end='')'''
# Using readline()
with open('description.txt','r') as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line,end='')
