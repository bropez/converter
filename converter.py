import os

if __name__ == '__main__':
	picture_dir = input("Where are your pictures located: ")
	sound_dir = input("Where are your sounds located: ")
	movie_dir = input("Where would you like your movies saved: ")
	max_comment = input("How many comments are there: ")

	for number in range(1, max_comment):
		command = "ffmpeg -loop 1 -y -i {}/comment{}.png -i {}/comment{}.mp3 -shortest {}/video{}.mov".format(
		picture_dir, 
		number, 
		sound_dir, 
		number, 
		movie_dir, 
		number
		)
		os.system(command)
	print("Your files have been converted")