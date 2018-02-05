#https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

str = input()

lst = list(map(int, str.split(" ")))

print("{} eh o maior".format(max(lst)))
