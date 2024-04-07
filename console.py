# coding:utf-8
import asyncio
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout, QLineEdit, QMessageBox
import public_data as pdt
import asyncio_c


# 管理端控制台类
class Console(QWidget):
    def __init__(self):
        super(Console, self).__init__()
        self.setWindowIcon(pdt.icon)
        self.setWindowTitle("单词弹弹弹管理端")

        self.contribute_phone = ""
        self.contribute_word = ""
        self.contribute_mnemonic = ""
        self.feedback_id = -1
        self.feedback_phone = ""
        self.feedback_timestamp = ""
        self.feedback_content = ""

        self.qvbl0 = QVBoxLayout()
        self.ql_phone = QLabel("手机号")
        self.qle_phone = QLineEdit()
        self.ql_new_phone = QLabel("新手机号")
        self.qle_new_phone = QLineEdit()
        self.ql_max_favorites = QLabel("最大收藏数")
        self.qle_max_favorites = QLineEdit()
        self.ql_phone.setFont(pdt.font0)
        self.qle_phone.setFont(pdt.font0)
        self.qle_phone.setValidator(QRegExpValidator(QRegExp("[0-9]{11}")))
        self.ql_new_phone.setFont(pdt.font0)
        self.qle_new_phone.setFont(pdt.font0)
        self.qle_new_phone.setValidator(QRegExpValidator(QRegExp("[0-9]{11}")))
        self.ql_max_favorites.setFont(pdt.font0)
        self.qle_max_favorites.setFont(pdt.font0)
        self.qle_max_favorites.setValidator(QRegExpValidator(QRegExp("[0-9]{9}")))
        self.qgl0 = QGridLayout()
        self.qgl0.addWidget(self.ql_phone, 0, 0)
        self.qgl0.addWidget(self.qle_phone, 0, 1)
        self.qgl0.addWidget(self.ql_new_phone, 1, 0)
        self.qgl0.addWidget(self.qle_new_phone, 1, 1)
        self.qgl0.addWidget(self.ql_max_favorites, 2, 0)
        self.qgl0.addWidget(self.qle_max_favorites, 2, 1)
        self.qvbl0.addLayout(self.qgl0)

        self.qpb_create_account = QPushButton("创建账号")
        self.qpb_del_account = QPushButton("销毁账号")
        self.qpb_search_account = QPushButton("查询账号")
        self.qpb_reset_password = QPushButton("重置密码")
        self.qpb_reset_max_favorites = QPushButton("重置最大收藏数")
        self.qpb_reset_phone = QPushButton("改绑手机号")
        self.qpb_create_account.setFont(pdt.font0)
        self.qpb_del_account.setFont(pdt.font0)
        self.qpb_search_account.setFont(pdt.font0)
        self.qpb_reset_password.setFont(pdt.font0)
        self.qpb_reset_max_favorites.setFont(pdt.font0)
        self.qpb_reset_phone.setFont(pdt.font0)
        self.qgl1 = QGridLayout()
        self.qgl1.addWidget(self.qpb_create_account, 0, 0)
        self.qgl1.addWidget(self.qpb_del_account, 0, 1)
        self.qgl1.addWidget(self.qpb_search_account, 1, 0)
        self.qgl1.addWidget(self.qpb_reset_password, 1, 1)
        self.qgl1.addWidget(self.qpb_reset_max_favorites, 2, 0)
        self.qgl1.addWidget(self.qpb_reset_phone, 2, 1)
        self.qvbl0.addLayout(self.qgl1)

        self.qvbl1 = QVBoxLayout()
        self.ql_contribute_phone = QLabel()
        self.ql_contribute_word = QLabel()
        self.ql_contribute_phone.setFont(pdt.font0)
        self.ql_contribute_word.setFont(pdt.font0)
        self.qhbl0 = QHBoxLayout()
        self.qhbl0.addWidget(self.ql_contribute_phone)
        self.qhbl0.addWidget(self.ql_contribute_word)
        self.qvbl1.addLayout(self.qhbl0)

        self.ql_contribute_mnemonic = QLabel()
        self.ql_contribute_mnemonic.setFont(pdt.font0)
        self.ql_contribute_mnemonic.setMaximumHeight(400)
        self.ql_contribute_mnemonic.setWordWrap(True)
        self.qvbl1.addWidget(self.ql_contribute_mnemonic)

        self.qpb_change_mnemonic = QPushButton("换一个助记")
        self.qpb_del_mnemonic = QPushButton("删除助记")
        self.qpb_change_mnemonic.setFont(pdt.font0)
        self.qpb_del_mnemonic.setFont(pdt.font0)
        self.qhbl1 = QHBoxLayout()
        self.qhbl1.addWidget(self.qpb_change_mnemonic)
        self.qhbl1.addWidget(self.qpb_del_mnemonic)
        self.qvbl1.addLayout(self.qhbl1)

        self.ql_feedback_id = QLabel()
        self.ql_feedback_phone = QLabel()
        self.ql_feedback_timestamp = QLabel()
        self.ql_feedback_id.setFont(pdt.font0)
        self.ql_feedback_phone.setFont(pdt.font0)
        self.ql_feedback_timestamp.setFont(pdt.font0)
        self.qhbl2 = QHBoxLayout()
        self.qhbl2.addWidget(self.ql_feedback_id)
        self.qhbl2.addWidget(self.ql_feedback_phone)
        self.qhbl2.addWidget(self.ql_feedback_timestamp)
        self.qvbl1.addLayout(self.qhbl2)

        self.ql_feedback_content = QLabel()
        self.ql_feedback_content.setFont(pdt.font0)
        self.ql_feedback_content.setMaximumHeight(400)
        self.ql_feedback_content.setWordWrap(True)
        self.qvbl1.addWidget(self.ql_feedback_content)

        self.qpb_read_feedback = QPushButton("已读")
        self.qpb_read_feedback.setFont(pdt.font0)
        self.qvbl1.addWidget(self.qpb_read_feedback)

        self.qhbl = QHBoxLayout(self)
        self.qhbl.addLayout(self.qvbl0)
        self.qhbl.addLayout(self.qvbl1)

        self.get_mnemonic()
        self.get_feedback()

        self.qpb_create_account.clicked.connect(self.create_account)
        self.qpb_del_account.clicked.connect(self.del_account)
        self.qpb_search_account.clicked.connect(self.search_account)
        self.qpb_reset_password.clicked.connect(self.reset_password)
        self.qpb_reset_max_favorites.clicked.connect(self.reset_max_favorites)
        self.qpb_reset_phone.clicked.connect(self.reset_phone)
        self.qpb_change_mnemonic.clicked.connect(self.get_mnemonic)
        self.qpb_del_mnemonic.clicked.connect(self.del_mnemonic)
        self.qpb_read_feedback.clicked.connect(self.read_feedback)

    # 检查手机号格式是否正确
    def check_phone(self):
        phone = self.qle_phone.text()
        return len(phone) == 11 and phone[0] == '1' and phone[1] > '2'

    # 检查新手机号格式是否正确
    def check_new_phone(self):
        phone = self.qle_new_phone.text()
        return len(phone) == 11 and phone[0] == '1' and phone[1] > '2'

    # 创建账号
    def create_account(self):
        if not self.check_phone():
            QMessageBox.critical(self, '错误', '请输入正确的手机号！')
        elif asyncio.run(asyncio_c.check_phone_exist(self.qle_phone.text())):
            QMessageBox.critical(self, '错误', '该手机号已经被注册过！')
        else:
            asyncio.run(asyncio_c.add_user(self.qle_phone.text(), "000000"))
            QMessageBox.information(self, "提示", "创建成功！")

    # 销毁账号
    def del_account(self):
        if not self.check_phone():
            QMessageBox.critical(self, '错误', '请输入正确的手机号！')
        elif not asyncio.run(asyncio_c.check_phone_exist(self.qle_phone.text())):
            QMessageBox.critical(self, '错误', '该账号不存在！')
        elif QMessageBox.question(self, "警告", "你真的要销毁账号吗？", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            asyncio.run(asyncio_c.destroy_account(self.qle_phone.text()))
            QMessageBox.information(self, "提示", "销毁成功！")

    # 查询账号
    def search_account(self):
        if not self.check_phone():
            QMessageBox.critical(self, '错误', '请输入正确的手机号！')
        elif not asyncio.run(asyncio_c.check_phone_exist(self.qle_phone.text())):
            QMessageBox.critical(self, '错误', '该账号不存在！')
        else:
            infor = asyncio.run(asyncio_c.get_personal_information(self.qle_phone.text()))
            vocabulary_rank = asyncio.run(asyncio_c.get_personal_vocabulary_rank(self.qle_phone.text()))
            mnemonic_rank = asyncio.run(asyncio_c.get_personal_mnemonic_rank(self.qle_phone.text()))
            QMessageBox.information(self, "账号信息", "手机号：" + self.qle_phone.text() + "\n密码：" + infor[0] + "\n昵称：" + infor[1] + "\n最大收藏数：" + str(infor[2]) + "\n注册时间：" + str(infor[3]) + "\n词汇量：" + str(infor[4]) + "\n词汇量排名：" + str(vocabulary_rank) + "\n助记贡献量：" + str(mnemonic_rank[0]) + "\n助记贡献排名：" + str((mnemonic_rank[1])))

    # 重置密码
    def reset_password(self):
        if not self.check_phone():
            QMessageBox.critical(self, '错误', '请输入正确的手机号！')
        elif not asyncio.run(asyncio_c.check_phone_exist(self.qle_phone.text())):
            QMessageBox.critical(self, '错误', '该账号不存在！')
        else:
            asyncio.run(asyncio_c.change_password(self.qle_phone.text(), '000000'))
            QMessageBox.information(self, "提示", "修改成功！")

    # 重置最大收藏数
    def reset_max_favorites(self):
        if not self.check_phone():
            QMessageBox.critical(self, '错误', '请输入正确的手机号！')
        elif not asyncio.run(asyncio_c.check_phone_exist(self.qle_phone.text())):
            QMessageBox.critical(self, '错误', '该账号不存在！')
        elif QMessageBox.question(self, "提示", "确定修改吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            asyncio.run(asyncio_c.set_personal_max_favorites(self.qle_phone.text(), self.qle_max_favorites.text()))
            QMessageBox.information(self, "提示", "修改成功！")
            asyncio.run(asyncio_c.send_email(self.qle_phone.text(), "您的最大收藏数已经被修改为：" + self.qle_max_favorites.text() + "。\n    请您注意查收！谢谢！"))

    # 改绑手机号
    def reset_phone(self):
        if not self.check_phone():
            QMessageBox.critical(self, '错误', '请输入正确的手机号！')
        elif not asyncio.run(asyncio_c.check_phone_exist(self.qle_phone.text())):
            QMessageBox.critical(self, '错误', '该账号不存在！')
        elif not self.check_new_phone():
            QMessageBox.critical(self, '错误', '请输入正确的新手机号！')
        elif asyncio.run(asyncio_c.check_phone_exist(self.qle_new_phone.text())):
            QMessageBox.critical(self, '错误', '该新手机号已经被绑定过！')
        else:
            asyncio.run(asyncio_c.change_phone(self.qle_phone.text(), self.qle_new_phone.text()))
            QMessageBox.information(self, "提示", "换绑成功！")

    # 获取助记信息
    def get_mnemonic(self):
        mnemonic = asyncio.run(asyncio_c.get_rand_mnemonic())
        if mnemonic is not None:
            self.contribute_phone = mnemonic[0]
            self.contribute_word = mnemonic[1]
            self.contribute_mnemonic = mnemonic[2]
        else:
            self.contribute_phone = ""
            self.contribute_word = ""
            self.contribute_mnemonic = ""
        self.ql_contribute_phone.setText("贡献者手机号：" + self.contribute_phone)
        self.ql_contribute_word.setText("单词：" + self.contribute_word)
        self.ql_contribute_mnemonic.setText("助记：" + self.contribute_mnemonic)

    # 删除助记
    def del_mnemonic(self):
        if self.contribute_phone != "" and QMessageBox.question(self, "提示", "确定删除该助记吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            asyncio.run(asyncio_c.set_mnemonic(self.contribute_phone, self.contribute_word, ''))
            QMessageBox.information(self, "提示", "删除助记成功！")
            asyncio.run(asyncio_c.send_email(self.contribute_phone, "您之前贡献的关于“"+self.contribute_word+"”的助记“"+self.contribute_mnemonic+"”涉嫌违规，已被删除。\n    非常抱歉！"))
            self.get_mnemonic()

    # 获取反馈信息
    def get_feedback(self):
        feedback = asyncio.run(asyncio_c.get_feedback())
        if feedback is not None:
            self.feedback_id = int(feedback[0])
            self.feedback_phone = feedback[1]
            self.feedback_content = feedback[2]
            self.feedback_timestamp = str(feedback[3])
        else:
            self.feedback_id = -1
            self.feedback_phone = ""
            self.feedback_timestamp = ""
            self.feedback_content = ""
        self.ql_feedback_id.setText("反馈ID：" + str(self.feedback_id))
        self.ql_feedback_phone.setText("反馈者手机号：" + self.feedback_phone)
        self.ql_feedback_timestamp.setText("反馈时间：" + self.feedback_timestamp)
        self.ql_feedback_content.setText("反馈内容：" + self.feedback_content)

    # 删除反馈
    def read_feedback(self):
        if self.feedback_id != -1 and QMessageBox.question(self, "提示", "确定删除该反馈吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            asyncio.run(asyncio_c.del_feedback(self.feedback_id))
            QMessageBox.information(self, "提示", "删除反馈成功！")
            asyncio.run(asyncio_c.send_email(self.feedback_phone, "您之前反馈的“"+self.feedback_content+"”已经审阅。\n    非常感谢！"))
        self.get_feedback()
