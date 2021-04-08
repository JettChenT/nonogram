def pprint(mtrx):
	for i in range(len(mtrx)):
		for j in range(len(mtrx[i])):
			print(f"{mtrx[i][j]}",end=' ')
		print()			