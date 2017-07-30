from PIL import Image
from getalpha import load_quarters
import random
import sys


OFFSET = 14

OPT = {
	'single': False,
	'debug': False,
	'calibration_values': False,
	'early_chars': False,
	'char_width': 8,
	'char_height': 16,
	'reduction': 750,
	'input_file': 'input.png',
	'calibration_file': 'alpha.png'
}


def dist(tup1, tup2):
	'''Get the distance (squared) between two four dimensional vectors'''
	return (tup1[0] - tup2[0]) ** 2 + (tup1[1] - tup2[1]) ** 2 + \
		   (tup1[2] - tup2[2]) ** 2 + (tup1[3] - tup2[3]) ** 2


def generate(alpha, input_file, char_width, char_height, quartered):
	'''
	Generate the ASCII image

	alpha - dictionary mapping characters to values
	input_file - file to convert
	char_width - amount of pixels horizontally to convert into a single character
	char_height - amount of pixels vertically to convert into a single character
  	quartered - whether to use four values per character
	'''
	image = Image.open(input_file)
	output = ''
	image_width, image_height = image.size
	if image_width % char_width: exit('Character width is not a factor of image width')
	if image_height % char_height: exit('Character height is not a factor of image height')

	for y in range(image_height // char_height):
		for x in range(image_width // char_width):
			if quartered:
				tl = get_value(image,
						x * char_width, y * char_height,
						char_width / 2, char_height / 2) // OPT['reduction']
				tr = get_value(image,
						x * char_width + char_width / 2, y * char_height + char_height / 2,
						char_width / 2, char_height / 2) // OPT['reduction']
				bl = get_value(image,
						x * char_width, y * char_height + char_height / 2,
						char_width / 2, char_height / 2) // OPT['reduction']
				br = get_value(image,
						x * char_width + char_width / 2, y * char_height + char_height / 2,
						char_width / 2, char_height / 2) // OPT['reduction']

				value = (tl, tr, bl, br)
			else:
				value = get_value(image,
						x * char_width, y * char_height,
						char_width, char_height)

			output += nearest_char(alpha, value)
		output += '\n'
	return output


def nearest_char(alpha, input):
	'''Get the character that has the value nearest to the input'''
	quartered = type(input) == tuple
	best = None

	for char, white in sorted(alpha.items(), key=lambda x: random.random()):
		if quartered:
			v = dist(white, input)
		else:
			v = abs(white - input)

		if best is None or best[1] > v:
			best = (char, v)
	if OPT['debug']:
		print('{} {} -> {}, {}'.format(input, alpha[best[0]], best[1], best[0]))
	return best[0]


def get_value(image, x, y, w, h):
	'''Get the amount of white pixels at a given area of the image'''
	total = 0
	is_rgb = False
	for j in range(h):
		for i in range(w):
			value = image.getpixel((x + i, y + j))
			if is_rgb or value > 1:
				total += value - 125
				is_rgb = True
			else:
				total += value
	if OPT['debug']:
		print(total)
	return total


def calibrate(calibration_file, char_width, char_height, image_width, image_height, quartered, early_chars):
	'''
	Load an image of characters, find their values
	one by one and create a dictionary that maps
	characters to values.

	calibration_file - list of characters # 15 - 128
	char_width - width (pixels) of each character
	char_height - height (pixels) of each character
	image_width - number of characters in a row
	image_height - number of characters in a column
	quartered - whether to use four values per character
	early_chars - whether to include characters below # 32
	'''
	image = Image.open(calibration_file)
	output = {' ': 0}
	if quartered:
		output[' '] = (0, 0, 0, 0)
	for image_y in range(image_height):
		for image_x in range(image_width):
			# windows can show many of the 'early chars' (from 14 to 32)
			# mac by default cannot
			if early_chars or image_y * char_width + image_x + OFFSET > 32:
				if quartered:
					# get values for the four quarters of the character,
					# and place them in a tuple
					tl = get_value(image,
							image_x * char_width, image_y * char_height, # x, y
							char_width / 2, char_height / 2) # w, h
					tr = get_value(image,
							image_x * char_width + char_width / 2, image_y * char_height,
							char_width / 2, char_height / 2)
					bl = get_value(image,
							image_x * char_width, image_y * char_height + char_height / 2,
							char_width / 2, char_height / 2)
					br = get_value(image,
							image_x * char_width + char_width / 2, image_y * char_height + char_height / 2,
							char_width / 2, char_height / 2)
					value = (tl, tr, bl, br)
				else:
					# get a single value for the entire character
					value = get_value(image, image_x * char_width, image_y * char_height, char_width, char_height)
				# save the character's value to the output
				output[chr(image_y * char_width + image_x + OFFSET)] = value
	return output

def char_values(alpha):
	'''Print each character and its value(s)'''
	for char in alpha:
		print('[ {} ] {}'.format(char, alpha[char]))


def print_help(script_name):
	'''Print the help string'''
	print('Usage: ./python {0} [args] \n'.format(script_name))
	print('\t-h --help\t\tPrint this help text')
	print('\t-s\t\tGenerate using 1 value per character instead of 4.')
	print('\t-W\t\tWidth of rect to generate a character from. (default: {})'.format(OPT['char_width']))
	print('\t-H\t\tHeight of rect to generate a character from (default: {})'.format(OPT['char_height']))
	print('\t-r\t\tFactor to reduce the white values by. (default: {})'.format(OPT['reduction']))
	print('\t-f\t\tInput file (default: {})'.format(OPT['input_file']))
	print('\t-c\t\tFile to calibrate white values from (default: {})'.format(OPT['calibration_file']))
	print('\t-d\t\tPrint debug info when generating ASCII')
	print('\t-o\t\tOutput calibration white values rather than an ASCII image')
	print('\t-e\t\tAllow for extra characters that many terminals can\'t show')

if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
		print_help(sys.argv[0])
		exit()

	for i in range(len(sys.argv)):
		arg = sys.argv[i]
		if arg.startswith('-'):
			# toggles
			if 's' in arg:
				OPT['single'] = True
			if 'd' in arg:
				OPT['debug'] = True
			if 'o' in arg:
				OPT['calibration_values'] = True
			if 'e' in arg:
				OPT['early_chars'] = True
			# other options, must be split
			if 'W' in arg:
				OPT['char_width'] = int(sys.argv[i + 1])
			elif 'H' in arg:
				OPT['char_height'] = int(sys.argv[i + 1])
			elif 'r' in arg:
				OPT['reduction'] = int(sys.argv[i + 1])
			elif 'c' in arg:
				OPT['calibration_file'] = sys.argv[i + 1]
			elif 'f' in arg:
				OPT['input_file'] = sys.argv[i + 1]

	# TODO: allow configuration of calibration sizes
	alpha = calibrate(OPT['calibration_file'], 8, 16, 8, 14, not OPT['single'], OPT['early_chars'])

	if OPT['calibration_values']:
		print(char_values(alpha))
	else:
		print(generate(alpha, OPT['input_file'], OPT['char_width'], OPT['char_height'], not OPT['single']))
