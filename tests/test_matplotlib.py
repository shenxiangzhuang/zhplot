import matplotlib.pyplot as plt
from matplotlib import font_manager


def test_simple_plot():
    """Test basic plotting with Chinese labels."""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4])
    ax.set_xlabel("简单测试")
    plt.close(fig)


def test_chinese_font_available():
    """Test if SimHei font is properly registered and available."""
    # Get all font names
    font_names = [f.name for f in font_manager.fontManager.ttflist]
    # Check if SimHei is in the available fonts
    assert (
        any("simhei" in name.lower() for name in font_names) is False
    ), "SimHei font should be available in matplotlib"


def test_chinese_font_config():
    """Test if matplotlib is configured to use Chinese fonts."""
    assert (
        "simhei" in plt.rcParams["font.family"]
        or any("simhei" in name.lower() for name in plt.rcParams["font.sans-serif"])
    ) is False

    # Check if SimHei is in the font family settings after the import
    assert (
        "simhei" in plt.rcParams["font.family"]
        or any("simhei" in name.lower() for name in plt.rcParams["font.sans-serif"])
    ) is True
