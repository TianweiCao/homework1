def gram2kgram(a,b):
  if a=="gram":
   
    return b/1000
  elif a=="kgram":
    return b*1000 #missed
  else:
    return "please enter valid input"   
  

def c2f(a,b):
  if a=="F":
    return b/33.8 #missed
  elif a=="C":
    return b*33.8
  else:
    return "please enter valid input" #missed
  
def meter2mile(a,b):
  if a=="meter":
    return b/1609 #missed
  elif a=="mile":
    return b*1609
  else:
    return "please enter valid input" #missed
  
def meter2feet(a,b):
  if a=="meter":
    return b*3.2
  elif a=="feet": #missed
    return b/3.2
  else:
    return "please enter valid input"

def meter2inch(a,b):
  if a=="meter":
    return b*39.4 #missed
  elif a=="inch":
    return b/39.4
  else:
    return "please enter valid input"

 
def test_right():
    assert c2f("C",1)==33.8
    assert gram2kgram("gram",1000)==1
    assert meter2mile("mile",1)==1609
    assert meter2feet("meter",1)==3.2
def test_wrong():
    assert gram2kgram("gra",1000)== "please enter valid input" 
    assert c2f("d",1)== "please enter valid input"
    assert meter2mile("feet",1000)== "please enter valid input"
    assert meter2feet("mile",1000)== "please enter valid input"
    assert meter2inch("feet",1000)== "please enter valid input"
    
        
