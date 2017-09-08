
print (" Marry had a little lamp")
#string formatting using .fromat() functions
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
#rpetaion using asterisk ( In this case it will print ten dots continuously in a line)
print("." * 10)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Python’s print() function comes with a parameter called ‘end’. By default, the value of this 
#parameter is ‘\n’, i.e. the new line character. You can end a print statement with any character/string 
#using this parameter. In this case end paramter act as a space

print(end1 + end2 + end3 + end4 + end5 + end6 , end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
