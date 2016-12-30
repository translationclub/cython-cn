# 安装

[Anaconda](https://docs.continuum.io/anaconda/)、[Canopy](https://www.enthought.com/products/canopy/)、[Python(x,y)](http://www.pythonxy.com/)、[Sage](http://www.sagemath.org/)等科学计算包，已内置 Cython，无需额外安装。注意如果你使用的包内置的 Cython 太陈旧，你依然可以通过下文说明去升级 Cython。如无明确说明本文档适用于 ``Cython 0.11.2`` 及以后版本。

与绝大部分 Python 软件包不同，Cython 需要系统有 C 编译器。各系统安装 C 编译器方法如下：

* **Linux** 通常内置 ``GNU C Compiler (gcc)``，如若未内置，也可使用系统包很方便的安装。
  * Ubuntu or Debian
    ```shell
    sudo apt-get install build-essential
    ```
* **Mac OS X**
* **Windows**

## 源码安装
从 `` http://cython.org`` 下载最新版，解压文件，切换目录，然后执行：
```shell
python setup.py install
```

## PIP 安装
```shell
pip install Cython
```

## 临时编译
```shell
pip install Cython --install-option="--no-cython-compile"
```
