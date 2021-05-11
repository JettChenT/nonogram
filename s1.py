from pprint import pprint
import time
import random
matrix = []
sideLen=eval(input("side length="))
accu=0
ANIMATION = False
jmp = False
DT = 0.1

# up
row_rules = []
# left
col_rules = []

print("Please enter row rules:")
for _ in range(sideLen):
	tl = list(map(int,input().split()))
	row_rules.append(tl)

print("Please enter col rules:")
for _ in range(sideLen):
	tl = list(map(int,input().split()))
	col_rules.append(tl)

print("solving...")
	
solved = False

for i in range(sideLen):
	matrix.append([])
	for j in range(sideLen):
		matrix[i].append(0)

def get_row(n):
	return [lst[n] for lst in matrix]
	
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
		return 2-(i==j)
	return 3

def validate(i,j):
	global solved
	if solved:
		return True
	s = status(i,j)
	cr = cnt(get_row(j))
	if len(cr)>len(row_rules[j]):
		return False
	flag = True
	for k in range(min(len(cr),len(row_rules[j]))):
		flag = flag and (cr[k]<=row_rules[j][k])
	if flag==False:
		return False
	if s==2:
		cnts = cnt(matrix[i])
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
	if len(cnts)>len(col_rules[i]):
		return False
	if cnts==col_rules[i]:
		global jmp
		jmp = True
		return False
	if len(cnts)==len(col_rules[i]):
		flag = True
		for j in range(len(cnts)):
			flag = flag and (cnts[j]<=col_rules[i][j])
		return flag
	return cnts[-1]<=col_rules[i][len(cnts)-1]
	
def check_row(r):
	return cnt(matrix[r]) == col_rules[r]

def bt(i,j):
	global accu
	accu+=1
	global matrix
	v = validate(i, j)
	global jmp
	if jmp:
		jmp = False
		if i==sideLen-1:
			return True
		ni,nj = i+1,0
	else:
		if not v:
			return False
		if solved:
			return True
	
		ni,nj = next_cord(i, j)
		if ni==nj==-1:
			return v
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
		# print("SOLVED!")
		# pprint(matrix)
		return
	else:
		matrix[0][0] = 0
		if bt(0,0):
			# print("SOLVED!")
			# pprint(matrix)
			return
		else:
			print("No solution!")
			return
	print(accu)
	

ti = time.time()
main()
tt = time.time()-ti
pprint(matrix)
print(f"time taken:{tt} seconds")
