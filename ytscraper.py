from pytubefix import YouTube
from pytubefix.cli import on_progress
import pandas as pd

videos_df = pd.read_csv('videos_df.csv')
urls = videos_df['video_id']

for url in urls: 
    try:
        # Specify your desired download path
        download_path = "Videos" 

        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)

        # Get the highest resolution stream
        ys = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        ys.download(output_path=download_path)
    except:
        print(f"Failed to download {url}: {e}")