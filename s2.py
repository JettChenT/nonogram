from pprint import pprint
import time
from q import Q,parse
matrix = []
sideLen=eval(input("side length="))
accu=0
ANIMATION = True
DT = 0

# up
row_rules = []
# left
col_rules = []


print("Please enter row rules:")
for _ in range(sideLen):
	ip = input()
	tl = list(map(parse,ip.split()))
	row_rules.append(tl)

print("Please enter col rules:")
for _ in range(sideLen):
	ip = input()
	tl = list(map(parse,ip.split()))
	col_rules.append(tl)

print("solving...")
	
solved = False

for i in range(sideLen):
	matrix.append([])
	for j in range(sideLen):
		matrix[i].append(0)

def get_row(n):
	res = []
	for lst in matrix:
		res.append(lst[n])
	return res
	
def cnt(lst):
	cst = False
	tmpl = []
	for c in lst:
		if c and not cst:
			cst = True
			tmpl.append(1)
		elif c:
			tmpl[-1]+=1
		else:
			cst=False
	if len(tmpl)==0:
		return [0]
	return tmpl

def next_cord(i,j):
	s = status(i,j)
	if s==1:
		return (-1,-1)
	if s==2:
		return (i+1,0)
	return (i,j+1)

def status(i,j):
	if j==sideLen-1:
		if i==j:
			# At the ultimate end
			return 1
		# At end of the row
		return 2
	# Normal mode
	return 3

def validate(i,j):
	global solved
	if solved:
		return True
	s = status(i,j)
	# print(f"case {s}")
	if s==2:
		cnts = cnt(matrix[i])
		# print(cnts,col_rules[i])
		return cnts == col_rules[i]
	if s==1:
		flag = True
		flag = flag and (cnt(matrix[-1])==col_rules[i])
		for i in range(len(matrix[0])):
			flag = flag and (cnt(get_row(i))==row_rules[i])
		if flag:
			solved = True
		return flag
	cnts = cnt(matrix[i])
	# print(cnts,col_rules[i])
	if len(cnts)>len(col_rules[i]):
		# print("#1")
		return False
	if len(cnts)==len(col_rules[i]):
		# print("#2")
		flag = True
		for j in range(len(cnts)):
			# print(cnts[j]<=col_rules[i][j])
			flag = flag and (cnts[j]<=col_rules[i][j])
		return flag
	# print("#3")
	return cnts[-1]<=col_rules[i][len(cnts)-1]

def bt(i,j):
	global accu
	accu+=1
	global matrix
	if ANIMATION:
		print(validate(i,j))
		print(i,j)
		pprint(matrix)
		time.sleep(DT)
	if not validate(i, j):
		return False
	if solved:
		return True
	ni,nj = next_cord(i, j)
	if ni==nj==-1:
		return validate(i, j)
	matrix[ni][nj] = 1
	ans_a = bt(ni,nj)
	if ans_a:
		return True
	matrix[ni][nj] = 0
	ans_b = bt(ni,nj)
	if ans_b:
		return True
	return False

def main():
	global matrix
	matrix[0][0] = 1
	if bt(0,0):
		print("SOLVED!")
		pprint(matrix)
	else:
		matrix[0][0] = 0
		if bt(0,0):
			print("SOLVED!")
			pprint(matrix)
		else:
			print("No solution!")
	
	print(accu)

ti = time.time()
main()
tt = time.time()-ti
print(f"total time taken:{tt} seconds")
# matrix = [
# 	[1,0,1,1],
# 	[0,0,0,0],
# 	[0,0,1,0],
# 	[1,1,1,1]
# ]
# # 
# pprint(validate(3,0))