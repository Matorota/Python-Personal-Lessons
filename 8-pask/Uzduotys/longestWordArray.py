def longestword(filename):
	with open(filename,'r+') as f:
		words = f.read().split()
		max_len_word = max(words,key=len)
		max_len = len(max(words,key=len))
		print('maximum lenth word in file :',max_len_word)
		print('lenth is : ',max_len)

longestword('data.txt')