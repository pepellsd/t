## 2-SQL

####вариант 1  
```create table temp (name VARCHAR, status SMALLINT);
insert into temp(name, status) select v1, v2 from (select name as v1, ROW_NUMBER() over(order by 1) r from full_names) a join (select status as v2, ROW_NUMBER() over (order by 1) r from short_names limit 500000) b on a.r=b.r;
DROP TABLE full_names;
ALTER TABLE temp RENAME TO full_names;
```
####вариант 2
```
update full_names set status = subq.status from (select status, name from short_names) as subq where SUBSTRING(full_names.name from '\d+')::int = SUBSTRING(subq.name from '\d+')::int;
```
####вариант 3
````
update full_names set status = subq.status from (select status, name from short_names) as subq where (string_to_array(full_names.name, '.'))[1] = subq.name;
````