import sys as sys

# before reset 2

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)

	yield datum

# modelop.metrics
def dict_metrics(datum):
# after reset 1
# after reset 1
# after reset 3
	yield {
		"foo": 1,
		"bar": "test result"
	}
