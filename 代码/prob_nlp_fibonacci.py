def function(x):
    f=-3*x*x+21.6*x+1
    return f
def fibonacci(x):
    if x==0 or x==1:
        y=1
    else:
        y=fibonacci(x-2)+fibonacci(x-1)
    return y
a=float(input("请输入区间上界:"))
b=float(input("请输入区间下界:"))
c=float(input("请输入区间缩短的相对精度:"))
i=1
k=1
cigma=0.01
while i<=100:
    if fibonacci(i)>=(1/c):
        n=i
        break
    i=i+1
print(n)
while k<=(n-2):
    t_1=a+0.382*(b-a);t_2=a+0.618*(b-a)
    if function(t_1)<function(t_2):
        b=t_2;a=a
    elif function(t_1)>function(t_2):
        a=t_1;b=b
    print("第{}次t_1,t_2的值分别为:".format(k),t_1,t_2)
    print("第{}次t_1、t_2的函数值分别为:".format(k),function(t_1),function(t_2))
    print("第{}次的区间为：".format(k),a,b)
    k=k+1
t_1=(a+b)/2;t_2=a+(0.5+cigma)*(b-a)
print("t_1,t_2:",t_1,t_2)
print("函数最小值：")
if function(t_1)<function(t_2):
    print(t_1,function(t_1))
elif function(t_1)>function(t_2):
    print(t_2,function(t_2))