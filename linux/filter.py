import json

# indent string
INDENT = '\t'

def usage():
	print ('usage : tree [TARGET_PATH] -J | jq . -c | python3 filter.py')

def parseContent(depth, content):
	indents = ''
	for d in range(depth):
		indents += INDENT

	# type
	#   directory
	#   file
	#   report ( jq command report. )
	tp = content['type']

	if tp =='directory':
		print('{}{}/'.format(indents, content['name']))
		for c in content['contents']:
			parseContent(depth + 1, c)
	elif tp == 'file':
		print('{}{}'.format(indents, content['name']))

if __name__ == '__main__':
	# parse stdin
	try:
		contents = json.loads(input())
	except Exception as e:
		print(e)
		usage()
		exit()

	# print
	for content in contents:
		parseContent(0, content)
