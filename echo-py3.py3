import sys as sys


# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)

	yield datum

# modelop.metrics
def dict_metrics(datum):
	# Diff commit after reset
	yield {
		"foo": 1,
		"bar": "test result"
	}
