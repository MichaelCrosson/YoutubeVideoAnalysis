from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=Lpk--3LH9Ck"

# Specify your desired download path
download_path = "C:/Users/nosso/OneDrive/Desktop" 

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Get the highest resolution stream
ys = yt.streams.get_highest_resolution()

# Download the video to the specified path
ys.download(output_path=download_path)
