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

SELECT * FROM student_mgmt.students;

-- 성별 기준으로 수학점수의 평균 
select gender, avg(math)
from student_mgmt.students
group by gender;

-- -- 성별 기준으로 수학점수의 평균 
select gender, avg(math)
from student_mgmt.students
group by gender # 원본은 그대로, 원본 테이블에 없는 값을 계산
having avg(math) >=60
order by gender DESC
LIMIT 1; # group by 결과에서 조건을 만족하는 값만 조회

-- -- 성별 기준으로 수학점수의 평균 
select gender, avg(math) 수학평균, max(math), min(math)
from student_mgmt.students
group by gender # 원본은 그대로, 원본 테이블에 없는 값을 계산
having avg(math) >= 60; # group by의 결과에서 조건을 만족하는 값만 조회 


select distinct rep_country from mywork.box_office;

-- 1. 실습: students 테이블에서 수학점수와 영어점수의 평균이 70점 이상인 사람들만 출력하려면?
-- 2. 성별 평균을 구하고 70점이 넘는 수학점수와 영어점수의 평균이 70점 이상인 사람들만 출력하려면?
-- 3. # 연도별 개봉한 영화의 편수를 집계해서 출력해주세요
-- 4. # 2019년 개봉 영화의 유형별 최대, 최소 매출액과 전체 매출액 집계하기

# 1. 
select name, AVG(math), AVG(english)
from student_mgmt.students
group by name
having AVG(math) >= 70 and AVG(english) >= 70;

SELECT name, math, english
FROM student_mgmt.students
WHERE math >= 70 && english >= 70;

SELECT name, math, english, ((math + english) /2) >= 70
FROM student_mgmt.students
WHERE ((math + english) /2) >= 70;

# 2.
-- select gender,sum(math)+sum(english)+sum(korean)/3 as '평균', avg(math), avg(english)
-- from student_mgmt.students
-- group by gender
-- having sum(math)+sum(english)+sum(korean)/3 > 70 and AVG(math) >= 70 and AVG(english) >= 70;

select gender,sum(math)+sum(english)+sum(korean)/3 as '평균'
from student_mgmt.students
group by gender;
-- having sum(math)+sum(english)+sum(korean)/3 > 70 and AVG(math) >= 70 and AVG(english) >= 70;


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
GROUP BY name, gender
HAVING 
	avg(english) >= 70 AND avg(math) >= 70; -- GROUP BY 이후의 조건을 판별합니다 

INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('dave', 'man ', '1983-07-16', 90, 80, 71);
SELECT DISTINCT gender FROM student_mgmt.students; 
SELECT * FROM students;
INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('dave ', 'man  ', '1983-07-16', 90, 80, 71);
SELECT DISTINCT name FROM student_mgmt.students; 
INSERT INTO students (name, gender, birth, english, math, korean) VALUES (' dave ', 'man  ', '1983-07-16', 90, 80, 71);
SELECT DISTINCT name FROM student_mgmt.students; 


# 3.
select YEAR(release_date), count(*)
from mywork.box_office
group by YEAR(release_date)
order by 2 DESC;

# 4. 2019년 개봉 영화의 유형별 최대, 최소 매출액과 전체 매출액 집계하기
SELECT 
    movie_type,
    MIN(sale_amt),
    MAX(sale_amt),
    SUM(sale_amt)
FROM
    mywork.box_office
WHERE
    YEAR(release_date) = 2019
        AND movie_type IS NOT NULL
GROUP BY movie_type;

SELECT movie_type, MAX(sale_amt), MIN(sale_amt), SUM(sale_amt) 
FROM mywork.box_office
WHERE YEAR(release_date) = 2019 
  && movie_type IS NOT NULL -- NULL 값은 IN, LIKE, = 같은 연산자로 찾을 수 없습니다 
GROUP BY movie_type;


SELECT 
    release_date,
    movie_type,
    MIN(sale_amt),
    MAX(sale_amt),
    SUM(sale_amt)
FROM
    mywork.box_office
GROUP BY YEAR(release_date), movie_type
HAVING YEAR(release_date) = 2019;

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
