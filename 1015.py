#https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

lst = []
for i in range(2):
    lst.append(list(map(float, input().split(" "))))
res = ((lst[1][0] - lst[0][0]) ** 2 + (lst[1][1] - lst[0][1]) ** 2) ** 0.5
print("{:.4f}".format(res))
