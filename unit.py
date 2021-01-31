def gram2kgram(a,b):
  if a=="gram":
    return b/1000
  elif a=="kgram":
    return b*1000
  else:
    return "please enter valid input"   
  
def C2F(a,b):
  if a=="F":
    return b/33.8
  elif a=="C":
    return b*33.8
  else:
    return "please enter valid input"

  def test_gram2kgram():
  assert gram2kgram("gram",1000)==1
  def test_C2F()
  assert C2F("C",1)==33.8
     
