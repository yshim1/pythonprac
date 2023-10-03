#Determines if two strings have common characters
word = 'abcdef'
word2 = "azcxev"
word3 = "ylmt"
mask = 0
mask2 = 0
mask3 = 0
for c in word:
  mask |= (1 << (ord(c) - ord('a')))
print(mask)
for c in word2:
  mask2 |= (1 << (ord(c) - ord('a')))
print(mask2)
for c in word3:
  mask3 |= (1 << (ord(c) - ord('a')))
print(mask3)
print(mask & mask2 > 0) #the & operator determines if there are common chars. 
#If result is non zero, then the two strings have common characters
print(mask3 & mask2 > 0)