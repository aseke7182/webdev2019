def count_substring(string, sub_string):
    go = True
    start = 0
    cnt = 0
    while go:
        a = string.find(sub_string,start)
        if a== -1:
            go = False
        else:
            cnt+=1
            start = a + 1
    return cnt

if __name__ == '__main__':