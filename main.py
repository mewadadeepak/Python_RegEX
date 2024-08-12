import re

"""
#Check if the string starts with "Deepak" and ends with "engineer":

txt = "Deepak is a software engineer"
x = re.search("^Deepak.*engineer$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match"                
                                       """


"""
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)                       
                                  """

"""
#Return a empty string if no match found
txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")                                   
                                        """

"""
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())        
                                                                                   """
"""
#The split() function returns a list where the string has been split at each match:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)                                              
                                                  """
"""
#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
                                               """
"""
#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
                                                     """
"""
#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
                                                      """

"""
#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)  
print(x)
                                                 """

"""
#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

                                       """

"""
#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
                                       """


#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())








