# celery配置文件

"""上面配置不管用"""
broker_url = 'redis://localhost/5'  # 任务库：实际情况选择
result_backend = 'redis://localhost/6'  # 结果库：实际情况选择
include = ['demo_celery_2.demo']  # 加载应用
