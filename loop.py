def count_code(code):
  count=0
  for i in range(len(code)):
    if code[i] == 'c' and code[i+1] == 'o' and code[i+3]=='e' :
      count=count+1
  print(count)    
count_code('a')
