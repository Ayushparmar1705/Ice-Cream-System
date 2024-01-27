create database ice_cream;

use ice_cream;


create table products(prod_id int primary key auto_increment,
prod_name varchar(100),
prod_cat varchar(100),
prod_qty int,
prod_price int,
prod_dis varchar(100));

select * from products;
drop table products;
-- drop table products;





create table billing(bill_id int primary key auto_increment,
date varchar(100),
cus_name varchar(100),
prod_name varchar(100),
quntity int,
price int,
total int);



select * from billing;


create table customers(cus_id int primary key auto_increment,
cus_name varchar(100),
cus_phno varchar(100));

drop table customers;


select * from customers;



create table billing(bill_id int primary key,
date varchar(100),
cus_name varchar(100),
prod_name varchar(100),
quntity int,
price int,
total int,
price_product int,
total_qty int);



select * from billing;


drop table billing;

update products set prod_qty = 60 where prod_id = 2;

