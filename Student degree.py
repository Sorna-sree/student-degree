marks=[]
n=5 #5 subject marks 
count1=0
count2=0
count3=0
count4=0
count5=0
for i in range(0,n):   #Enter the 5 Marks
    marks.append(int(input("enter the marks:")))
for i in range(0,n):
    if(marks[i]>=60):   # score above 60% in all subject   
        count5+=1
    if(marks[i]>=90 or marks[i]>=40):
        if(marks[i]>=90):
            count1+=1
        else:
            count2+=1
    elif(marks[i]>=75 or marks[i]>=50):
        if(marks[i]>=75): 
            count3+=1
        else:
            count4+=1
if(count1==3 and count2==2 or count1==2 and count2==3 or count5==5): 
    print("pass")
elif(count3==3 and count4==2 or count3==2 and count4==3):
    print("pass")
else:
    print("fail")