from components.Dialog import alertDialog


def members_only_exception(page):
    alert_dialog = alertDialog(
        page=page,
        title="Members Only",
        content_text="Only Members able to download this video",
        color="red",
    )
    page.dialog = alert_dialog
    alert_dialog.open = True
    page.update()


def video_private_exception(page):
    alert_dialog = alertDialog(
        page=page,
        title="Private Video",
        content_text="Video is Privet unable to download",
        color="red",
    )
    page.dialog = alert_dialog
    alert_dialog.open = True
    page.update()


def video_region_blocked_exception(page):
    alert_dialog = alertDialog(
        page=page,
        title="Region Blocked",
        content_text="Unable to download this video in your region",
        color="red",
    )
    page.dialog = alert_dialog
    alert_dialog.open = True
    page.update()


def video_unavailable_exception(page):
    alert_dialog = alertDialog(
        page=page,
        title="Unavailable Video",
        content_text="Video Unavailable at this time.",
        color="red",
    )
    page.dialog = alert_dialog
    alert_dialog.open = True
    page.update()


def video_or_audio_exception(page):
    alert_dialog = alertDialog(
        page=page,
        title="Video or Audio Warning",
        content_text="Chose audio or video to download please!",
        color="blue",
    )
    page.dialog = alert_dialog
    alert_dialog.open = True
    page.update()
