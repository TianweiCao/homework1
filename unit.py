def gram2kgram(a,b):
  if a=="gram":
    return b/1000,"kgram"
  elif a=="kgram":
    return b*1000,"gram"
  else:
    return "please enter valid input"   
  

def c2f(a,b):
  if a=="F":
    return b/33.8
  elif a=="C":
    return b*33.8
  else:
    return "please enter valid input"
  
def meter2mile(a,b):
  if a=="meter":
    return b/1609
  elif a=="mile":
    return b*1609
  else:
    return "please enter valid input"
 
def test_c2f():
    assert c2f("C",1)==33.8
     
def test_c2f():
    assert gram2kgram("gram",1000)==1kgram

def test_meter2mile():
    assert meter2mile("mile",1)==1609
        
