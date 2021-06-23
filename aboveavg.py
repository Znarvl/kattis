
c = int(input())
j = 0
while j < c:
    tot = 0
    numOfStudents = 0
    aboveavg = 0
    string = input().split()
    numOfStudents = int(string[0])
    for i in range(1, numOfStudents+1):
        tot += int(string[i])
    average = tot / numOfStudents

    for i in range(1, numOfStudents + 1):
        if int(string[i]) > average:
            aboveavg += 1
    
    value = (float(aboveavg) / float(numOfStudents)) * float(100)
    decimal = "{:.3f}".format(value) + '%'
    print(decimal)
    j+=1

