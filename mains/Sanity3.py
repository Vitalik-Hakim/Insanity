### ALL CHARACTERS ARE OUTPUT WITHIN ONE CELL ###
## Cell is 'cleaned' after outputting character##
#       Allows for limitless story-telling      #

from beta import *
from alphaArrGen import *
# 2D Array
keys = [alphaArr,[A,a,B,b,C,c,D,d,E,e,F,f,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z,SPACE,period,comma,questionmark,at]]

final_story = []
ask = input("Type A to input text. Type B to input a file.")
if ask == "A":
	get = input("Please input your story here: ")
	get = get.replace(" " ,"*") #for space " "
	content = list(get)
elif ask == "B":
	file = input("Input file path")
	get = open(str(file),'r').read()
	get = get.replace(" " ,"*") #for space " "
	content = list(get)
else:
	print ("Invalid output")
getfor = get

for letter in content:
	for ind in range(len(keys[0])):
		if letter == keys[0][ind]:
			final_story.append(keys[1][ind])

story = ' '.join(str(e) for e in final_story)
print("This is your story in BrainFuck "+"\n"+story)
yes_list = ["yes","Y","y","Yes","Si","Oui"]
YorN = input("Do you want to write this into to a text file?: ")
if YorN in yes_list:
    with open("{}.txt".format(getfor[0:10]), "w") as text_file:
        story = story.replace(" ","\n")
        text_file.write(story)