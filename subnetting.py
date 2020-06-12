class nosubnetmasking(Exception):
    pass
b=list()
subnet=''
z=0
a=input('ENTER IP ADDRESS:  ')
b=a.split('.')
c=int(b[0])
if (c>=192  ):
    pass

if (c>=1 and c<=127):
    subnet='255.'*1
    z=254**3
    cl='A'
if (c>=128 and c<=191):
    cl='B'
if (c>=192 and c<=223):
    cl='C'
if (c>=224 and c<=255):
    print('It doesnot have any subnet masking.')
    exit()

n=int(input("Enter how many computer you want to connect to IP :"))
if (cl=='A'):
    if(n>=65534):
        x=16777214-n
        add=x//(256*256)
        output='255.'+str(add)+'.0.0'
    elif(n>=254):
        x=65534-n
        add=x//256
        output='255.'*2+str(add)+'.0'
    else:
        add=254-n
        output='255.'*3+str(add)
if (cl=='B'):
    if(n>254):
        x=65534-n
        add=x//256
        output='255.'*2+str(add)+'.0'
    else:
        add=254-n
        output='255.'*3+str(add)
if (cl=='C'):
    add=z-n
    output='255.'*3+str(add)

print('The Required Subnet Mask is : ',output)
