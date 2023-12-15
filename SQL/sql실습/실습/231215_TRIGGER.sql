DROP DATABASE IF EXISTS Mart_Rkk;
CREATE DATABASE Mart_Rkk DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

USE Mart_Rkk;

create table customers(
	cus_id int  not null auto_increment primary key ,
    cus_username varchar(15) not null ,
    cus_birthdate date default (current_date)
	
);
create table products(
	prod_id  int unsigned not null  auto_increment primary key ,
    pro_productname varchar(30) not null unique,
    pro_quantity int not null, 
    pro_price int not null,
    CHECK(pro_quantity>0),
    CHECK(pro_price>0)
);

create table orders(
	ord_id int unsigned not null  auto_increment primary key ,
    order_quantity int  not null,
    cus_id int ,
	prod_id int unsigned,
    FOREIGN KEY(cus_id) REFERENCES customers(cus_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(prod_id) REFERENCES products(prod_id) ON UPDATE CASCADE ON DELETE CASCADE,
    CHECK(order_quantity>0)
 
);
DELETE FROM customers where cus_id=1;#삭제 확인
UPDATE customers set cus_id=-1 where cus_username="류준규";
UPDATE customers set cus_id=-3 where cus_username="김씨";
insert into customers values(1, "김윤성", '1999-07-02');
insert into customers values(2, "김준우", '1996-03-15');
insert into customers values(3, "류준규", '1997-07-25');
insert into customers (cus_username,cus_birthdate) values( "김씨", '1997-07-25');
insert into customers (cus_username,cus_birthdate) values( "박씨", '1997-07-25');
insert into customers (cus_username,cus_birthdate) values( "이씨", '1997-07-25');
insert into customers (cus_username) values( "전씨" );
insert into products values(1001, "새우깡", 1500,2000);
insert into products values(1002, "포카칩", 2000,1700);
insert into products values(1003, "초코송이", 3000,500);

insert into orders values(5555, 100, 1,1002);
insert into orders values(6666, 1000,2, 1003);
insert into orders values(7777, 500,3,1001);
insert into orders values(9999, 500,6,1010);#없는 prod_id 삽입불가확인
drop trigger prevent_negative_update;
DELIMITER //
CREATE TRIGGER prevent_negative_update
BEFORE UPDATE ON customers
FOR EACH ROW
BEGIN
    IF NEW.cus_id <=0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '0보다 큰값으로 수정해주세요';
    END IF;
END;
//
DELIMITER ;

UPDATE customers set cus_id=0 where cus_username="류준규";

select * from products;
select * from orders ;
select * from customers;
