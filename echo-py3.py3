import sys as sys

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	# commit 1
	# commit 2
	# commit 3
	# commit 4
	# commit 5
	# commit 6
	# commit 7

	yield datum

# modelop.metrics
def dict_metrics(datum):
	yield {
		"foo": 1,
		"bar": "test result"
	}
