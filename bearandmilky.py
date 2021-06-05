#bear and milky cookies
#iterating till the range and taking the no of elements as input.
for i in range(int(input())):
    #takes interger input from the user
    n = int(input())
    #This function helps in getting a multiple inputs from user. It breaks the given input by the specified separator. If a separator is not provided then any white space is a separator.
    l = input().split()
    #another variable with value zero
    c=0
    #executing  from the statement from the input which is stored in variable l.
    for i in l:
        if i=="cookie":
    #executing the statement if it's satisfy then it will increment the value of input and store on the empty disk.
            c+=1
    #this part is executed when above statement is dis-satisfy.
        else:
            c=0
            
        if c==2:
            #break is used for discontinue of the statement.
            break
    #if the condition is valid then it will print yes otherwise else part will execute.
    if c==0:
        print("YES")
    else: 
        print("NO") 