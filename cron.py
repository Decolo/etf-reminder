from crontab import CronTab

# 创建一个 Cron 作业对象
cron = CronTab(user="admin")  # 替换为您的用户名

# 创建一个新的 Cron 作业
job = cron.new(command="python ./crawlers/run.py")  # 替换为您的 Python 脚本的路径

# 设置 Cron 作业的定时规则
job.setall("0 17 * * 1-5")  # 替换为您的定时规则

# 将 Cron 作业写入 CronTab
cron.write()
