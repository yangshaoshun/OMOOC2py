# OMOOC.py 周任务代码试作

## 4w

### 程序说明

4wex0 文件夹内文件说明
+ bottle.py 使用的bottle框架
+ main.py 服务器端
+ CLI.py 客户端
+ input.tpl 输入模板
+ history.tpl 历史模板
+ mydaily.log 日记文件

### 使用说明
+ `python main.py` 运行服务器
+ 浏览器地址栏输入 *http://localhost:8080* ，写单行日记和查看历史纪录
+ 在另一个终端 `python CLI.py` 运行客户端，可打印历史纪录，输入新日记，操作同 `3wex0`


---
### 本周任务完成情况
####完成
+ 使用bottle框架，完成作业要求的基本日记功能
+ 使用requests，在命令行实现兼容 3W Net 作业

####未完成
+ 扩展模板 jinja2
+ 应用 bootstrap 框架
+ 使用数据库存储日记


---
### 大妈给出的向导
- 私人笔记:
    + SAE 发布服务
    + web 页面端口
    + 用户认证