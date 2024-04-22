import requests


def download_obj(download_url):
    """画像をダウンロードする

    Args:
        download_url (str): 画像のURL

    Returns:
        bytes: 画像データ、ダウンロードに失敗した場合はNone
    """
    img_data = requests.get(
        download_url,
        stream=True,
    ).content

    if len(img_data) > 0:
        return img_data
    else:
        return None
