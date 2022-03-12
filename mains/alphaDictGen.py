from alphaArrGen import *
from Sanity1 import keys as k
func = 'alphDict = { '

for i in range(len(alphaArr)):
	func += '"'+alphaArr[i]+'": "'+k[1][i]+'", '

func += '"end": period }'

