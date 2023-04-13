# select.md 在此记录的是mysql查询语句
```mysql
use demo;
select * from user;
select username from account;
select username from account where id=1;
select username from account where id=1 and username='admin';
select username from account where id=1 or username='zhang_san';
# 查询账户id=人物id的数据 as 可以用在表，数据，字段中
select * from account as a join profile as p on profile.id=account.id;
select * from account as a join profile as p on profile.id=account.id where p.nickname='admin';
select * from account as a left join profile as p on profile.id=account.id where p.nickname='admin';
select * from account as a right join profile as p on profile.id=account.id where p.nickname='admin';
# 查询所有并分组,统计数量大于20个的查询出来
select nickname,gender from profile group by gender having count(*)>20;
# 查询所有并排序
select id,nickname from profile order by id desc;
select id,nichname,birthdate from profile order by birthdate asc;
# 将所有并分页展示 limit
select id,nichname,birthdate from profile limit 0, 5;
# 查询出年龄18-28之间的人 where between and
select id,nichname,birthdate，age from profile where age between 18 and 28;
# from > where > group by > select > order by > limit
```
```sql
select *,
    field, count(*), t2.field as t2f,'可添加'
from table,
     table2 as t2,
     table3 join table4 on t3.id=t4.id, # 连接两个表变成一个新表
     table5 left join table6 on t3.id=t4.id,# 左连接, 查出左表
     table5 right join table6 on t3.id=t4.id # 右连接，查出右表
where id="1" and age between 18 and 28
    group by age having count(*) > 10
    order by age asc limit 1,5
```

