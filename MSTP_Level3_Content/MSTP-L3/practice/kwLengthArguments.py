def playerDetails(**x):
	for item in x.items():
		print(item[0], ':', item[1])

playerDetails(name = "kohli", team = "rcb", native = "delhi")