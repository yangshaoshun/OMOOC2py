# Mydaily Tk 桌面版
>由于前期缺乏记录，现在只能按照印象一点点倒着记录折腾的过程，索引一下

## Tkinter


## 绑定回车键
bind

## 添加退出按钮
master.quit()


## 输入框 + Message 的实现

## StringVar 变量使用

## 输入框 + Text 的实现 

### Text 获取内容

text.insert()


> 参考大妈的demo 之后，发现的几个细节
- 文本框内新行有颜色提示，可以理解为告诉用户当前输入的内容是保存在这一行
- 输入框持续输入，新行依次往下移动；超过文本框纵向区域，自动移动到可视区域 

## 颜色提示

text.tag_config()
text.tag_add()

## 滚动条 + 可视区域

text.see(INDEX) 


