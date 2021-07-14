import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv('file/Salary_Data.csv')
list1=list(data['YearsExperience'])
list2 = list(data['Salary'])
n = len(list1)


sx = 0
sx2 = 0
sx3 = 0
sx4 = 0
sy = 0
sxy = 0
sx2y = 0
for i in range(n):
    sx = sx + list1[i]
    sx2 = sx2 + (list1[i])**2
    sy = sy + list2[i]
    sxy = sxy + list1[i]*list2[i]
    sx3 = sx3 + (list1[i])**3
    sx4 = sx4 + (list1[i])**4
    sx2y = sx2y + ((list1[i])**2)*list2[i]



A = np.array([[n,sx],[sx,sx2]])
B = np.array([sy,sxy])
A2 = np.array([[n,sx,sx2],[sx,sx2,sx3],[sx3,sx3,sx4]])
B2 = np.array([sy,sxy,sx2y])
X = np.dot(np.linalg.inv(A),B)
X2 = np.dot(np.linalg.inv(A2),B2)


# degree 1 and 2
def LR(x):
    y = X[1]*x + X[0]
    return y
def QR(m):
    n = X2[2]*m*m + X2[1]*m + X2[0]
    return n
    
    
list3 = []
list4 = []
for j in list1:
    list3.append(LR(j))
    list4.append(QR(j))
    

# calculating mean squared  error 
ssr = 0
sse = 0
sst = 0
er = 0
er2 = 0
ssr2 = 0
sse2 = 0
sst2 = 0
avg = sum(list2)/n
for k in range(n):
    ssr = ssr + (list3[k] - avg)**2
    sse = sse + (list2[k] - list3[k])**2
    sst = sst + (list2[k] - avg)**2
    er = er + (list2[k] - list3[k])**2
    er2 = er2 + (list2[k] - list4[k])**2
    
    ssr2 = ssr2 + (list4[k] - avg)**2
    sse2 = sse2 + (list2[k] - list4[k])**2
    sst2 = sst2 + (list2[k] - avg)**2
    
print("\nR**2 for linear is : %f "%(ssr/sst))   
print("R**2 for Quadratic : %f "%(ssr2/(sse2+ssr2)))   
print("So better is Linear Interpolation.")
print("Function is y = %f *x + %f "%(X[1],X[0]))
print("x - Year of experinece & y - salary.\n")


# plotting the curves
plt.scatter(list1,list2, marker='o',s=90,c='m')
plt.plot(list1,list3,'y',linewidth=8,label='Degree 1')
plt.plot(list1,list4,'c',linewidth=4,label='Degree 2')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.legend()
plt.show()


# uncomment this to run model on input data

#case = float(input("Enter x : "))
#print("y is : %f"%LR(case))








