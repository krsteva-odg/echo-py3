import sys as sys

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	# after commit 1
	# after commit 2
	# after commit 3
	# commit 4

	yield datum

# modelop.metrics
def dict_metrics(datum):
	yield {
		"foo": 1,
		"bar": "test result"
	}
