import os
import urllib
from proglog import ProgressBarLogger
import moviepy.editor as mp
from pytube import YouTube, Search
import pytube.request

pytube.request.default_range_size = 524288


class MyBarLogger(ProgressBarLogger):

    def __init__(self, prog_bar):
        super().__init__()
        self.last_message = ""
        self.previous_percentage = 0
        self.prog_bar = prog_bar

    def callback(self, **changes):
        # Every time the logger message is updated, this function is called with
        # the `changes` dictionary of the form `parameter: new value`.
        for parameter, value in changes.items():
            # print ('Parameter %s is now %s' % (parameter, value))
            self.last_message = value

    def bars_callback(self, bar, attr, value, old_value=None):
        # Every time the logger progress is updated, this function is called
        if "Writing audio" in self.last_message:
            percentage = (value / self.bars[bar]["total"]) * 100
            if percentage > 0 and percentage <= 100:
                if int(percentage) != self.previous_percentage:
                    self.previous_percentage = int(percentage)
                    # print(self.previous_percentage / 100)
                    self.prog_bar.value = self.previous_percentage / 100
                    self.prog_bar.color = "green"
                    self.prog_bar.update()
                    if self.prog_bar.value == 1.0:
                        self.prog_bar.color = "transparent"
                        self.prog_bar.update()


def search(input_value):
    videos_search = Search(input_value)
    return videos_search


def search_results(input_value):
    try:
        return search(input_value=input_value).results
    except urllib.error.URLError:
        pass


def video_downloader(url_input, output_path, file_name, page, on_progress, e):
    yt = YouTube(url_input, on_progress_callback=on_progress)
    yt.streams.filter(type="video").first().download(
        output_path=output_path,
        filename=file_name,
    )

    page.snack_bar.open = True
    page.update()


def audio_downloader(url_input, output_path, file_name, page, on_progress, prog_bar, e):
    yt = YouTube(url_input, on_progress_callback=on_progress)
    yt.streams.filter(type="audio").first().download(
        output_path=output_path,
        filename=file_name,
    )
    convert_mp4_to_mp3(file_path=output_path + "/" + file_name, prog_bar=prog_bar)
    page.snack_bar.open = True
    page.update()


def convert_mp4_to_mp3(file_path, prog_bar):
    clip = mp.AudioFileClip(file_path)
    new_file = os.path.splitext(file_path)[0] + ".mp3"
    logger = MyBarLogger(prog_bar=prog_bar)
    clip.write_audiofile(new_file, logger=logger)
    os.remove(file_path)
