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
include = ['demo_celery2.demo']  # 加载应用
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
show variables like '%character%';
```
```sql
-- demo 数据表操作 comment '注释'
show tables;
create table 'table_name'(
    id int unsigned auto_increment COMMENT 'id:类型int,约束,整型,非负数,自增',
    name varchar(20) NOT NULL COMMENT 'name:类型可变长字符串,约束不能为空', 
    primary key ('id') COMMENT '设置id主键为,也可在字段后面添加',
    unique key 'name' ('name') COMMENT '设置name唯一索引,也可在name字段后面添加，与主键类似'
)ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
show create table table_name; -- 查看创建表语句
desc table_name; -- 查看表字段及约束
drop table table_name; -- 删除表
insert into table_name values ('1','张三'),(2, '李四'),(3, '王二麻子');
```
```text
# 表数据类型 获取:SELECT DATA_TYPE FROM information_schema.COLUMNS GROUP BY DATA_TYPE
| varchar    || timestamp  || bigint     || int        || longtext   || enum       |
| text       || mediumtext || json       || datetime   || set        || char       |
| binary     || varbinary  || tinyint    || blob       || double     || decimal    |
| longblob   || smallint   || mediumblob || time       || float      || date
```
```text
# mysql常见约束
默认约束	保存数据时，如果未指定该字段的值，则采用默认值	DEFAULT
非空约束	限制该字段的数据不能为null	NOT NULL
唯一约束	保证该字段的所有数据都是唯一、不重复的	UNIQUE
主键约束	主键是一行数据的唯一标识，要求非空且唯一	PRIMARY KEY
自增约束	为每条记录生成唯一的标识号	AUTO_INCREMENT
检索约束	保证字段值满足某一个条件(8.0.16版本之后)	CHECK
外键约束	用来让两张表的数据之间建立连接，保证数据的一致性和完整性	FOREIGN KEY
```
```python
todo = '注意: 有时候不要一为的去封装，有时候简单一点也挺好'
```

