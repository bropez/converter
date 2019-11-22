"""Video Prep

A wrapper script that encapsulates converter.py, cropper.py, and naming.py.

This script requires that `time`, `sys`, and `tqdm` all be installed within the
Python environment you are running this script in.
"""


import time
import sys
from tqdm import tqdm

from converter import conversion
from naming import create_title
from cropper import open_in_paint, crop_it


def get_dir():
	"""Gets a directory from an argument in the command line or user input

	Args:
		None

	Returns:
		dir (str) - A directory to be used for all scripts
	"""
	if sys.argv[1]:
		dir = sys.argv[1]
		return dir
	
	dir = input("Where would you like to look: ")
	return dir


if __name__ == '__main__':
	directory = get_dir()
	time.sleep(3)
	
	for number in tqdm(range(1, 80)):
		name = 'comment{}.png'.format(str(number))
		
		open_in_paint(name)
		crop_it('{}/.comment_errors.txt'.format(directory), name, number)
		
	conversion(directory)
	create_title(directory)