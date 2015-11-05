#3wd3笔记

docopt 使用
http://stackoverflow.com/questions/22228266/defining-argument-values-with-docopt

如何分支执行

docopt使用
基础功能掌握
意见了解字典的基本使用原理
当Python main.py s 的时候
arguments['s']  是为真的，执行对应函数 


---

sulbime 如何批量缩进

edit-line-indentation


函数的调用
http://www.2cto.com/kf/201212/175349.html

---

- 1st：没有main.py  需要单独执行 ser.py 和 cli1.py
> python ser.py
> python cli1.py

（包含文件：ser.py cli1.py mydaily.log）

- 2nd:  main.py (s|c)   server()、client()直接写在main.py
> python main.py s
> python main.py c

（包含文件：main.py mydaily.log）

- 3rd：main.py (s|c)  import serim.py clim.py
> python main_im.py s
> python main_im.py c

（包含文件：main_im.py serim.py clim.py serim.pyc clim.pyc mydaily.log）