from dataclasses import dataclass
from pathlib import Path

import matplotlib
from matplotlib import font_manager


@dataclass
class MatplotlibChineseize:
    font_name: str = "simhei"
    font_ttf: str = "simhei.ttf"

    def __post_init__(self):
        self.font_dir_path = Path(__file__).parent / "fonts"
        self.font_ttf_path = self.font_dir_path / self.font_ttf

    def setup(self):
        # Ref: https://github.com/uehara1414/japanize-matplotlib
        font_files = font_manager.findSystemFonts(fontpaths=[self.font_dir_path])
        for fpath in font_files:
            font_manager.fontManager.addfont(fpath)
        matplotlib.rc("font", family=self.font_name)


def matplotlib_chineseize():
    MatplotlibChineseize().setup()


matplotlib_chineseize()
