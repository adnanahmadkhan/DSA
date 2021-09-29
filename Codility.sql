select test_groups.`name` as `name`, 
count(test_cases.id) as `all_test_cases`,
sum(case when test_cases.`status` = "OK" then 1 else 0 end) as "passed_test_cases",
sum(test_groups.`test_value`) as total_value
from test_cases full join test_groups ON test_cases.`group_name` = test_groups.`name`
group by test_groups.`name`
order by total_value desc;


## POSTGRESQL Query Codility 100%

-- write your code in PostgreSQL 9.4
select test_groups.name as name, 
count(test_cases.id) as all_test_cases,
sum(case when test_cases.status = 'OK' then 1 else 0 end) as passed_test_cases,
sum(case when test_cases.status = 'OK' then test_groups.test_value else 0 end) as total_value
from test_cases full join test_groups ON test_cases.group_name = test_groups.name
group by test_groups.name
order by total_value desc, name;

