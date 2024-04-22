name="Amrut"
print(type(name))

amount=45.90
print(type(amount))

#DataTypes
#1.Integer
#2.Boolean
#3.Float
#4.String
#5.None
def num(n):
    print(n)

num("hyyy")    
l1="Rahul Gandhi".split()
print(type(l1))
print(l1)

h1=[10,20,30]
h2=h1.copy()

print(type(h2))

enames=['Rahul','Sonia','Priyanka',"Modi"]
for ename in enames:
    print(ename)

i=0
while i<=len(enames)-1:
    print(enames[i])
    i=i+1

usernames=['Rahuli','Sonia','Priyanka',"Modi"]
usernames.append('amitsaha')
print(usernames)



polnames=['Rahulw', 'Sonia', 'Priyankaw', 'Modiw', 'Amithw']
#         0        1         2          3       4
# insert "Rajiv Gandhi" at index 1 - using index method
#what is list index method. insert elemnt at specified index value

polnames.insert(2,"rajivw")
print(polnames)

r1=[10,60,30]
r2=[52,78,74]
r3=r1.extend(r2)
print(r3)
