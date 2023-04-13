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
### mysql
```sql
-- demo数据库操作 -- 大写代表可有可无 -- 
create database demo;
show databases;
drop database demo;
use demo;
create database IF NOT EXISTS demo DEFAULT CHAR SET  utf8mb4 COLLATE utf8mb4_unicode_ci;
-- 查看错误日志, 链接地址 : http://cd.itheima.com/news/20221007/161036.html
show variables like '%log_error%';
```
```sql
-- demo 数据表操作 comment '注释'
show tables;
create table 'table_name'(
    id int unsigned auto_increment COMMENT 'id:类型int,约束,整型非负数,自增',
    name varchar(20) NOT NULL COMMENT 'name:类型可变长字符串,约束不能为空', 
    primary key ('id') COMMENT '设置id主键为,也可在字段后面添加',
    unique key 'name' ('name') COMMENT '设置name唯一索引,也可在name字段后面添加，与主键类似'
)ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
desc table_name; -- 查看表字段及约束
drop table table_name; -- 删除表
```