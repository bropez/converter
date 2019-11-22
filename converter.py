import os
from moviepy.editor import AudioFileClip
import datetime
from tqdm import tqdm


def get_baddies(dir):
	try:
		with open("{}/.comment_errors.txt".format(dir), "r") as file:
			data = file.read().splitlines()
	except OSError:
		data = []
		
	# print(data)
	return data
	


def conversion(dir):
	picture_dir = "{}/pictures".format(dir)
	sound_dir = "{}/sounds".format(dir)
	movie_dir = "{}/movies".format(dir)
	trash_list = get_baddies(dir)

	file_amount = 80

	# added the title
	audio_clip = AudioFileClip("{}/.title.mp3".format(sound_dir))
	audio_duration = audio_clip.duration + .20
	audio_duration = datetime.datetime.utcfromtimestamp(audio_duration)
	audio_clip.close()
	duration_format = audio_duration.strftime("%H:%M:%S.%f")

	command = "ffmpeg -hide_banner -loglevel panic -loop 1 -y -i {}/.title.png -i {}/.title.mp3 -t {} {}/.title.mp4".format(
		picture_dir, 
		sound_dir, 
		duration_format,
		movie_dir,
		)
	os.system(command)


	for number in tqdm(range(1, file_amount)):
		if str(number) in trash_list:
			continue
			
		audio_clip = AudioFileClip("{}/comment{}.mp3".format(sound_dir, number))
		audio_duration = audio_clip.duration + .20
		audio_duration = datetime.datetime.utcfromtimestamp(audio_duration)
		audio_clip.close()
		duration_format = audio_duration.strftime("%H:%M:%S.%f")
		
		command = "ffmpeg -hide_banner -loglevel panic -loop 1 -y -i {}/comment{}.png -i {}/comment{}.mp3 -t {} {}/comment{}.mp4".format(
		picture_dir, 
		number, 
		sound_dir, 
		number, 
		duration_format,
		movie_dir, 
		number
		)
		os.system(command)
		
	print("Your files have been converted")
	

if __name__ == '__main__':	
	directory = input("Where would you like to look: ")
	conversion(directory)
	