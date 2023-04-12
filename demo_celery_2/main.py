from celery import Celery

broker = 'redis://127.0.0.1:6379/10'  # 设置broker
backend = 'redis://127.0.0.1:6379/11'  # 设置backend
# 创建一个应用
app = Celery("demo", broker=broker, backend=backend)

app.autodiscover_tasks(["demo_celery_2.demo"])


