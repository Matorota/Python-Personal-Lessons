def unique_list(big):
  num = []
  for a in big:
    if a not in num:
      num.append(a)
  return num
print('unique elements are')
print(unique_list([1,2,3,3,3,3,4,5]))
