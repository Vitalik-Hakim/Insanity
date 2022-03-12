from alpha import *
from alphaArrGen import *
# 2D Array
keys = [alphaArr,[A,a,B,b,C,c,D,d,E,e,F,f,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z,SPACE,period,comma,questionmark,at]]

final_story = []
get = input("Please input your story here: ")
get = get.replace(" " ,"*") #for space " "
content = list(get)
cell = 0

for letter in content:
	for ind in range(len(keys[0])):
		if letter == keys[0][ind]:
			cell += 1
			final_story.append((cell)*">"+keys[1][ind])

story = ' '.join(str(e) for e in final_story)
print("This is your story in BrainFuck "+"\n"+story)