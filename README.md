# Zh-Plot: Show Chinese in Figures with one line code

[![Python](https://img.shields.io/pypi/pyversions/zhplot.svg?color=%2334D058)](https://pypi.org/project/zhplot/)
[![PyPI](https://img.shields.io/pypi/v/zhplot?color=%2334D058&label=pypi%20package)](https://pypi.org/project/zhplot/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

[![Build Docs](https://github.com/shenxiangzhuang/zhplot/actions/workflows/build_docs.yaml/badge.svg)](https://github.com/shenxiangzhuang/zhplot/actions/workflows/build_docs.yaml)
[![Test](https://github.com/shenxiangzhuang/zhplot/actions/workflows/test.yaml/badge.svg)](https://github.com/shenxiangzhuang/zhplot/actions/workflows/test.yaml)
[![Codecov](https://codecov.io/gh/shenxiangzhuang/zhplot/branch/master/graph/badge.svg)](https://codecov.io/gh/shenxiangzhuang/zhplot)
[![GitHub License](https://img.shields.io/github/license/shenxiangzhuang/zhplot)](https://github.com/shenxiangzhuang/zhplot/blob/master/LICENSE)


## 快速开始

### 安装

使用pip安装`zhplot`:

```bash
pip install zhplot
```

### 使用方法

使用`zhplot`非常简单，只需在脚本开头导入即可:
```diff
+ import zhplot
import matplotlib.pyplot as plt
```

### 一个简单的例子
<div align="center">
    <img src="https://github.com/shenxiangzhuang/zhplot/blob/7569552e07a8b4de7afd8c9df5cbcb154a349e97/docs/images/zhplot_demo.png?raw=true" width="500"/>
</div>

```python
import zhplot
import matplotlib.pyplot as plt


plt.plot([1, 2, 3, 4])
plt.title('这是一个标题')
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.show()
```
