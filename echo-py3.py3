import sys as sys

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	# again
	# again commit 2

	yield datum

# modelop.metrics
def dict_metrics(datum):
	yield {
		"foo": 1,
		"bar": "test result"
	}
