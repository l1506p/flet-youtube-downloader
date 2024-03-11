import os, sys
import urllib
import moviepy.editor as mp
from pytube import YouTube, Search
import pytube.request

pytube.request.default_range_size = 524288


def search(input_value):
    videos_search = Search(input_value)
    return videos_search


def search_results(input_value):
    try:
        return search(input_value=input_value).results
    except urllib.error.URLError:
        pass


def video_downloader(url_input, output_path, file_name, page, e):
    yt = YouTube(url_input)
    yt.streams.filter(type="video").first().download(
        output_path=output_path,
        filename=file_name,
    )

    page.snack_bar.open = True
    page.update()


def audio_downloader(url_input, output_path, file_name, page, e):
    yt = YouTube(url_input)
    yt.streams.filter(type="audio").first().download(
        output_path=output_path,
        filename=file_name,
    )
    convert_mp4_to_mp3(file_path=output_path + "/" + file_name)
    page.snack_bar.open = True
    page.update()


def convert_mp4_to_mp3(file_path):
    clip = mp.AudioFileClip(file_path)
    new_file = os.path.splitext(file_path)[0] + ".mp3"
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    clip.write_audiofile(new_file)
    os.remove(file_path)
