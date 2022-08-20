# Difference between set / dictionary 

# names = ["John", "John", "John", "Liam", "TJ", "Daniel", "Derek"]

# print(names)
# print(names)
# print(names) 

# s = set(names)
# print(s)

# #initializing empty dictionary 
# names = dict()


# TJ = [["age", 12], ["school", "YISS"]]


# 1. mostFrequent(L): 
# Return the most frequent element in list L
def mostFrequent(L):
	maxName, maxCount = "", 0 
	nameDict = {}	
	for i in L: 
		nameDict[i] = nameDict.get(i, 0) + 1 	# storing value frequency for key name
		if maxCount < nameDict[i]: 
			maxCount = nameDict[i]
			maxName = i
	return maxName








print(mostFrequent(["TJ", "TJ",  "Lisa", "John", "Jack", "Phil", "John"]))



# nameList = []
# nameDict = {}
# nameDict["Andy"] = 3 
# nameDict["TJ"] = 1
# nameDict["Paul"] = 2
# nameDict["Andy"] = 6			# updates Andy value to 6 
# del nameDict["Andy"]			# removes key/val pair Andy
# # del nameDict["Daniel"]	# crashes if trying to delete a key not existing in dictionary

# print(nameDict)
# print(len(nameDict))

# x = nameDict.get("Paulie", 8)
# print(x)

