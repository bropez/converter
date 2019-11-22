"""naming script

This script writes a properly formatted description and title.

This file can also be imported as a module and contains the following
functions:
    * create_title - Creates formatted description and title
"""


def create_title(dir: str): 
    """Creates two files holding a description and title of a video

    Args:
        dir (str): The directory for the files to be saved in

    Returns:
        None
    """
    # read the ytdescription file
    # directory = "10.11.2019 - completed/submission3"
    desc_f = open("{}/.ytdescription.txt".format(dir), "r")
    print(desc_f.readline())
    desc_f.close()

    # ask and create new yttitle file
    yt_title = input("Title of Youtube video: ")
    title_f = open("{}/yttitle.txt".format(dir), "w")
    title_f.write("{} - r/AskReddit".format(yt_title))
    title_f.close()

if __name__ == '__main__':
    directory = "10.11.2019 - completed/submission3"
    create_title(directory)