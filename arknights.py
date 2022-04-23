import random

#TODO:
# web app w/ screenshot uploading capability
# constraints
# reroll function (selective)
# MTG mulligan (reroll a random 11 op team)
# stretch: image process operator type????


# sort operator list by level.
# option in format [A, B, C]
# A: number of ops. Check your friend display to see how many you have.
# B: weighting. Rolls n random indices within [1, numOps] and selects the lowest number.
	# Also, weighting < 1 is dumb. If you set weighting < 1 I hate you and you will never pull another 6*.
# C: pageSize. Number of operators on a page when in the multi-select screen for squad comp.

CIRNOBYL = [180, 1, 16]
GANYULESS = [74, 1, 16]
SYO = [167, 1, 16] 
ZEPHYR = [185, 1, 12]

SETTINGS = CIRNOBYL


def randomize():
	global SETTINGS
	numOps = SETTINGS[0]
	weighting = SETTINGS[1]
	pageSize = SETTINGS[2]

	allOps = list(range(1,numOps))

	ops = set([])
	weighting = max(1, weighting) 
	while len(ops) < 12:
		result = allOps[-1] # set to max
		for j in range(weighting):
			result = min(result,random.randint(0,len(allOps)-1))
		ops.add(allOps[result])
		allOps.remove(allOps[result])

	ops = list(ops)
	ops.sort()
	return ops


def paginate(ops):
	global SETTINGS
	pageSize = SETTINGS[2]
	ops.sort()
	page = 1
	opsOnPage = []

	for op in ops:
		newPage = (op-1)//(pageSize)+1
		if newPage != page:
			if opsOnPage:
				print("Page", page, "no.", opsOnPage)
			opsOnPage = []
			page = newPage
		opsOnPage.append((op-1)%(pageSize)+1)
	if opsOnPage:
		print("Page", page, "no.", opsOnPage)


def main():
	ops = randomize()
	print(ops, "\n")
	paginate(ops)

main()
