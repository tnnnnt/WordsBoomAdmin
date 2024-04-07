# coding:utf-8
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
import WordsBoomAdmin.public_data as pdt


# 定义左键点击图标的处理函数
def left_act(reason):
    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    if reason == 3:
        pdt.console.showNormal()


# 定义系统托盘图标类
class MySystemTrayIcon(QSystemTrayIcon):  # 系统托盘图标类
    def __init__(self):
        super(MySystemTrayIcon, self).__init__()
        # 设置图标和提示信息
        self.setIcon(pdt.icon)
        self.setToolTip("单词弹弹弹管理端")

        # 创建右键菜单和退出动作
        self.qm = QMenu()
        self.qa_exit = QAction('退出')

        # 将退出动作添加到右键菜单中
        self.qm.addAction(self.qa_exit)
        self.setContextMenu(self.qm)

        # 连接退出动作的triggered信号到quit_app函数
        self.qa_exit.triggered.connect(self.quit_app)
        self.activated.connect(left_act)

    # 定义退出应用程序的函数
    def quit_app(self):
        # 隐藏系统托盘图标并退出应用程序
        self.setVisible(False)
        QCoreApplication.instance().quit()
