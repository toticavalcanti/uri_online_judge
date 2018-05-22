#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sub_tags(tag, num, str_to_sub):
	opened = False
	result = []
	flag = False

	tag = tag.lower()
	i = 0
	while i < len(str_to_sub):
		if str_to_sub[i] == "<":
			opened = True
			result.append(str_to_sub[i])
			i += 1
		elif str_to_sub[i] == ">":
			opened = False
			result.append(str_to_sub[i])
			i += 1
		elif str_to_sub[i].lower() == tag[0] and opened:
			pos = 0
			flag = True
			for j in range(1, len(tag)):
				if str_to_sub[i + j].lower() == tag[j].lower():
					flag = True
					pos = j
				else:
					flag = False
					result.append(str_to_sub[i])
					i += 1
					break
			if flag:
				result.append(str(num))
				i = i + 1 + pos
		else:
			result.append(str_to_sub[i])
			i = i + 1

	return "".join(result)

while True:
	try:
		tag = input()
		num = input()
		str_to_sub = input()
		print(sub_tags(tag, num, str_to_sub))
	except(EOFError):
		break
