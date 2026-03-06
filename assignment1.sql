
SQL Section (2 Questions)
Q4. Find the Second Highest Salary
Table: employees
id
name
salary
1
Alice
90000
2
Bob
85000
3
Charlie
85000
4
David
80000
5
Eva
70000


Requirement:Write a SQL query to find the second highest distinct salary.

Expected Output:
second_highest_saly
85000

>>second highest distinct salary
SELECT DISTINCT salary AS second_highest_saly
FROM (
	SELECT SALARY
	DENSE_RANK ()(ORDER BY salary DESC ) AS rank
	FROM employees
) ranked_salaries
WHERE rank = 2;

Q5. Find Customers with No Orders
customers
customer_id
customer_name
1
Alice
2
Bob
3
Charlie
orders
order_id
customer_id
amount
1
1
200
2
2
150



Write a SQL query to find customers who have not placed any orders.
Expected Output:
customer_nae
Charlie



>>>>customer name with no order

SELECT customer_name FROM
customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
WHERE order_id is NULL;
