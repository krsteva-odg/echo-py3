import sys as sys


# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	print(datum)

	yield datum

# modelop.metrics
def dict_metrics(datum):
	# commit after reset for 1
	# commit again 2
	yield {
		"foo": 1,
		"bar": "test result"
	}
