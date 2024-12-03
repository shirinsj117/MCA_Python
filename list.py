n=input("Enter a string: ")
list_string=n

newlist=[i for i in list_string.casefold()] 

dict={}.fromkeys(newlist,0)

for i in newlist:
    if i in dict:
     dict[i]+=1
print(list_string)
print(dict)
#2. Adding 'ing' at the end of the string
if len(n) >= 3:
    if n[-3:] != "ing": 
        print(n + "ing")
    else:
        print(n + "ly")
else:
    print(n)
#3. accept list of words and return the length of the longest word
list=["Hello","World","programming","python","Advanced DS"]
print(list)
a=0
for i in list:
    if len(i)>a:
        a=len(i)
    else:
        a
        print(a)
#4. Pattern printing
n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="") 
        print('')
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')