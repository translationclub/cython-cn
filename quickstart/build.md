# 构建代码

Cython 代码必须编译（不同于 Python），Cython 编译分两个阶段：

* Cython 将 ``.pyx`` 文件编译为 ``.c`` 文件，containing the code of a Python extension module
* C 编译器将 ``.c`` 文件编译为可供 Python 直接引用使用的 ``.so``（Windows 上为 ``.pyd``）文件。

有多种方式可以构建 Cython 代码：

* 使用 distutils，编写 ``setup.py``
* 
* 
* 

当前 distutils 是最常用的构建 Cython 代码的方式，其他方式在 [Source Files and Compilation](http://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html#compilation) 有详细的描述。

## 使用 distutils 构建 Cython 模块

以　``Hello World`` 为例:

* ``hello.pyx``
  ```python
  def say_hello_to(name):
      print('Hello %s!' % name)
  ```
* 对应的 ``setup.py``
  ```python
  from distutils.core import setup
  from Cython.Build import cythonize

  setup(
      name = 'Hello',
      ext_modules = cythonize('hello.pyx'),
  )
  ```

运行 ``python setup.py build_ext --inplace`` 构建代码，编译生成的 ``hello.so`` 即可供 Python 直接引用使用

* 文件详情
  ```shell
  (cython) ~/Cython/cython-docs/build/hello$ ls
  build  hello.c  hello.pyx  hello.so  setup.py
  ```
* 使用示例
  ```python
  In [1]: from hello import say_hello_to

  In [2]: say_hello_to('Kimi.Huang')
  Hello Kimi.Huang!
  ```
