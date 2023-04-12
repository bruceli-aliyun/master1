# master1
>这个githup文件夹，记录的是python需要掌握的一些案列
### celery
```shell
# 执行命令--在 tasks.py 所在目录执行(一个) --pool=solo需要加上
celery -A demo_celery.tasks worker -l info --pool=solo
```