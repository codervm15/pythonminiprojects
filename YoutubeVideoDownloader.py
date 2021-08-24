# Here we download videos from youtube

from pytube import YouTube

link = input("Enter video link")
print("Downloading....")

YouTube(link).streams.first().download()

print("Video downloaded successfully")

