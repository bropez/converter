# converter

I realized that instead of importing two separate files (.png, .mp3) in Premiere Pro and syncing them up was much harder than just joining them together and importing one .mov file.

A simple script that joins a large list of .png files with .mp3 files of the same name into one .mov file of the same name.

## Installation
[FFmpeg](https://ffmpeg.org/download.html) will be needed as well as adding it to your ```Path``` environment variable.


## Usage
After getting the script into your desired directory, run the script and it will prompt you where the images are located, where the .mp3's are located, and where you would like your .mov's saved to.

![Picture of how to use converter.py](https://raw.githubusercontent.com/bropez/converter/master/converter_example.PNG)

Something to note is that the file names are hard coded along with how many times it will run.
