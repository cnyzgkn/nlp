import re

pattern = re.compile(r'hello.*\!')

match = pattern.match(r'hello ! how are you! welcome~')

if match:
	print match.group()

