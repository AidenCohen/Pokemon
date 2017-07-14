i = [0,0,0,1,0]
r = 10

while(r<99801):
  done = False
  r = r+1
  i[4] = i[4]+1
  if(i[4] == 9):
    i[3] = i[3]+1
    i[4] = 0
  if( float(i) == float(i)[::-1] and done == False):
      print(r)
      done = True
