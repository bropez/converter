import pyautogui


def open_in_paint(name):
	joinlocation = pyautogui.locateOnScreen('search/100.png')
	joinpoint = pyautogui.center(joinlocation)
	joinx, joiny = joinpoint
	pyautogui.click(joinx, joiny)
	
	pyautogui.hotkey('ctrl', 'o')
	pyautogui.typewrite(name)
	pyautogui.press('enter')


def crop_it(directory, name, num):
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
