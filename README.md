# master1
>在此记录的是python需要掌握的一些案列
### celery
```shell
# 执行命令--在 tasks.py 所在目录执行(一个) --pool=solo需要加上
celery -A demo_celery.tasks worker -l info --pool=solo
```
### celery配置文件
```python
# config.py
broker_url = 'redis://localhost/5'  # 任务库：实际情况选择
result_backend = 'redis://localhost/6'  # 结果库：实际情况选择
include = ['demo_celery_2.demo']  # 加载应用
```