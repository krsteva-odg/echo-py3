import sys as sys


# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	print(datum)
	print(datum)
	print(datum)
	# try to reproduce
	# Detect change

	yield datum

# modelop.metrics
def dict_metrics(datum):
	yield {
		"foo": 1,
		"bar": "test result"
	}
