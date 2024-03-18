from pytube.exceptions import (
    MembersOnly,
    VideoPrivate,
    VideoRegionBlocked,
    VideoUnavailable,
)
from utils.exceptions import (
    members_only_exception,
    video_private_exception,
    video_region_blocked_exception,
    video_unavailable_exception,
)
from api.pytube_api import video_downloader

YOUTUBE_URL = "https://www.youtube.com/watch?v="


class YtVideoDownload:
    def __init__(self, page, dir, prog_bar):
        self.page = page
        self.dir = dir
        self.prog_bar = prog_bar

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size
        self.prog_bar.value = percentage_of_completion
        self.prog_bar.color = "green"
        self.prog_bar.update()
        if self.prog_bar.value == 1.0:
            self.prog_bar.color = "transparent"
            self.prog_bar.update()

    def downloader(self, e):
        try:
            video_downloader(
                url_input=YOUTUBE_URL + e.control.data[0],
                output_path=self.dir.directory_path.value,
                file_name=e.control.data[1] + ".mp4",
                page=self.page,
                on_progress=self.on_progress,
                e=e,
            )
        except (MembersOnly, VideoPrivate, VideoRegionBlocked, VideoUnavailable) as err:
            match err:
                case MembersOnly():
                    members_only_exception(page=self.page)
                case VideoPrivate():
                    video_private_exception(page=self.page)
                case VideoRegionBlocked():
                    video_region_blocked_exception(page=self.page)
                case VideoUnavailable():
                    video_unavailable_exception(page=self.page)
