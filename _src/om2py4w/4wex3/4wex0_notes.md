# 4wex0_notes

## 测试
大妈的视频中的代码，一一测试，理解大致的原理。
从简单的 hello.world 开始

route：指的是接入的页面
每个 route 下面，有个用来执行的函数代码，有展示内容，有提交内容
由不同的 method 用来区分

网页中展示函数的返回值

最终main.py 的基础模板为
```
# -*- coding: utf-8 -*-
from bottle import * 

@route('/')


if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)
```

---

[大妈当年的用 bottle 写 todolist 的代码](https://bitbucket.org/ZoomQuiet/bottle-simple-todo/src)
[官方教程](https://github.com/myzhan/bottle-doc-zh-cn/blob/master/docs/tutorial_app.rst)

Bottle内置了独创的模板引擎。模板是后缀名为 .tpl 的文本文件。模板的内容混合着HTML标签和Python语句，模板也可以接受参数。

以%开头的行被当作Python代码来执行。请注意，只有正确的Python语句才能通过编译，要不模板就会抛出一个异常。除了Python语句，其它都是普通的HTML标记。

如果想要在不以%开头的行中访问变量，则需要把它放在两个大括号中间。这告诉模板，需要用变量的实际值将其替换掉。
{{...}}打印出Python语句的结果.

---

request.Get.get()  干嘛使的