import requests


def check_connection(page):
    url = "https://www.youtube.com/"
    timeout = 2
    try:
        requests.get(url=url, timeout=timeout)
        return True
    except requests.ConnectionError as exception:
        page.banner.open = True
        page.update()
        return False
