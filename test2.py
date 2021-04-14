class InvalidLengthException(Exception):
 pass
class mobile:
 def __init__(self,mob):
  self.__mob = mob
 def val(self):
  try:
   if(len(self.__mob)!=10):
    raise InvalidLengthException
   else:
    print("Valid number")
  except InvalidLengthException:
   print("Invalid")
  print("Inside class")
mob = mobile("1234567890")
try:
 mob.val()
 print("Outside")
except InvalidLengthException:
 print("Invalid length")

