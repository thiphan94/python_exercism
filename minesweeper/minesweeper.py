def annotate(minefield):


    n = len(minefield)
	m = len(minefield[0]) if n > 0 else 0
	res = []
	for i in range(n):
		if len(minefield[i]) != m:
			raise ValueError('The board is invalid with current input.')
		s = []
		for j in range(m):
			if minefield[i][j] == "*":
				s.append("*")
			elif minefield[i][j] == ' ':
				x = sum(minefield[a][b] == "*" for a in range(max(0, i-1), min(i+2, n)) for b in range(max(0, j-1), min(j+2, m)))				
				s.append(' ' if x == 0 else str(x))
			else:
				raise ValueError('The board is invalid with current input.')
		res.append("".join(s))
	return res