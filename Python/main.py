import argparse


def read_lines(filename):
	with open(filename, 'r') as f:
		return list(f)

def exact_match(pattern, text):
	return pattern in text

def search(pattern, target_file):
	lines = read_lines(target_file)
	for i, line in enumerate(lines):
		if exact_match(pattern, line):
			print('{}: {}'.format(i, line[:-1]))

def main():
	parser = argparse.ArgumentParser(description='not quite grep')
	
	parser.add_argument('pattern', help='The pattern to look for')
	parser.add_argument('file', help='File to search from')

	args = parser.parse_args()
	
	search(args.pattern, args.file)

if __name__ == '__main__':
	main()
