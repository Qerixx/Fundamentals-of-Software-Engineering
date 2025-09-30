N=int(input())
a = N//3600
b=(N-(a*3600))//60
c=(N-(a*3600))%60
print('{}:{:02}:{:02}'.format(a, b, c))
