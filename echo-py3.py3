import sys as sys


# modelop.score
def action(datum):
	# after reset 1
	sys.stdout.flush()
	print(datum)

	yield datum

# modelop.metrics
def dict_metrics(datum):
# new
	# commit after reset
	yield {
		"foo": 1,
		"bar": "test result"
	}
