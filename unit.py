def Converse(A,B)
  if A=1
    return B/1000
  eif A=2
    return B*1000
  else
    return "shit"   
def test_Converse()
  assert Converse(1,1000)==1
     
