# A python program to transpile an english story into brainfuck equivalent
#The elifs get wayyyy crazy :))
from alpha import *

final_story = []
temp_story = []
get = input("Please input your story here: ")
getfor = get
get = get.replace(" " ,"*") #for space " "
content = list(get)
cell = 0
for letter in content:
    if letter == "A":
        cell = cell+1
        temp_story.append(A)
        final_story.append(((cell)*">"+A))
    elif letter == "B":
        cell = cell+1
        temp_story.append(B)
        final_story.append(((cell)*">"+B))
    elif letter == "C":
        cell = cell+1
        temp_story.append(C)
        final_story.append(((cell)*">"+C))
    elif letter == "D":
        cell = cell+1
        temp_story.append(D)
        final_story.append(((cell)*">"+D))
    elif letter == "E":
        cell = cell+1
        temp_story.append(E)
        final_story.append(((cell)*">"+E))
    elif letter == "F":
        cell = cell+1
        temp_story.append(F)
        final_story.append(((cell)*">"+F))
    elif letter == "G":
        cell = cell+1
        temp_story.append(G)
        final_story.append(((cell)*">"+G))
    elif letter == "H":
        cell = cell+1
        temp_story.append(H)
        final_story.append(((cell)*">"+H))
    elif letter == "I":
        cell = cell+1
        temp_story.append(I)
        final_story.append(((cell)*">"+I))
    elif letter == "J":
        cell = cell+1
        temp_story.append(J)
        final_story.append(((cell)*">"+J))
    elif letter == "K":
        cell = cell+1
        temp_story.append(K)
        final_story.append(((cell)*">"+K))
    elif letter == "L":
        cell = cell+1
        temp_story.append(L)
        final_story.append(((cell)*">"+L))
    elif letter == "M":
        cell = cell+1
        temp_story.append(M)
        final_story.append(((cell)*">"+M))
    elif letter == "N":
        cell = cell+1
        temp_story.append(N)
        final_story.append(((cell)*">"+N))
    elif letter == "O":
        cell = cell+1
        temp_story.append(O)
        final_story.append(((cell)*">"+O))
    elif letter == "P":
        cell = cell+1
        temp_story.append(P)
        final_story.append(((cell)*">"+P))
    elif letter == "Q":
        cell = cell+1
        temp_story.append(Q)
        final_story.append(((cell)*">"+Q))
    elif letter == "R":
        cell = cell+1
        temp_story.append(R)
        final_story.append(((cell)*">"+R))
    elif letter == "S":
        cell = cell+1
        temp_story.append(S)
        final_story.append(((cell)*">"+S))
    elif letter == "T":
        cell = cell+1
        temp_story.append(T)
        final_story.append(((cell)*">"+T))
    elif letter == "U":
        cell = cell+1
        temp_story.append(">"+U)
        final_story.append(((cell)*">"+U))
    elif letter == "V":
        cell = cell+1
        temp_story.append(V)
        final_story.append(((cell)*">"+V))
    elif letter == "W":
        cell = cell+1
        temp_story.append(W)
        final_story.append(((cell)*">"+W))
    elif letter == "X":
        cell = cell+1
        temp_story.append(X)
        final_story.append(((cell)*">"+X))
    elif letter == "Y":
        cell = cell+1
        temp_story.append(Y)
        final_story.append(((cell)*">"+Y))
    elif letter == "Z":
        cell = cell+1
        temp_story.append(Z)
        final_story.append(((cell)*">"+Z))

    elif letter == "*":
        cell = cell+1
        temp_story.append(SPACE)
        final_story.append(((cell)*">"+SPACE))
    elif letter == "a":
        cell = cell+1
        temp_story.append(a)
        final_story.append(((cell)*">"+a))
    elif letter == "b":
        cell = cell+1
        temp_story.append(b)
        final_story.append(((cell)*">"+b))
    elif letter == "c":
        cell = cell+1
        temp_story.append(c)
        final_story.append(((cell)*">"+c))
    elif letter == "d":
        cell = cell+1
        temp_story.append(d)
        final_story.append(((cell)*">"+d))
    elif letter == "e":
        cell = cell+1
        temp_story.append(e)
        final_story.append(((cell)*">"+e))
    elif letter == "f":
        cell = cell+1
        temp_story.append(f)
        final_story.append(((cell)*">"+f))
    elif letter == "g":
        cell = cell+1
        temp_story.append(g)
        final_story.append(((cell)*">"+g))
    elif letter == "h":
        cell = cell+1
        temp_story.append(h)
        final_story.append(((cell)*">"+h))
    elif letter == "i":
        cell = cell+1
        temp_story.append(i)
        final_story.append(((cell)*">"+i))
    elif letter == "j":
        cell = cell+1
        temp_story.append(j)
        final_story.append(((cell)*">"+j))

    elif letter == "k":
        cell = cell+1
        temp_story.append(k)
        final_story.append(((cell)*">"+k))
    elif letter == "l":
        cell = cell+1
        temp_story.append(l)
        final_story.append(((cell)*">"+l))
    elif letter == "m":
        cell = cell+1
        temp_story.append(m)
        final_story.append(((cell)*">"+m))

    elif letter == "n":
        cell = cell+1
        temp_story.append(n)
        final_story.append(((cell)*">"+n))

    elif letter == "o":
        cell = cell+1
        temp_story.append(o)
        final_story.append(((cell)*">"+o))

    elif letter == "p":
        cell = cell+1
        temp_story.append(p)
        final_story.append(((cell)*">"+p))

    elif letter == "q":
        cell = cell+1
        temp_story.append(q)
        final_story.append(((cell)*">"+q))


    elif letter == "r":
        cell = cell+1
        temp_story.append(r)
        final_story.append(((cell)*">"+r))

    elif letter == "s":
        cell = cell+1
        temp_story.append(s)
        final_story.append(((cell)*">"+s))

    elif letter == "t":
        cell = cell+1
        temp_story.append(t)
        final_story.append(((cell)*">"+t))

    elif letter == "u":
        cell = cell+1
        temp_story.append(u)
        final_story.append(((cell)*">"+u))
    elif letter == "v":
        cell = cell+1
        temp_story.append(v)
        final_story.append(((cell)*">"+v))
    elif letter == "w":
        cell = cell+1
        temp_story.append(w)
        final_story.append(((cell)*">"+w))
    elif letter == "x":
        cell = cell+1
        temp_story.append(x)
        final_story.append(((cell)*">"+x))
    elif letter == "y":
        cell = cell+1
        temp_story.append(y)
        final_story.append(((cell)*">"+y))
    elif letter == "z":
        cell = cell+1
        temp_story.append(z)
        final_story.append(((cell)*">"+z))
    elif letter == ".":
        cell = cell+1
        temp_story.append(period)
        final_story.append(((cell)*">"+period))
    elif letter == ",":
        cell = cell+1
        temp_story.append(comma)
        final_story.append(((cell)*">"+comma))
    elif letter == "?":
        cell = cell+1
        temp_story.append(period)
        final_story.append(((cell)*">"+period))
    elif letter == "@":
        cell = cell+1
        temp_story.append(at)
        final_story.append(((cell)*">"+at))
    else:
        pass


##### Ahh finallyyy what a tedious code####
story = ' '.join(str(e) for e in final_story)
print("This is your story in BrainFuck "+"\n"+story)



yes_list = ["yes","Y","y"]
YorN = input("Do you want to write this into to a text file?: ")
if YorN in yes_list:
    with open("{}.txt".format(getfor[0:10]), "w") as text_file:
        story = story.replace(" ","\n")
        text_file.write(story)
else:
    pass
