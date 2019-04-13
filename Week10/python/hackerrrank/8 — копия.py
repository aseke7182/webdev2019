if __name__ == '__main__':
    s = input()
    ok = False
    for i in s:
        if i.isalnum():
            ok = True
    print(ok)
    ok = False

    
    for i in s:
        if i.isalpha():
            ok = True
    print(ok)
    ok = False

    
    for i in s:
        if i.isdigit():
            ok = True
    print(ok)
    ok = False

    
    for i in s:
        if i.islower():
            ok = True
    print(ok)
    ok = False

    
    for i in s:
        if i.isupper():
            ok = True
    print(ok)
    ok = False

