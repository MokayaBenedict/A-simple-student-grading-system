mark=int(input("Enter your grades:  =>"))
def gradeGenerator(mark):
  if mark <0 or mark>100:
    return "Invalid Mark"
  elif mark >79:
    return "A => You smashed it"
  elif mark >=60 and mark <=79:
    return "B => You gave it your best"
  elif mark >=49 and mark <=59:
    return "C => Keep pushing, you'll make it"
  elif mark >=40 and mark <=48:
   return "D => Better luck next time"
  else:
   return "F => The biggest room is room for improvement,keep pushing hard"
print(gradeGenerator(mark))
  
    