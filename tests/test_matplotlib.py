import matplotlib.pyplot as plt

import zhplot  # noqa


def test_chinese_font_config():
    """Test if matplotlib is configured to use Chinese fonts."""
    # Check if SimHei is in the font family settings after the import
    assert (
        "Noto Sans SC" in plt.rcParams["font.family"]
        or any("Noto Sans SC" in name.lower() for name in plt.rcParams["font.sans-serif"])
    ) is True
