from celery import Celery  # 导入Celery

broker = 'redis://127.0.0.1:6379/5'  # 设置broker

backend = 'redis://127.0.0.1:6379/6'  # 设置backend

app = Celery('tasks', broker=broker, backend=backend)  # 实例化celery


# 编写任务
@app.task
def add(x, y):
    return x + y