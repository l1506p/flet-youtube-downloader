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
from api.pytube_api import audio_downloader

import emoji

YOUTUBE_URL = "https://www.youtube.com/watch?v="


class YtAudioDownload:
    def __init__(self, page, progress_ring, dir):
        self.page = page
        self.progress_ring = progress_ring
        self.dir = dir

    def downloader(self, e):
        try:
            self.progress_ring.visible = True
            self.progress_ring.update()
            title = e.control.data[1]
            global row_title
            if emoji.emoji_count(title) > 0:
                row_title = emoji.replace_emoji(title, replace="")
            elif "|" in title:
                row_title = title.replace("|", "")
            else:
                row_title = title
            audio_downloader(
                url_input=YOUTUBE_URL + e.control.data[0],
                output_path=self.dir.directory_path.value,
                file_name=row_title + ".mp4",
                page=self.page,
                e=e,
            )
            self.progress_ring.visible = False
            self.progress_ring.update()
        except (MembersOnly, VideoPrivate, VideoRegionBlocked, VideoUnavailable) as err:
            match err:
                case MembersOnly():
                    members_only_exception(page=self.page)
                    self.progress_ring.visible = False
                    self.progress_ring.update()
                case VideoPrivate():
                    video_private_exception(page=self.page)
                    self.progress_ring.visible = False
                    self.progress_ring.update()
                case VideoRegionBlocked():
                    video_region_blocked_exception(page=self.page)
                    self.progress_ring.visible = False
                    self.progress_ring.update()
                case VideoUnavailable():
                    video_unavailable_exception(page=self.page)
                    self.progress_ring.visible = False
                    self.progress_ring.update()
