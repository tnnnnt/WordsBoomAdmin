# coding:utf-8
import asyncio
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import WordsBoomAdmin.public_data as pdt
from WordsBoomAdmin import asyncio_c
from WordsBoomAdmin.console import Console
from WordsBoomAdmin.my_system_tray_icon import MySystemTrayIcon


# 管理员登录界面类
class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setWindowIcon(pdt.icon)
        self.setWindowTitle("管理员登录")
        self.setWindowModality(Qt.ApplicationModal)  # 设置为应用程序级别的模态对话框
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # 始终在前面

        # 创建账号、密码标签和文本框以及登录按钮
        self.ql_account = QLabel("账号")
        self.qle_account = QLineEdit()
        self.ql_password = QLabel("密码")
        self.qle_password = QLineEdit()
        self.qpb_login = QPushButton("登录")

        # 设置字体
        self.ql_account.setFont(pdt.font0)
        self.qle_account.setFont(pdt.font0)
        self.ql_password.setFont(pdt.font0)
        self.qle_password.setFont(pdt.font1)
        self.qle_password.setEchoMode(QLineEdit.Password)
        self.qpb_login.setFont(pdt.font0)
        self.qpb_login.setDefault(True)

        # 创建水平布局和垂直布局，并将控件添加到布局中
        self.qhbl0 = QHBoxLayout()
        self.qhbl1 = QHBoxLayout()
        self.qvbl = QVBoxLayout(self)
        self.qhbl0.addWidget(self.ql_account)
        self.qhbl0.addWidget(self.qle_account)
        self.qhbl1.addWidget(self.ql_password)
        self.qhbl1.addWidget(self.qle_password)
        self.qvbl.addLayout(self.qhbl0)
        self.qvbl.addLayout(self.qhbl1)
        self.qvbl.addWidget(self.qpb_login)

        # 连接登录按钮的点击事件到登录方法
        self.qpb_login.clicked.connect(self.logining)

        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # 登录方法
    def logining(self):
        # 检查管理员账号和密码是否正确
        if asyncio.run(asyncio_c.check_admin_account(self.qle_account.text())) and asyncio.run(asyncio_c.check_admin_password(self.qle_password.text())):
            # 隐藏登录窗口，显示控制台和系统托盘图标
            self.hide()
            pdt.console = Console()
            pdt.my_system_tray_icon = MySystemTrayIcon()
            pdt.console.show()
            pdt.my_system_tray_icon.show()
        else:
            QMessageBox.critical(self, '错误', '账号或密码错误！')

    def closeEvent(self, event):
        QCoreApplication.instance().quit()
