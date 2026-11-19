data=[16,25,39,27,12,8,45,43]
for i in range(len(data)):
    print('%3d' %data[i],end='')
print()

for i in range(len(data)-1,0,-1):
    for j in range(i)：
     if data[ j] ＞data[ j+ l] ：
        data[j+1],data[j]=data[j],data[j+1]
        
        
        print