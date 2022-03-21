select * from countries;
select email,phone_number from employees;
select * from employees where last_name="fay";
select hire_date from employees where last_name="Grant" or last_name="Whalen";
select employees.first_name,employees.last_name from employees join jobs on employees.job_id=jobs.job_id where  jobs.job_title="Shipping Clerk";
select * from employees;
select employees.first_name from employees join departments where departments.department_id="8";
select * from departments order by department_id desc;
select last_name from employees where last_name like "k%";
select first_name from employees where hire_date between '1995-01-01' and '1998-01-01';
select job_title from jobs where max_salary<5000;
select lower(email) from employees;
select first_name from employees where hire_date like "1995%";
INSERT INTO employees(employee_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id) VALUES
(207,'PAUL','Newton','paul.newton@sqltutorial.org','515.127.4563','1997-12-24',13,2900.00,114,11);
select * from dependents;
set sql_safe_updates=0;
set foreign_key_checks=0;

delete from departments where department_name="shipping";
