# double push 
## 背景
双推是指把一个文件的修改，推到两个不同的 git 库中

* 一个是 github 本身的，默认的远程地址为 https://git.gitbook.com/yangshaoshun/omooc2py.git
* 一个是book 对应的库，远程地址为 https://github.com/yangshaoshun/OMOOC2py.git

默认使用 git push 命令会推到第一个地址，我们的任务是把第二个地址也加入进来。

最终的效果是一次推送，更新两个库。

## 安装
安装过 github desktop for mac

## 配置

~双推的折腾过程

1.找到 config 文件

- 问题：mac 下找不到 .git/config 文件

	- 使用cd 命令：可以进入该文件夹，虽然外面看不到
	- google 搜索：mac 下如何查看隐藏文件 —— 未尝试
	- textmate 编辑器：打开文件，有『查看隐藏文件夹』选项 —— 打开 config 文件进行编辑


2.编辑 config 文件

对照大妈给出的[双推教程](https://github.com/ZoomQuiet/OMOOC2py/issues/1)
修改 config 文件。内容有些许区别，手工加入 book 和 hub 标示的两块代码

```
[remote "book"]
    url = https://git.gitbook.com/[帐号]/[图书名].git
    fetch = +refs/heads/*:refs/remotes/origin/*
[remote "hub"]
    url = git@github.com:OpenMindClub/[图书名].git
    fetch = +refs/heads/*:refs/remotes/origin/*

```

3.回到仓库根目录测试

>由于之前一直使用 github for desktop 作为推送，命令行使用不熟又走了很多弯路。

- 直接进入 terminal ，输入git remote - v ，提示此目录下没有 git repo
	- 回头看提示，仓库根目录，五个字又视而不见了
	- cd 命令进入根目录 cd omooc2py
	- git remote -v，看到新加入的 book 和 hub


- 第一轮测试：修改了omooc2py/readme.md 文件

	- git add .
	- git commit -a -m”first test”
	- git push hub  （大妈的 git pu，是配置过简写了，又是一个小坑啊）提示输入用户名和密码，成功
	- git push book
		- 提示用户名和密码，失败；gitbook 认证失败，用户名或密码错误
		- 网页登陆发现由于以前单独注册过gitbook的原因，密码一栏为 no password，修改密码
	- 重试 git push book ，成功

- 打开浏览器，分别在 github 和 gitbook 查看修改的文件，提交成功（不容易啊）。

4.自动双推

- 修改 config 文件，删除之前加入的两块，直接在原有的自己账号的 origin 下，多加入 url 一栏即可

```
...
[remote "origin"]
    url = https://[用户名]:[口令]@git.gitbook.com/[帐号]/[图书名].git
    url = git@github.com:OpenMindClub/[图书名].git
    fetch = +refs/heads/*:refs/remotes/origin/*

```

- 再次测试，只需要简单的一次 git push ，成功，两处同时更新

## 体验

review 整个流程，在理解了什么是双推之后，一共两步

1. 编辑 config 文件
2. 加入 gitbook 对应的 url

当然中间有很多前提，整个历程走了很多弯路

1. 隐藏文件 .git/config
2. gitbook 的登录设置
3. 命令行操作 git

---
151018 10:11 仓促完成，记流水账，待修改




