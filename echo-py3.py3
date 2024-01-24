import sys as sys

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)

	yield datum

# after reset commit 2
# after reset commit 3
# single commit, no reset

# modelop.metrics
def dict_metrics(datum):
	# after reset commit 1
	yield {
		"foo": 1,
		"bar": "test result"
	}
