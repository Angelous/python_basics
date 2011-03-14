y = input ("Enter year of your birth ")
m = input ("Enter month of your birth ")
d = input ("Enter day of your birth ")
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

if m in [1,2]:
  m=m+12 
  y=y-1
  n = (d + 2*m + (3*(m+1)/5) + y + (y/4) - (y/100) + (y/400) + 2)%7
else:
  n = (d + 2*m + (3*(m+1)/5) + y + (y/4) - (y/100) + (y/400) + 2)%7
print days[n]