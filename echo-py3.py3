import sys as sys


# modelop.score
def action(datum):
	sys.stdout.flush()
	# before commit 2
	# before commit 3
	print(datum)
	# prod

	yield datum

# modelop.metrics
def dict_metrics(datum):
# another commit for 1
# another commit for 2
# another commit for 3
	yield {
		"foo": 1,
		"bar": "test result"
	}
