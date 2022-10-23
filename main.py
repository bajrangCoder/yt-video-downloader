'''
Author:@bajrangCoder
'''
from pytube import YouTube
from pathlib import Path
import os

file_size = 0

def main():
    print("\n\tWelcome to YouTube video Downloader!\n")
    url = str(input("Enter video url: "))
    if url == None:
        print("Enter valid url!")
    else:
        download_video(url)

def download_video(url):
    try:
        video = YouTube(url, on_progress_callback=progress_check)
    except:
        print("ERROR! Check your url and connection, Try Again...")
    
    video_type = video.streams.filter(file_extension='mp4').get_highest_resolution()
    title = video.title
    print(f"Fetching: {format(title)}")
    global file_size
    file_size = video_type.filesize
    if video_type.exists_at_path(file_path()):
        print("File already exists.")
        return
    video_type.download(file_path())
    print("Download complete!")

def progress_check(chunk, file_handle, bytes_remaining):
    remaining = (100 * bytes_remaining) / file_size
    percent = 100 - int(remaining)
    print(f"Downloading: {percent}%")

def file_path():
    home = Path.home()
    download_path = os.path.join(home, 'Videos')
    return download_path

if __name__ == "__main__":
    main()
