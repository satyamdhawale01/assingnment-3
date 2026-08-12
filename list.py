list=[5,4,6,1,3,2]
n=len(list)

for i in range (n):
   for j in range (0,n-i-1):
      if list [j]> list[j+1]:
       list[j],list[j+1]=list[j+1],list[j]

print("bubble sort",list)


#selected sort
for i in range(n):
     min_index = i

     for j in range (i+1,n):
        if list[j]< list[min_index]:
           min_index=j

    list [i],list[min_index]=list[min_index],list[i]

print("selection sort",list)       
