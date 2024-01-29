import sys as sys

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	# after reset 1
	# after reset 3

	yield datum

# modelop.metrics
def dict_metrics(datum):
	# after reset 2
	# after reset 4
	yield {
		"foo": 1,
		"bar": "test result"
	}
