if __name__ == '__main__':
    n = int(input())
    arr =  input().split()
    maxi = -101
    ans = -101


    for i in arr:
        if int(i) > maxi:
            ans = maxi
            maxi = int(i)
        elif int(i) > ans and int(i)!=maxi:
            ans = int(i)
    print(ans)

