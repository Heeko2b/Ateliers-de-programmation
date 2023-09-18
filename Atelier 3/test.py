import re

#Check if the string starts with "The" and ends with "Spain":

txt = "bisgambiglia"
x = re.search("^(?!.*\.$)(?!.*\.\.)([\w^\.]*)$", txt) #Pas de . au début, pas de point a la fin
#x = re.search("^([\w[^\.]]{0,5})$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")