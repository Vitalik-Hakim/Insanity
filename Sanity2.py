from alpha import *
from alphaDictGen import func
# dictionary 
alhpDict = {}
exec(func)
final_story = []
get = input("Please input your story here: ")
get = get.replace(" " ,"*") #for space " "
content = list(get)
cell = 0

for letter in content:
	for key, val in alphDict:
		if letter == key:
			cell += 1
			final_story.append((cell*">"+val))

story = ' '.join(str(e) for e in final_story)
print("This is your story in BrainFuck "+"\n"+story)