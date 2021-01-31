def gram2kgram(a,b):
  if a=="gram":
   
    return b/1000
  elif a=="kgram":
    return b*1000 #missed
  else:
    return "please enter valid input"   
  

def c2f(a,b):
  if a=="F":
    return round(b/33.8,2) 
  elif a=="C":
    return round(b*33.8,2)
  else:
    return "please enter valid input" #missed
  
def meter2mile(a,b):
  if a=="meter":
    return round(b/1609,4) 
  elif a=="mile":
    return round(b*1609,4)
  else:
    return "please enter valid input" 
  
def meter2feet(a,b):
  if a=="meter":
    return round(b*3.2,2)
  elif a=="feet": 
    return round(b/3.2,2)
  else:
    return "please enter valid input"

def meter2inch(a,b):
  if a=="meter":
    return round(b*39.4,2) 
  elif a=="inch":
    return round(b/39.4,2)
  else:
    return "please enter valid input"

 
def test_right():
    assert gram2kgram("gram",1000)==1
    assert gram2kgram("gram",100)==0.1
    assert c2f("F",1)==0.03
    assert c2f("C",1)==33.8
    assert meter2mile('meter",1)==0.0006
    assert meter2mile("mile",1)==1609
    assert meter2feet("feet",1)==0.31
    assert meter2feet("meter",1)==3.2
    assert meter2inch("meter",1)==39.4
    assert meter2inch("inch",1)==0.03
    
def test_wrong():
    assert gram2kgram("gra",1000)== "please enter valid input" 
    assert c2f("d",1)== "please enter valid input"
    assert meter2mile("feet",1000)== "please enter valid input"
    assert meter2feet("mile",1000)== "please enter valid input"
    assert meter2inch("feet",1000)== "please enter valid input"
    
        
