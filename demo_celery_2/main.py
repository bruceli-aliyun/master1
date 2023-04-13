from celery import Celery
from . import config

# broker = 'redis://127.0.0.1:6379/10'  # 设置broker
# backend = 'redis://127.0.0.1:6379/11'  # 设置backend
# 创建一个应用
# app = Celery("demo", broker=broker, backend=backend)
# todo 可以使用上面的方法导入配置文件
app = Celery("demo")
# celery配置文件
app.config_from_object(config)
# 注册任务
app.autodiscover_tasks(["demo_celery_2.demo"])







