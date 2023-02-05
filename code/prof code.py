my_list = []
with open('tabdelimited.txt','r') as file:
    # reading each line    
    for line in file:
        # reading each word        
        word= line.split()
        if word[-1].isdigit():
            my_list.append(word[-1])
        length=len(my_list)
for i in range(0, length-1):
    for j in range(i+1, length):
        if my_list[i]>my_list[j]:
            f=my_list[i]
            my_list[i]=my_list[j]
            my_list[j]=f
print("The last column sorted value is")
for i in my_list:
    print(i)
