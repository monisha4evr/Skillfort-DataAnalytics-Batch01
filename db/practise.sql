select name ,name|| '-' || city from students;
select name,concat(name,' ',city) from students;
select name , concat(name,' ','skillfort') from students;
select name,concat(name||'('||city||')' ) from students;
select name,concat_ws('-',name,city) from students;
select format('Mr.%s',name) from students;
select concat(name,'-',COALESCE(age,18)) from students where age is null;-- empty value
select name,concat_ws('-',name,age) from students where age is null; -- skill null


select name,city from students;

select concat(name,'-',city) from students;
select name || '-' || city from students;
select name || '(' || city || ')' from students;
select concat_ws('-',name,city) from students;
select concat(name,'-',age) from students where age is null; -- consider as empty
select concat_ws('-',name,COALESCE(age,20)) from students where age is null; -- skip null value
select concat('Mr','.',name) from students;
select format('%s %I',name,COALESCE(age,0)) from students;

-- lower,upper,initcap
select * from students where lower(city)='panruti';
substring(column,start_position,total_count)
select id,substring(id,1,2) from students;
select id,substring(id,3) from students;

select s.name,length(s.name) as name_length  from students s;
select city,substring(city,length(city)-2) from students;

select id, position('01' in id) from students; -- pattern Match
select id,strpos(id,'S') from students;
-- Trim
select * from students where trim(name)='Swetha';
select name,trim(name) as tname,ltrim(name),rtrim(name) from students order by id desc;
-- PADDING
select id,lpad(id,10,'0'),rpad(id,10,'0') from students;
-- replace 
select city,replace(city,'Pondicherry','Pondy') from students;
-- reverese 
select city,reverse(city) from students;


select '5' , cast('5' as integer), cast ('5.3' as float);

select * from public.order;

select * from current_date;
select * from current_time;
select * from current_timestamp;
select current_date as today,current_date-interval '5 days' as int_day;
select current_date as today,current_date+interval '5 days' as int_day;
select * from current_date today
,extract(day from current_date) as date
,extract(month from current_date) as month
,extract(year from current_date) as year
,extract(week from current_date) as week
,extract(quarter from current_date) as quarter
;

select date_part('day', current_timestamp);
select 15+10,(15-10) subtract,(15*10) as multiply;
select 15-10;
select 15*10;
select round(15.0/10);
select ceil(5.6);
select floor(5.6);
select '5' ,cast('5' as integer);

--  Aggregation Function

select * from payments;
select sum(paid) as tot_earning from payments;
select min(paid) from payments;
select max(paid) from payments;
-- 1. january month total Earning 
-- 2. January month total transaction

select count(transaction_id) from payments;

select * from students;
-- Find total number of students in Students Table
select count(distinct(city)) from students;


SELECT count(id) from students;

select city from students group by city order by city desc;
select city,count(name) total_student from students group by city having count(name)>20 order by city desc;
select * from payments;

from / join 
where
group by 
having 
select 
distinct
order by 
limit;

select * from students;
select * from courses;
select * from payments;

select * from students where id='22S001';
select * from payments where student='22S001';
select * from courses where id in('22C15','22C12');

-- Joins
Cross Join 
inner Join 
left join
right join
full join 


inner join (Both Table Matching Records)

select p.transaction_id,s.name,s.area,p.paid,c.name,c.fee
from payments p
join students s
on p.student = s.id
join courses c
on p.course = c.id 
;

select s.id,s.name,s.area,p.transaction_id,p.paid
from payments p
right join students s
on p.student = s.id
order by s.id desc ;

select s.id,s.name,s.area,p.transaction_id,p.paid
from students s
left join payments p 
on p.student = s.id
order by s.id desc ;

-- Subquery
select count(*) from orders;
select round(avg(total_amount)) from orders;
select * from orders where total_amount>7804;
select * from orders where total_amount > (select round(avg(total_amount)) from orders);

select customer_id from orders group by customer_id having count(*)>1;
select * from customers where customer_id in(select customer_id from orders group by customer_id having count(*)>1);
select category,price from products;
select * from products where (category,price) in (
select category,price from products group by category,price having count(*)>1);

select * from customers c where  exists (
select 1 from orders o where  c.customer_id =o.customer_id
)

SELECT *
FROM products p
WHERE price < (
    SELECT AVG(price)
    FROM products p2
    WHERE p2.category = p.category
);
SELECT 
    product_name,
    price,
    (SELECT AVG(price) FROM products) AS average_price
FROM products;



