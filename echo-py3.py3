import sys as sys

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	# again
	# again commit 2
# hi 9:30
# commit 4 after reset
# commit 5 after reset
	yield datum

# modelop.metrics
def dict_metrics(datum):
	yield {
		"foo": 1,
		"bar": "test result"
	}
