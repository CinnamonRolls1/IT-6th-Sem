pix_nos=[]
s=0
for i in range(8):
    print("Enter no of pixels for gray image level "+str(i))
    no=int(input())
    s+=no
    pix_nos.append(no)

pm=list(map(lambda x:x/s, pix_nos))
cm=pm
cum=0
for i in range(len(cm)):
    cm[i]+=cum
    cum=cm[i]
L=list(map(lambda x:x*7, cm))
rounded_cm=[]
for val in L:
    rounded_cm.append(round(val))

prev=-1

new_pix_nos=[]
for i in range(len(rounded_cm)):
    if rounded_cm[i]==prev:
        new_pix_nos[-1]+=pix_nos[i]
    else:
        new_pix_nos.append(pix_nos[i])
    prev=rounded_cm[i]

print(new_pix_nos)