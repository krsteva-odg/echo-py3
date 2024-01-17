import sys as sys


# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	print(datum)
	# commit 4

	yield datum

# modelop.metrics
def dict_metrics(datum):
	# reset 3
	# commit after reset for 1
	# commit again 2
	print(datum)
	yield {
		"foo": 1,
		"bar": "test result"
	}
