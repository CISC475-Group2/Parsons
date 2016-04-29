def tokenize(inputString):
	"""Convert String into list of tokens
	Input: String to be converted
	Output: List representation of input string
	"""
	return inputString.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(input):
	"""Read BSL+ program from string representation of program
		Input: String Representation of program
		Output:String representation of program delimited by the | symbol
		"""
	if len(input) == 0:
		raise SyntaxError('cannot parse empty string')
	if input.count('(') != input.count(')'):
		raise SyntaxError('unbalenced parens')
	else:
		returnList = []
		for line in input.split('\n'):
			returnList.append(parse_tokens(tokenize(line)))
		return  add_Dilimiter(returnList)


def parse_tokens(tokenizedInput):
	"""Parses single line in file, returning a list containing the parsed line
		Input: Tokenised Input of program
		Output: list containing parsed Line
		"""
	if len(tokenizedInput) ==0:
		raise SyntaxError('unexpected EOF while reading')
	else:
		token = tokenizedInput.pop(0)
		if token == '(':
			if len(tokenizedInput) == 0:
				raise SyntaxError('Found ublaenced parenthese')
			else:
				List= []
				while tokenizedInput[0] != ')':
					List.append(parse_tokens(tokenizedInput))
				tokenizedInput.pop(0)
				return List
		elif token == ')':
			raise SyntaxError("unexpected ) found")
		else:
			return str(token)

def add_Dilimiter(parsed_input):
	"""Adds delimiters to the parsed input for readability into blocks
		Input: parsed program
		Output: list contaning placeholders for locations of block insertion"""
	outputstring=""
	if type(parsed_input) == type([]):
		outputstring = outputstring + "( "
		for item in range(len(parsed_input)):
			outputstring= outputstring + "<nt> "
		outputstring = outputstring + ")|"
		for item in parsed_input:
			outputstring = outputstring + add_Dilimiter(item)
		return outputstring
	else:
		outputstring = parsed_input+"|"
		return outputstring


def convert_list(input_list,depth):
	output = []
	newDepth=depth+1
	output.append(input_list[depth].split())
	if  input_list[depth].count("<nt>") != 0:
		for i in range (0,input_list[depth].count("<nt>")):
			returnValue = convert_list(input_list,newDepth)
			output.append (returnValue[0])
			newDepth = returnValue[1]
		return [output, newDepth ]
	else:
		return [output,newDepth]



def read_parse_string_to_list(input_string):
	outList = input_string.split('|')
	del outList[-1]
	return convert_list(outList,0)[0]


def generate_parson_question(input_string):
    """ Given input racket solution string, we want to generate data for a Parson's Problem.
            Input: Racket string
            Output: list for Parsons's Problem."""
    return read_parse_string_to_list(parse(input_string))
