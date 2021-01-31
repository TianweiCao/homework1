def gram2kgram(a,b):
  if a=="gram":
    return b/1000
  elif a=="kgram":
    return b*1000
  else:
    return "please enter valid input"   
  

  def test_gram2kgram():
    assert gram2kgram("gram",1000)==1
    
  
