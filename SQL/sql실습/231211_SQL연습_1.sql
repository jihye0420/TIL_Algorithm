-- 주석 1
# 주석 2
/* 여
러
줄 */

SELECT * FROM sakila.actor;
select * from sakila.actor;
select * from SAKILA.ACTOR;

# 명령어는 대문자로 작성, 테이블/DB명/컬럼명 같은 변수명은 소문자로 작성
# 윈도우에서는 소문자, 대문자 가리지 않음
# 리눅스에서는 소문자, 대문자를 가림

CREATE database fisa;
-- DROP database fisa;

USE sakila; -- 커서를 sakila 안으로 옮기겠음
SELECT * FROM actor; -- 그 안에 있는 테이블은 DB명 생략 가능
SELECT * FROM world.city;

CREATE DATABASE IF NOT EXISTS mywork; -- IF NOT EXISTS : 존재하지 않는다면
USE mywork;

-- 테이블(복수)은 데이터 튜플(단수)을 모아두는 장소
CREATE TABLE if not exists mywork.students
	( 
	stu_no VARCHAR(15) PRIMARY KEY, 
	stu_name VARCHAR(20) NOT NULL, 
	grade INT NOT NULL,
	class VARCHAR(20) NOT NULL,
	sex ENUM('male', 'female') NOT NULL,
	age INT,
	enter_date DATE
	 ); 

-- DROP TABLE IF EXISTS mywork.student; 


-- INSERT INTO DB명.테이블명 (컬럼명) VALUES (실제값);
 
INSERT INTO mywork.students (stu_no , stu_name , grade , class, sex, age, enter_date)
VALUES
('A10003', '김연지3', 3, 5, 'FEMALE', NULL, '2023-12-11');


-- DEFAULT 확인

DROP TABLE IF EXISTS mywork.students;
-- 테이블(복수)은 데이터 튜플(단수)을 모아두는 장소

-- 제약조건 추가
CREATE TABLE mywork.students (
    stu_no VARCHAR(15) PRIMARY KEY,
    stu_name VARCHAR(20) NOT NULL UNIQUE,
    grade INT NOT NULL,
    class VARCHAR(20) DEFAULT '미정',
    sex ENUM('male', 'female') NOT NULL,
    age INT CHECK (age > 0),
    enter_date DATE
); 


-- INSERT INTO DB명.테이블명 (컬럼명) VALUES (실제값);

-- VARCHAR에 지정한 값보다 큰 값은 들어가지 않음 
INSERT INTO mywork.students (stu_no , stu_name , grade , class, sex, age, enter_date)
VALUES
('A10003', '김연지3', 3, 5, 'FEMALE', -3, '2023-12-11');

INSERT INTO mywork.students (stu_no , stu_name , grade , class, sex, age, enter_date)
VALUES
('A10005', '김연지3', 3, NULL, 'FEMALE', 3, '2023-12-11');

INSERT INTO mywork.students (stu_no , stu_name , grade , class, sex, age, enter_date)
VALUES
('A10005', '김연지4', 3, NULL, 'FEMALE', 3, '2023-12-11');

INSERT INTO mywork.students VALUES ('A10006', '김연지', 3, NULL, 'FEMALE', 3, '2023-12-11');
	
INSERT INTO mywork.students (stu_no , stu_name , grade , sex, age, enter_date)VALUES ('A10007', '김연지1', 3, 'FEMALE', 3, '2023-12-11');

	


	






