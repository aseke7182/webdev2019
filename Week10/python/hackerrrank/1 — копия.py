arr = (input()).split()
n = int(arr[0])
m = int(arr[1])
for i in range(n):
    if i<(n-1)/2:
        print(( (i*2+1) * ".|.").center(m,'-'))
    elif i== (n-1)/2:
        print("WELCOME".center(m,'-'))
    else:
        x = n-i-1
        print(( (x*2+1) *  ".|.").center(m,'-'))

