# a3py

[English](README.md) | 简体中文

`a3py`是一个Python工具包。

## 1. 简介

### 简化的

* 变量命名风格转换
* 日期时间转换
* 环境变量
* hash库

### 改良的

* 更快的json（使用ujson）
* 易读的

### 实践经验的

* 动态
* 并发

## 2. 使用

### 安装

```shell script
pip install a3py

```

### 样例

```python
from datetime import date
from a3py.simplified.datetime import date2str
from a3py.improved.json import fast_dumps
from a3py.improved.readable import get_readable_size


if __name__ == "__main__":
    assert date2str(date(2019, 10, 3)) == "2019-10-03"
    assert fast_dumps([1, 2, 3]) == "[1,2,3]"
    assert get_readable_size(1024 * 1024) == "1.0MB"

```
