-- regex (Regular Expression) 

~ regex Match 
~* case insensitive
!~ not regex match
!~* not regex match case insensitive 

^ -- starting 
$ -- Ending
+ -- one or more
* -- zero or more 
. -- any one match
? -- 0 or one 
[0-9] -- any digit
[A-Z] -- any caps
[a-z] -- any smallcase
{n} -- Exactly n times

select * from customers;
select * from customers where city ~* '^c';
select * from customers where city ~ 'i$';

-- regexp_replace()
select  regexp_replace('Hello word',' ','');
select regexp_replace(customer_name,'_','') as customername from customers;
select regexp_replace('100-2020-1220','-','');
select regexp_replace('100-2020-1220','-','','g');
select regexp_replace(customer_name,'[0-9]+','') as cname from customers;

-- regexp_match()
select regexp_match(customer_name,'[a-zA-Z_]*') from customers;
select email,regexp_match(email,'([A-Za-z0-9]+)@') from customers;


CTE - (Common Table Expression) 
-- instead of writing complex query , we can divide them into small 
--  easy to read and understandable 
-- dont store in Database 

select * from orders;
select customer_id,sum(total_amount) as total,count(*) as total_order 
from orders group by customer_id having count(*)>1;

with customer_order as (select customer_id,sum(total_amount) as total,count(*) as total_order 
from orders group by customer_id)
select * from customer_order where total_order>1;

-- view 

-- create view view_name as ()
create view customer_order_view as (select customer_id,sum(total_amount) as total,count(*) as total_order 
from orders group by customer_id);

select * from customer_order_view;






