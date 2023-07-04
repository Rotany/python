with open('./text.txt','r+') as file:
    for line in file:
        print(line)
    file.write('Family very funny\n')
    file.write('Papa gordo\n')
    file.write('we will go to the beach on friday\n')
