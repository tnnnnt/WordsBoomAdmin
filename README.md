# WordsBoomAdmin
我的毕业设计：基于PyQt5与Web的背单词软件单词弹弹弹管理员端

（1）防止软件多开：通过文件锁机制实现。

（2）登录账号：使用唯一的管理员账号与密码进行登录。

（3）快捷创建用户账号：不需要验证码验证，直接使用手机号进行注册，初始密码默认为“000000”。

（4）销毁用户账号：使用手机号进行销毁。

（5）查询账号：通过手机号查询用户的信息，包括密码、昵称、收藏夹容量、注册时间、词汇量及排名、助记贡献量及排名等。

（6）快捷重置用户密码：不需要验证码验证，直接使用手机号进行密码的修改，密码默认修改为“000000”。

（7）设置用户收藏夹容量：管理员可以自定义修改用户的收藏夹容量。

（8）快捷改绑用户手机号：不需要验证码验证，直接输入原手机号与新手机号进行改绑。

（9）审核助记：查看用户贡献的助记，发现不合适的助记可以进行删除操作，删除后自动向用户发送反馈。

（10）查看反馈：查看用户的反馈并自动对用户发送回执。
