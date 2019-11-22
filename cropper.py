"""Picture Cropping

This script uses mspaint to crop a specific comment out of a
picture of a reddit post. It then opens the next picture in the 
directory and does the same.

This script requires that `pyautogui` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:
	* open_in_paint	- Opens the given file in mspaint
	* crop_it		- Crops the reddit comment out of the entire image
"""


import pyautogui


def open_in_paint(name: str):
	"""Opens a specific file in mspaint

	Args:
		name (str):			The filename that needs to be opened next

	Returns:
		None
	"""
	joinlocation = pyautogui.locateOnScreen('search/100.png')
	joinpoint = pyautogui.center(joinlocation)
	joinx, joiny = joinpoint
	pyautogui.click(joinx, joiny)
	
	pyautogui.hotkey('ctrl', 'o')
	pyautogui.typewrite(name)
	pyautogui.press('enter')


def crop_it(directory: str, name: str, num: int):
	"""Crops the wanted comment out of the reddit post image

	Args:
		directory (str):	The directory that the .comment_errors.txt should be saved in
		name (str):			The name of the file the .png should be saved under
		num (int):			The id of the photo
	"""
	joinlocation = pyautogui.locateOnScreen('search/100.png')
	joinpoint = pyautogui.center(joinlocation)
	joinx, joiny = joinpoint
	pyautogui.click(joinx, joiny)
	
	selectlocation = pyautogui.locateOnScreen('search/select.png')
	try:
		selpoint = pyautogui.center(selectlocation)
	except TypeError:
		# print("check {}, select tool error".format(name))
		f = open(directory, 'a')
		f.write('\n')
		# f.write("Check comment {}, select tool error".format(name))
		f.write("{}".format(str(num)))
		f.close()
		return
		
	selx, sely = selpoint
	pyautogui.click(selx, sely)
	
	topleftlocation = pyautogui.locateOnScreen('search/top_left.png')
	bottomrightlocation = pyautogui.locateOnScreen('search/bottom_right.png')

	try:
		tlpoint = pyautogui.center(topleftlocation)
	except TypeError:
		# print("check comment {}, top left error".format(str(num)))
		f = open(directory, 'a')
		f.write('\n')
		# f.write("Check comment {}, top left error".format(str(num)))
		f.write("{}".format(str(num)))
		f.close()
		return
		
	try:
		brpoint = pyautogui.center(bottomrightlocation)
	except TypeError:
		# print("check {}, bottom right error".format(name))
		f = open(directory, 'a')
		f.write('\n')
		# f.write("Check comment {}, bottom right error".format(name))
		f.write("{}".format(str(num)))
		f.close()
		return
	tlx, tly = tlpoint
	brx, bry = brpoint

	pyautogui.moveTo(tlx, tly)
	pyautogui.mouseDown(button='left')
	pyautogui.mouseUp(button='left', x=brx, y=bry)
	
	pyautogui.hotkey('ctrl', 'shift', 'x')
	pyautogui.hotkey('ctrl', 's')
	
	
if __name__ == '__main__':
	directory = input("Where would you like to look: ")
	
	for number in tqdm(range(1, 80)):
		name = 'comment{}.png'.format(str(number))
		
		open_in_paint(name)
		crop_it('{}/.comment_errors.txt'.format(directory), name, number)
