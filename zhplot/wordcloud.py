import os
from pathlib import Path


def wordcloud_chineseize():
    font_ttf: str = "NotoSansSC-Regular.ttf"
    os.environ["FONT_PATH"] = f"{Path(__file__).parent}/fonts/{font_ttf}"


wordcloud_chineseize()
