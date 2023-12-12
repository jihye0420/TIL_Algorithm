-- 주석 1
# 주석 2
/* 여
러
줄 */

SELECT * FROM sakila.actor;
select * from sakila.actor;
select * from SAKILA.ACTOR;

# 명령어는 대문자로 작성, 테이블/DB명/컬럼명 같은 변수명은 소문자로 작성합니다
# 윈도우에서는 소문자, 대문자 가리지 않습니다
# 리눅스에서는 소문자, 대문자를 가립니다

CREATE database fisa;
DROP database fisa;

USE sakila; -- 커서를 sakila 안으로 옮기겠음
SELECT * FROM actor; -- 그 안에 있는 테이블은 DB명 생략 가능
SELECT * FROM world.city;

CREATE DATABASE IF NOT EXISTS mywork; -- IF NOT EXISTS : 존재하지 않는다면
USE mywork;

DROP TABLE IF EXISTS mywork.students;
-- 테이블(복수)은 데이터 튜플(단수)을 모아두는 장소
CREATE TABLE mywork.students
	( 
	stu_no VARCHAR(15) PRIMARY KEY, 
	stu_name VARCHAR(20) NOT NULL UNIQUE, 
	grade INT NOT NULL,
	class VARCHAR(20) default '미정',
	sex ENUM('male', 'female') NOT NULL,
	age INT check(age > 0),
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
	
USE mywork;
select count(*) from box_office;

-- DML
-- 1. 모든 값 
select * from box_office;
-- 와일드카드는 웬만하면 실무에서 사용하지 않는 것이 좋습니다
-- 속도와 유지보수를 생각했을 때 각각 컬럼명을 써주는 것을 권장합니다

select count(*) from box_office; -- 함수 사용 
SELECT movie_name, rep_country FROM box_office; -- 컬럼 선택 
SELECT * FROM box_office WHERE years=2004; -- 조건절 
-- 2004년 혹은 2005년에 제작된 영화
-- SQL은 방언이 많다 -> 함수나 명령어들을 작성하는 방법이 제각각이다
SELECT * FROM box_office WHERE years=2004 OR years=2005;
SELECT * FROM box_office WHERE years BETWEEN 2004 AND 2005;
SELECT * FROM box_office WHERE 2004 <= years AND years <= 2005;
SELECT * FROM box_office WHERE 2004 <= years && years <= 2005;  

-- 문자열 
SELECT * FROM box_office WHERE movie_name LIKE '천년'; -- 일치하는
-- 글자수 따져서 일치하는 _ 언더바 하나당 글자 하나 
-- 글자수가 0개이상 몇개라도 일치한 % - 몇글자이든 상관없이 
-- 천년으로 시작하는
SELECT * FROM box_office WHERE movie_name LIKE '천년%';
-- 천년으로 끝나는
SELECT * FROM box_office WHERE movie_name LIKE '%천년';

SELECT * FROM box_office WHERE movie_name LIKE '천년_'; -- 천년 한글자
SELECT * FROM box_office WHERE movie_name LIKE '%천년%'; -- 천년이라는 단어가 어디든 들어가는
SELECT * FROM box_office WHERE movie_name IN ('여우', '학'); -- 리스트에 있는 단어와 완전히 일치

-- 여우나 학이라는 단어가 들어간 영화 전부 
SELECT * FROM box_office WHERE movie_name LIKE '%여우%' OR movie_name LIKE '%학%'; 
SELECT * FROM box_office WHERE movie_name LIKE '%여우%' || movie_name LIKE '%학%'; 
SELECT * 
FROM box_office 
-- 등호 연산자가 = / 논리연산자 && || !
WHERE movie_name LIKE '%여우%' -- 조건1 
     && years = 2007;  -- 조건2 
     
-- 2018년 개봉한 한국 영화 조회하기
SELECT count(*) FROM box_office WHERE release_date LIKE '2018%' AND rep_country LIKE '한국';

-- 2019년 개봉 영화 중 관객수가 500만 명 이상인 영화 조회하기
SELECT count(*) FROM box_office 
WHERE audience_num >= 5000000 AND
release_date LIKE '2019%';

SELECT * FROM box_office;
-- 2019년 개봉 영화 중 관객수가 500만 명 이상이거나 
-- 매출액이 400억 원 이상인 영화 조회하기
SELECT * FROM box_office 
WHERE release_date LIKE '2019%' && -- 조건1
      (audience_num >= 5000000 || sale_amt >= 40000000000); -- 조건2 

-- 2012년에 제작됐지만, 2019년에 개봉된 영화를 조회하기.
SELECT * FROM box_office
WHERE years=2012 AND release_date LIKE '2019%';
     
SELECT movie_name, years AS 제작년도, release_date AS 개봉년도
FROM box_office
WHERE years=2012 AND release_date LIKE '2019%';

SELECT movie_name, years "제작 년도", release_date "개봉 년도"
FROM box_office
WHERE years=2012 AND release_date LIKE '2019%';

select * from box_office 
 where movie_name 
 IN (select movie_name 
     from box_office 
     where movie_name like '%천년%' or '%여우%');

SELECT name, continent, region
  FROM world.country
 WHERE population > 50000000
 ORDER BY continent, region DESC; -- continent 오름차순, region 내림차순 
 
 SELECT code, name, continent, region, population
  FROM world.country
 WHERE population > 100000000
 ORDER BY 2 ASC; -- 문자열 정렬은 collation 설정을 따른다 
 
  SELECT code, name, continent, region, population
  FROM world.country
 WHERE population > 100000000
 ORDER BY 2 ASC
 LIMIT 3;
 
-- 2019년 개봉하고 500만 명 이상의 관객을 동원한 
-- 매출액 기준 상위 5편의 영화만 조회
SELECT * FROM box_office
WHERE release_date LIKE '2019%' AND 
audience_num >= 5000000
ORDER BY sale_amt DESC
LIMIT 5;

-- 2019년 제작한 영화 중 관객수 1~10위 영화를 조회
SELECT * FROM box_office
WHERE release_date LIKE '2019%' 
ORDER BY audience_num DESC
LIMIT 10;

-- box_office 테이블에서 
-- 2019년 제작된 영화 중 
-- 영화 유형(movie_type 칼럼)이 장편이 아닌 
-- 영화를 순위(ranks)대로 조회.
SELECT * FROM box_office
WHERE years LIKE '2019%'
AND movie_type != '장편'
ORDER BY ranks;

DROP DATABASE IF EXISTS student_mgmt;
CREATE DATABASE student_mgmt DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

USE student_mgmt;
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id TINYINT NOT NULL AUTO_INCREMENT, -- 값을 넣을 때 마다 자동으로 1씩 증가하는 옵션
  name VARCHAR(10) NOT NULL,
  gender ENUM('man','woman') NOT NULL,
  birth DATE NOT NULL,
  english TINYINT NOT NULL,
  math TINYINT NOT NULL,
  korean TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('dave', 'man', '1983-07-16', 90, 80, 71);
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('minsun', 'woman', '1982-10-16', 30, 88, 60);
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('david', 'man', '1982-12-10', 78, 77, 30);
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('jade', 'man', '1979-11-1', 45, 66, 20);
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('jane', 'man', '1990-11-12', 65, 32, 90);
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('wage', 'woman', '1982-1-13', 76, 30, 80);
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('tina', 'woman', '1982-12-3', 87, 62, 71);

-- 성별 기준으로 수학점수의 평균 
SELECT gender, avg(math)
FROM student_mgmt.students
GROUP BY gender; 

-- -- 성별 기준으로 수학점수의 평균 
SELECT gender, avg(math)
FROM student_mgmt.students
GROUP BY gender -- 원본은 그대로 두고, 원본테이블에 없는 값을 계산해 냅니다 
HAVING avg(math) >= 60
ORDER BY gender DESC
LIMIT 1; -- group by의 결과에서 조건을 만족하는 값만 조회 

-- -- 성별 기준으로 수학점수의 평균 
SELECT gender, AVG(math) 수학평균, AVG(english), AVG(korean)
FROM student_mgmt.students
GROUP BY gender -- 원본은 그대로 두고, 원본테이블에 없는 값을 계산해 냅니다 
HAVING avg(math) >= 60; -- group by의 결과에서 조건을 만족하는 값만 조회 


SELECT gender, AVG(math) 수학평균, AVG(english), AVG(korean)
FROM student_mgmt.students
GROUP BY gender -- 원본은 그대로 두고, 원본테이블에 없는 값을 계산해 냅니다 
HAVING avg(math) >= 60; -- group by의 결과에서 조건을 만족하는 값만 조회 

-- 현재 데이터베이스는 몇개 대표국가의 영화를 다루고 있는 걸까?
SELECT DISTINCT rep_country FROM mywork.box_office;

-- 실습: students 테이블에서 수학점수와 영어점수의 평균이 70점 이상인 사람들만 출력하려면?
SELECT name, math, english
FROM student_mgmt.students
WHERE math >= 70 && english >= 70;

SELECT name, math, english, ((math + english) /2) >= 70
FROM student_mgmt.students
WHERE ((math + english) /2) >= 70;

-- 성별 평균을 구하고 70점이 넘는 수학점수와 영어점수의 평균이 70점 이상인 사람들만 출력하려면?
SELECT name, gender, AVG(math) 개인별점수, AVG(english) AS 개인별점수
FROM student_mgmt.students
GROUP BY name, gender -- name으로 1차 group by하기 때문에 행단위와 다를바 없음
HAVING 
	avg(english) >= 70 AND avg(math) >= 70; -- GROUP BY 이후의 조건을 판별합니다 

INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('dave', 'man ', '1983-07-16', 90, 80, 71);
SELECT  DISTINCT gender FROM student_mgmt.students; 
SELECT * FROM students;
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('dave ', 'man  ', '1983-07-16', 90, 80, 71);
SELECT  DISTINCT name FROM student_mgmt.students; 
INSERT INTO students (name, gender, birth, english, math, korean) VALUES (' dave ', 'man  ', '1983-07-16', 90, 80, 71);
SELECT  DISTINCT name FROM student_mgmt.students; 

-- # 연도별 개봉한 영화의 편수를 집계해서 출력해주세요
SELECT year(release_date), count(release_date)
FROM mywork.box_office
GROUP BY year(release_date)
order by 2 DESC;

-- # 2019년 개봉 영화의 유형별 최대, 최소 매출액과 전체 매출액 집계하기
SELECT movie_type 영화종류, MAX(sale_amt) 최대매출액, MIN(sale_amt) 최소매출액, SUM(sale_amt) 전체매출액 
FROM mywork.box_office
WHERE YEAR(release_date) = 2019
GROUP BY movie_type;

-- movie_type이 NULL 이 아닌 값들만 출력하기 (NULL은 값이 아닙니다. 값없음입니다.)
SELECT movie_type 영화종류, MAX(sale_amt) 최대매출액, MIN(sale_amt) 최소매출액, SUM(sale_amt) 전체매출액 
FROM mywork.box_office
WHERE YEAR(release_date) = 2019
  && movie_type IS NOT NULL -- NULL 값은 IN, LIKE, = 같은 연산자로 찾을 수 없습니다 
GROUP BY movie_type
ORDER BY 최소매출액 DESC; -- ALIAS를 지어주면 해당 쿼리문 내에서는 ALIAS를 컬럼명처럼 쓸 수 있습니다

SELECT movie_type 영화종류, MAX(sale_amt) 최대매출액, MIN(sale_amt) 최소매출액, SUM(sale_amt) 전체매출액 
FROM mywork.box_office
WHERE YEAR(release_date) = 2019
  && movie_type IS NOT NULL -- NULL 값은 IN, LIKE, = 같은 연산자로 찾을 수 없습니다 
GROUP BY movie_type
ORDER BY 3 DESC; 

SELECT movie_type 영화종류, MAX(sale_amt) 최대매출액, MIN(sale_amt) 최소매출액, SUM(sale_amt) 전체매출액 
FROM mywork.box_office
WHERE YEAR(release_date) = 2019
  && movie_type IS NOT NULL -- NULL 값은 IN, LIKE, = 같은 연산자로 찾을 수 없습니다 
GROUP BY movie_type
WITH ROLLUP;  -- 명시한 컬럼별로 GROUP BY한 결과를 전체 합계해주는 명령어 
