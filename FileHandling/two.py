#read - user.txt file and print data

fp=open('user.txt','r')
data=fp.read()
print(data)
fp.close()