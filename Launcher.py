# 第一章 第一节 前言
# 欢迎打开 Era.js-SDK 示例程序源文件！
# 通过阅读本文件，你将学习到关于使用 Era.js 进行富文本游戏开发的一切！
# 本文件的文件名称为 `Launcher.py`，是游戏代码的总入口，本文件的第一行代码就是整个游戏的第一行代码。
# 那么本文件的第一行代码在哪里呢？是在第1行的名为“前言”（↖）的那家伙吗？
# 并不是。从本文件的第1行到第8行，都被称为`注释`，都以`#`号为一行开头。注释会被程序忽略掉，所以我无论在这里说什么都不会影响到程序的运行~
# 参见：[注释](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#comments)
# 另外，还有一件事情需要你提前知晓，整个教程都是真实的可以被运行起来的代码，推荐一边阅读源代码，一边打开程序进行对照。
# 你看见根目录的`Front.bat`文件了吗？双击打开，引擎的前端就会被启动，
# 然后再双击打开根目录下的`Debug.bat`代码就会运行起来啦！
# 如果你在学习的过程中需要重启游戏，那么在一般情况下，你只需要重启游戏后端。
# 这个方法可以节省你的时间哦~
# 言归正传，现在我们准备引入程序的第一行代码了！当当当当！
import erajs.api as a
# 这个语句十分简单，就是从`erajs`库中引入了`api`模块，并将其重命名为`a`，以方便以后调用。
# 引入完毕后，游戏引擎的全部 API 就已经可以使用了！
# 现在，请让我向你展示，引擎是如何使用的。
# 但在此之前，出于Python对于源代码的读取顺序的原因，我需要向你展示的代码被放在了本文件的末尾。
# 因此，请跳转至本文件的末尾，并寻找`第一章 第二节`的小标题，我会在那里等你，稍后见！
# ---------分割线：请跳转至文件末尾---------

# 第二章 第一节 一起设计一个有吸引力的游戏封面！
# 欢迎！我们又见面了！
# 刚才在1.2里，我们欣赏了游戏引擎的最简单形式，
# 但不得不说的是，如果仅仅是一个“孤零零的”，“不加任何修饰”的按钮放在第一个页面上，看起来总会让人有些不太满意。
# 没关系，我们在这一个小节里面学习制作一个常用的封面，
# 通过对这一节的学习，希望能使你学会游戏引擎的基础排版，和一些常用控件的使用。
# 那么我们开始吧！
# 你也许会好奇，我们在1.2中生成按钮的时候，引用了一个名为`cover`的`界面函数`，那是什么呢？
# 是这样的，我们可以简单的把一个`函数`理解为`被打包起来的几行代码`，
# 那么在Era.js引擎里，我们意识到`函数里面的几行代码`与`界面里面的几个控件`具有一定的相似性。
# 因此，我们在这个的基础上进行了最基本的抽象，这也是Era.js引擎的关键理念之一：
# 函数≈界面，一个函数≈一个界面，因此我们在这里约定：代表一个界面的函数就被称为`界面函数`。
# 很重要哦~ 要记牢。这会方便我们在后续的开发过程中进行抽象，加速开发。
# 好了，现在让我们请出刚才在文末引用了，却不知道究竟在哪儿定义的界面函数：cover！


def cover():
    # 函数的定义十分简单，一目了然，我就不赘述了。丢一个参考链接吧：
    # 参见：[定义函数](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions)
    # 函数定义好后，就能够被引用了！下面我们来往里面填充内容吧！
    a.title('Dev Guide with Era.js v{}'.format(a.version))
    # 首先，这是名为title的API，它的作用也特别直白：设置游戏窗口标题。
    # 标题就是括号里面的内容，但为什么会使用format函数呢？是因为我们要往字符串中塞入一个代表版本的变量。
    # 参见：[字符串函数](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format)
    # 参见：[格式字符串语法](https://docs.python.org/zh-cn/3/library/string.html#formatstrings)
    # 现在，我们新建一个页面，将原来的单按钮顶下去！
    a.page()
    # 这是名为page的API，作用是新建一个页面，之后的所有控件都在新的页面中生成。
    # 引擎只会显示最新的一个页面，旧的页面会被模糊掉，但不会模糊得十分彻底，而是能够让人勉强看清，以免玩家错过关键信息。
    # 接下来就轮到调整页面版式了！
    # 在默认情况下，页面中的内容都是左对齐的，但这种排布方式不一定都美观，因此我们在这里改变一个排版方式：
    a.mode('grid', 1)
    # 这是名为mode的API负责改变页面排版方式。
    # 在这里，我们将排版方式改为了“grid”(网格)，并且给了他一个参数“1”。
    # 则代表我们将排版模式变成了一个一列网格。
    # 而且网格有一个比较重要的特点，就是在网格中的对齐方式都是居中对齐
    # 这样，我们通过生成一个一列网格来实现了每行居中的功能。
    # 现在，让我们往网格里面装东西吧！
    a.t()
    # 噫？这是装了个什么东西？
    # 这就是传说中的最常用、最有用、最好用的控件——文本控件！
    # 而如果我们不往里面装文本的话（比如现在这个），会发生什么？
    # 答案是换行（换档）！
    # 什么意思呢？比如如果我们的排版模式是`line`，那么执行这个语句，就相当于回车键，
    # 后续的内容都会在下一行进行显示。
    # 而如果我们的排版模式是`grid`，这里我们以三列网格为例，执行这个语句，我们的光标就会从第一行第一个单元格，跳转到第二个单元格。
    # 而如果我们的光标本来就在第一行的第三个单元格，那么执行之后就会跳转到第二行的第一个单元格。
    # 而在这里，我们在一列网格中使用，作用就是从第一行第一个单元格，跳转到第二行第一个单元格，也就意味着换了一行而已。
    # 都是为了美观呀！美观！
    # 好了，终于可以开始装东西了，来！
    a.h('Era.js 开发向导')
    # 这是标题，用法很简单就不赘述了，我们换行
    a.t()
    # 再显示一行文字。
    a.t('Version: {}'.format(a.version))
    # 这里语法与title一样，都是进行了字符串格式化。没有什么特别值得说的东西。
    # 接下来，我们进行几次换行
    for _ in range(4):
        a.t()
    # 一行行换行毕竟太麻烦，这里我们使用循环进行5次换行。再生成控件的话，就会在比较靠下的地方了。
    a.b('　　页面逻辑教程　　', a.goto, ui_logic)
    a.t()
    a.t()
    a.b('　　　控件教程　　　', a.goto, ui_widgets)
    a.t()
    a.t()
    a.b('　　　排版教程　　　', a.goto, ui_mode)
    a.t()
    a.t()
    a.b('　　　数据教程　　　', a.goto, ui_data)
    a.t()
    a.t()
    a.b('　　代码组织教程　　', a.goto, ui_code)
    a.t()
    a.t()
    a.b('　　 ＭＯＤ教程 　　', a.goto, ui_mod)
    a.t()
    a.t()
    a.b('　　　退出教程　　　',  a.exit)
    a.t()


def ui_logic():
    def change_page(page):
        # 在这里定义一个简单的换页逻辑
        a.clear(1)  # 从引擎的界面逻辑中去除掉当前的页面
        a.goto(page)  # 进入一个新页面，该页面与原页面属于兄弟节点

    def page1():
        # 当一个子页面完全只属于一个父页面而不需要被其他页面调用时，
        # 可以将象征这个子页面的函数（如：page1）放在父函数（ui_gui_logic）内。
        a.page({'background-color': '#434648'})  # 新建一个红色页面
        a.h('第一页（暨页面着色演示）')
        a.t()
        a.b('返回', a.back)
        a.b('下一页', change_page, page2)
        a.b('回到主界面', a.back, num=2)  # 向 back 传递参数 num，可以指定返回到第几个父节点。

    def page2():
        a.page({'background-color': '#535659'})  # 新建一个页面
        a.h('第二页（暨页面着色演示）')
        a.t()
        a.b('返回', a.back)
        a.b('上一页', change_page, page1)
        a.b('下一页', change_page, page3)
        a.b('回到主界面', a.back, num=2)

    def page3():
        a.page({'background-color': '#636669'})  # 新建一个页面
        a.h('第三页（暨页面着色演示）')
        a.t()
        a.b('返回', a.back)
        a.b('上一页', change_page, page2)
        a.b('回到主界面', a.back, num=2)
    a.page()
    a.h('页面逻辑展示')
    a.t()
    a.b('第一页', a.goto, page1)
    a.b('第二页', a.goto, page2)
    a.b('第三页', a.goto, page3)
    a.b('刷新', a.repeat)  # 当您需要刷新当前界面以显示某些游戏数据的变化时，请用这个方法。
    a.b('返回', a.back)
    a.t()
    a.b('清屏（慎用（请在使用时组合其他界面逻辑））', a.cls)


def ui_widgets():
    pass


def ui_mode():
    pass


def ui_data():
    pass


def ui_code():
    pass


def ui_mod():
    pass


# ---------分割线---------
# 第一章 第二节 最简单的页面有多简单？
# 欢迎回来！现在请让我向你展示一个最简单的界面！请看好：
a.init()
a.b('进入向导', cover)
# 完成！
# 怎样？是不是觉得特别简单？确实就是如此简单！
# 这两行代码做的事情很简单：
# 1. 引擎初始化；
# 2. 生成一个文字为`进入向导`，且点击之后就会进入`cover`页面函数的`按钮`。
# 是不是特别直白？这也是游戏引擎 API 设计时十分注重的点。
# 在这里，`b`是`button`的别名，你可以用button来代替b，效果是一样的。试试看？
# `b`和`button`具有同样的效果，但本引擎`推荐`都使用缩写，
# 因为在以后的开发过程中，h(标题,heading)、t(文本,text)、b(按钮,button)和l(链接,link)都是日常最频繁使用的元素，
# 适当的缩写可以提高代码中有效信息的密度，且不会被大量令人眼花的文字给看晕。
# 而关于init这个API呢，做的事情很复杂，你可以仔细看看后端究竟输出了什么，会让你对初始化的流程有一个基本的认识。我们会以后再聊。
# 好了，这就是最简单的界面了，你看看前端，是不是有一个可爱的小按钮出现呢？
# 点击它，我们出发去往第二章，第二章的源代码在当初`第一章 第一节`的后面。
# 我们在那儿碰面！
