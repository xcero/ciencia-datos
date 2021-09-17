#For para manejo de Listas 
fruits = ["apple", "banana", "cherry"]
for value in fruits:
  print("Lista -", value)

#For para manejo de Tuples 
fruits = ("apple", "banana", "cherry")
for value in fruits:
  print("Tuples -",value)  

#For para manejo de Sets 
fruits = {"apple", "banana", "cherry"}
for value in fruits:
  print("Set -",value)    

#For para manejo de Dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for value in thisdict:
  print("Diccionary -", value, " - ", thisdict[value])      