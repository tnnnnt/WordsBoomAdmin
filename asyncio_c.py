# coding:utf-8
import asyncio
from decimal import Decimal
import datetime

IP = '123.175.77.65'  # 服务器的IP地址
PORT = 11451  # 服务器监听的端口号
BUFLEN = 8192  # 一次最多读取的字节数


# 异步函数，向服务器发送请求并接收响应
async def req(s):
    reader, writer = await asyncio.open_connection(IP, PORT)  # 连接到服务器
    writer.write(s.encode())  # 发送消息给服务器
    await writer.drain()  # 等待接收来自服务器的响应
    data = await reader.read(BUFLEN)  # 从服务器接收数据（每次最多读取BUFLEN个字节）
    ret = data.decode()
    writer.close()
    await writer.wait_closed()
    return ret


# 检查手机号是否存在
async def check_phone_exist(phone):
    return await req('00' + phone) == '1'


# 添加用户
async def add_user(phone, password):
    await req('03' + phone + password)


# 修改密码
async def change_password(phone, password):
    await req('05' + phone + password)


# 销毁账户
async def destroy_account(phone):
    await req('12' + phone)


# 更换手机号
async def change_phone(phone, new_phone):
    await req('14' + phone + new_phone)


# 设置助记
async def set_mnemonic(phone, word, mnemonic):
    await req('25' + phone + word + ',' + mnemonic)


# 获取个人词汇量排名
async def get_personal_vocabulary_rank(phone):
    return await req('33' + phone)


# 获取个人助记排名
async def get_personal_mnemonic_rank(phone):
    return eval(await req('34' + phone))


# 检查管理员账号
async def check_admin_account(account):
    return await req('50' + account) == '1'


# 检查管理员密码
async def check_admin_password(password):
    return await req('51' + password) == '1'


# 获取个人信息
async def get_personal_information(phone):
    return eval(await req('52' + phone))


# 设置用户最大收藏量
async def set_personal_max_favorites(phone, num):
    await req('53' + phone + num)


# 获取随机助记
async def get_rand_mnemonic():
    return eval(await req('54'))


# 获取反馈
async def get_feedback():
    return eval(await req('55'))


# 删除反馈
async def del_feedback(id):
    await req('56' + str(id))


# 发送邮件
async def send_email(phone, content):
    await req('57' + phone + content)
