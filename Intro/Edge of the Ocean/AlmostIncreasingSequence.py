def solution(sequence):
	count=0
	for i in range(1,len(sequence)):
		if sequence[i] <= sequence[i-1]:
			count += 1
		if i==1 or sequence[i] > sequence[i-2]:
			sequence[i-1] = sequence[i]
		else:
			sequence[i] = sequence[i-1]
		if count > 1:
			return False
	return True