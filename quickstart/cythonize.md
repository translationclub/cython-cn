# 使用静态类型提速

Cython 是 Python 编译器，这意味着无须改动即可编译原生 Python 代码（一些 Cython 尚不支持的语法会报错）。当然，为了优化核心代码，使用静态类型声明是很有帮助的。因为使用静态类型能够．．．

静态类型声明使用 ``cdef`` 关键字。

## 变量

如下纯 Python 代码：

```python
def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
```

使用 Cython 编译之后仅仅能获得 35% 的速度提升，但是添加一些静态类型声明将大有不同。

添加静态类型声明之后，代码如下：

```cython
def f(double x):
    return x**2-x

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
```

．．．

添加静态类型之后，相对于纯 Python 代码，有着 4 倍的速度提升。

## 函数
