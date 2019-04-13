from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    cnt = 0
    size = 0
    for i in student_marks[query_name]:
        size+=1
        cnt += i;
    ans = Decimal(cnt/size)
    print(round(ans,2))
