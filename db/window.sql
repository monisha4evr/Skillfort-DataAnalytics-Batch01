select customer_name,sum(qty) as total_qty from "order" group by customer_name;

over()

select *,sum(qty) over(
partition by customer_name
order by id desc
) from "order";

partition by 
order by 
Frame - rows between unbounded preceding 1 following
unbounded ,preceding , following  current row

-- type 1: 
1. previous rows to current row 

rows between unbounded preceding and  current row

2. current row + previous row 

rows between 1 preceding and current row 

3.  current row + next row 

rows between current row and 1 following 

rows between unbounded preceding and unbounded following 


select id,customer_name,qty, min(qty) over (
partition by customer_name
order by id
rows between unbounded preceding and unbounded following
) from "order";


ranking 
row_number
rank
dense_rank
ntile

select customer_name,unit_price ,dense_rank() over(
partition by customer_name
order by unit_price
) 
from "order"; 

select customer_name,unit_price ,DENSE_Rank() over(
partition by customer_name
) 
from "order"; 

Aggregate function 
lead , lag, firstvalue,lastvalue