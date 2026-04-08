git:git是一个版本控制工具，用于跟踪文件变化并管理项目版本。

# git的使用
## git config
首次使用git时，需要配置用户名和邮箱。


git配置文件有两个
一个是全局（C:\Users\用户名\.gitconfig），
git config--global user.name "wanghy"
git config--uglobal user.email"wanghy_work@163.com"
一个是局部的。存在项目的.git目录下的config文件
git config user.name 查看自己的用户名
配置局部的用户名
git config user.name "wanghy"

# git命令
## 工作区到暂存区
git add 文件名       # 一个文件
git add.            # 所有文件

## 暂存区到本地仓库
git commit -m "提交信息"

## 连接本地仓库和远程仓库
git remote add origin https://github.com/用户名/仓库地址.

## 本地仓库到远程仓库
git push