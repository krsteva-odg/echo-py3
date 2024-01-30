import sys as sys
# after reset 3

# modelop.score
def action(datum):
	sys.stdout.flush()
	# after reset 1
	print(datum)

	yield datum

# modelop.metrics
def dict_metrics(datum):
# after reset 2
	yield {
		"foo": 1,
		"bar": "test result"
	}
