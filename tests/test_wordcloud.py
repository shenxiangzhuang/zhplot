import os

import zhplot  # noqa


def test_chinese_font_config():
    """Test if wordcloud is configured to use Chinese fonts."""
    font_path_env = os.getenv("FONT_PATH")
    assert font_path_env is not None
    assert "NotoSansSC-Regular" in font_path_env
