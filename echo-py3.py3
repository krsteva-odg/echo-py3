import sys as sys


# modelop.score
def action(datum):
	sys.stdout.flush()
	# before commit 2
	print(datum)
	# prod

	yield datum

# modelop.metrics
def dict_metrics(datum):
# another commit for 1
	yield {
		"foo": 1,
		"bar": "test result"
	}
