from operator import *
def times_i_at_odd(L):
	return [L[i] for i in range(len(L)) if i%2 ==1]

def sum_cols(grid, n):
	if grid == []:
		return 0
	else:
		return grid[0][n]+sum_cols(grid[1:],n)

def replace_v1(s, a, b):
	"""a is one character string"""
	if s == "":
		return ""
	else:
		if s[0] == a:
			return b+replace_v1(s[1:], a, b)
		else:
			return s[0]+replace_v1(s[1:], a, b)

def replace_v2(s, a, b):
	"""a is one character string"""
	if s == "":
		return ""
	else:
		if s.startswith(a):
			return b+replace_v2(s[len(a):], a, b)
		else:
			return s[0]+replace_v2(s[1:], a, b)


ops = {"+": add, "-": sub, "*": mul, "/": truediv}

class Stack:
	def __init__(self):
		self._items =[]

	def push(self, item):
		self._items.append(item)

	def pop(self):
		return self._items.pop()

def eval_postfix(expr):
	s = Stack()
	l = expr.split()
	for token in l:
		if token >= '0' and token <= '9':
			s.push(token)
		else:
			v2 = int(s.pop())
			v1 = int(s.pop())
			s.push(ops[token](v1,v2))
	return s.pop()

