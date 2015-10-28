#pyc文件生成
[生成单个pyc文件](http://blog.csdn.net/sislcb/article/details/4002414)

python就是个好东西，它提供了内置的类库来实现把py文件编译为pyc文件，这个模块就是 py_compile 模块。

使用方法非常简单，如下所示，直接在idle中，就可以把一个py文件编译为pyc文件了。(假设在windows环境下)


```
import py_compile

py_compile.compile(r'H:/game/test.py')
```

##实践
见 `_src\om2py2w\2wex0\main.pyc`
可以直接双击 main.pyc 运行 