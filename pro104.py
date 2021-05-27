import csv
import statistics

with open('SOCR-HeightWeight_pro104.csv') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

sum=0
for i in range(0,len(new_data)):
    sum=sum+new_data[i]

def mean():
    mean=sum/len(new_data)
    print(mean)

def median():
    n=len(new_data)
    new_data.sort()
    calc=int(len(new_data)/2)

    if n%2==0:
        median=(new_data[calc]+new_data[(calc)-1])/2
        print(median)

    else:
        num=(len(new_data)-1)/2
        median=new_data[num]
        print(median)

def mode():
    mode=statistics.mode(new_data)
    print(mode)

mean()
median()
mode()
    