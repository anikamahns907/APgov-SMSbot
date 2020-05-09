
f = open("question.txt", "r")
wrong = True
for line in f:
    line = line.split('\n')[0]
    print(line)


    while(wrong):
        response = input("Copy this text: ")
        print(response, line)
        if (str(response) == str(line)):
            print('success')
            break
        else:
            print('fail')
           



