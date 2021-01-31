def unit(a,b):
  if a=="meter":
    return b/1000
  if a=="temperature"
    return b*33.8
  elif a=="kilometer":
    return b*1000
  else:
    return "shit"   
  
def test_unit():
  assert unit("meter",1000)==1
     
