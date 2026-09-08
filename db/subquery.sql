/* single row subquery 
1. Find the orders where the total amount is greater than the average order amount.
2. Find the product with the highest price.

2. Multiple row subquery
Find the customers who have placed more than one order.
Find the products whose price is greater than the price of any product in the Electronics category.

3.Multiple Column subquery
Find the products that have the same category and price as another product.
Find the orders that have the same customer and order status as another order.

corelated:
Find the customers who have placed at least one order.
Find the products whose price is greater than the average price of products in the same category.

non-corelated:
Find the products whose price is greater than the average product price.
Find the orders whose total amount is greater than the highest order amount of customer 5.

Select Clause:
Display each product name along with the average product price.
Display each order along with the highest order amount.

from clause:
Find the average order amount for each customer using a subquery in the FROM clause.
Find the total sales for each product using a subquery in the FROM clause.

where Clause:
-------------
Find the products whose price is greater than the average product price.
Find the orders placed by customers from Chennai.


in: Find customers who have placed an order.
any: Find products whose price is greater than any product in the Electronics category.
all: Find products whose price is greater than all products in the Electronics category.
exists: Find customers who have placed at least one order.
*/

select * from orders;
select round(avg(total_amount)) from orders;
select * from orders where total_amount > 7804;

select * from orders where total_amount > (select round(avg(total_amount)) from orders);

types:
1. Based on Result 
2. Based on Execution

1. Based on Result 
	- single row Subquery 
	- multiple row Subquery 
	- multiple Value Subquery 
2. Based on Execution 
	- Correlated 
	- Non Correlated 

- single row Subquery 
Eg: select * from orders where total_amount > (
select round(avg(total_amount)) 
from orders);

- multiple row Subquery 

select customer_id from orders group by customer_id having count(*)>1 ;
select * from customers where customer_id =10;
select * from customers where customer_id =1;
select * from customers where customer_id =5;

select * from customers where customer_id in (
select customer_id 
from orders 
group by customer_id 
having count(*)>1 )

select * from products where (category,price) in
(select category,price 
from products 
group by category,price 
having count(*)>1);


-- Corelated 
select * from customers ;
select * from orders;

select * from customers c where exists (
select * from orders o where c.customer_id = o.customer_id
)

select clause (scalar)
from clause (Derived/inline view)
where clause (filtering purpose )

select * from products;

select avg(price) from products;
select *,(select avg(price) from products) from products;

-- Find the average order amount for each customer using a subquery in the FROM clause.
SELECT customer_id,count(*) as totalorder, round(AVG(total_amount),2) AS avg_order_amount
FROM (
    SELECT customer_id, total_amount
    FROM orders
) AS order_data
GROUP BY customer_id;





