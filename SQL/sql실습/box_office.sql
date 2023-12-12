USE mywork;

USE mywork;

SELECT sale_amt
FROM mywork.box_office
WHERE sale_amt > 40000000000;

SELECT * FROM box_office;

SELECT movie_type, SUM(sale_amt)   -- 각 행에 대한 결과가 아니라 그룹으로 집계하고 싶은 결과 함수
FROM  mywork.box_office
GROUP BY movie_type; -- 분류에 의한 결과

SELECT movie_type, SUM(sale_amt)   -- 각 행에 대한 결과가 아니라 그룹으로 집계하고 싶은 결과 함수
FROM  mywork.box_office
GROUP BY movie_type-- 분류에 의한 결과
HAVING SUM(sale_amt)> 15000000000 -- GROUP BY로 나눈 뒤의 조건
ORDER BY movie_type , SUM(sale_amt) DESC -- 순서 정렬
LIMIT 2;

# 용량을 줄이거나 속도를 빠르게!
-- SQL함수 : 진짜 많아요. 쓰시게 되는 것만 쓰게 될 거, 똑같은 동작을 하는 여러개 함수 - RDBMS 종류마다 쓰는 함수명을 다 넣어놓은 경우도 있습니다
SELECT CHAR_LENGTH('SQL'), LENGTH('SQL'), CHAR_LENGTH('홍길동👩🏻‍'), LENGTH('홍길동👩🏻‍💻');
# SQL에서 한글 1글자 : 3바이트 LENGTH로 확인

SELECT CONCAT('This', 'Is', 'MySQL', '.') AS CONCAT1,
       CONCAT('SQL', NULL, 'Books') AS CONCAT2, # NULL과 문자열을 연결하면 그 결과는 NULL
       CONCAT_WS(' ', 'This', 'Is', 'MySQL') AS CONCAT_WS;
		# CONCAT_WS() 함수는 구분자인 첫 번째 매개변수가 콤마(,)이므로 두 번째부터 네 번째 매개변수를 연결하면서 그 사이에 구분자 콤마 기입

# sql 언어 거의 유사, 회사마다 서버 종류가 다양
# 문법이나 함수명이 여러 서버에서 혼용가능하도록
SELECT FORMAT(123456789.123456, 4) fmt, -- FORMAT(숫자를 3개씩 끊어서 ,로 출력, 소수점이후 N번째 자리까지 반올림 출력)
       INSTR('ThisIsSQL', 'sql') instring, -- index string, MySQL은 1부터 시작, 윈도우서버 SQL은 대소문자 구분 없음
       LOCATE('my', 'TheMyDBMSMySQL', 5) locates, -- 'TheMyDBMSMySQL'에서 'my'를 찾아줘 5번째인덱스 이후에서
       POSITION('my' IN 'TheMyDBMSMySQL') pos; -- LOCATE('my', 'TheMyDBMSMySQL', 1) 과 같은 동작

SELECT LOWER('ABcD'), LCASE('ABcD'),
       UPPER('abcD'), UCASE('abcD');

SELECT REPEAT('SQL', 3),
       REPLACE('생일 축하해 철수야', '철수', '영희') REP,
       REVERSE('SQL');

# SUBSTR() 함수는 첫 번째 매개변수 str의 문자열에서 두 번째 매개변수 pos로 지정된 위치부터 세 번째 매개변수 len만큼 잘라 반환합니다.
-- len은 생략 가능하며, 생략하면 str의 오른쪽 끝까지 잘라냅니다. 또한 pos 값에 음수도 넣을 수 있는데, 이때는 시작 위치를 왼쪽이 아닌 오른쪽 끝을 기준으로 잡습니다.
-- 그리고 SUBSTRING(), MID() 함수는 SUBSTR() 함수와 사용법이 같습니다.
SELECT SUBSTR('This Is MySQL', 6, 2) FIRST,
       SUBSTRING('This Is MySQL', 6) SECOND,
       MID('This Is MySQL', -5) THIRD; -- 음수인덱싱

SELECT CURDATE(), CURRENT_DATE(), CURRENT_DATE,
       CURTIME(), CURRENT_TIME(), CURRENT_TIME,
       NOW(), CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP;

SELECT DATE_FORMAT('2021-01-20 13:42:54', '%d-%b-%Y') Fmt1,
       DATE_FORMAT('2021-02-20 13:42:54', '%U %W %j') Fmt2;

SELECT STR_TO_DATE('21,01,2021', '%d,%m,%Y') CONV1,
       STR_TO_DATE('19:30:17', '%H:%i:%s') CONV2,
       STR_TO_DATE('09:30:17', '%h:%i:%s') CONV3,
       STR_TO_DATE('17:30:17', '%h:%i:%s') CONV4;  -- ‘19:30:17’에서 시간이 19시로 24시간 형태인데, %h는 12시간 형태이므로 변환에 실패해 결국 NULL을 반환

SELECT SYSDATE(), SLEEP(2), SYSDATE(); -- 매번 함수 호출시의 시간

SELECT NOW(), SLEEP(2), NOW(); -- 문장 단위로 실행됨



SELECT DATE_ADD('2021-01-20', INTERVAL 5 DAY) DATEADD,
	   ADDDATE('2021-01-20', INTERVAL 5 MONTH) ADD_DATE1,
       ADDDATE('2021-01-20', 5 ) ADD_DATE2,
       ADDDATE('2021-01-20', INTERVAL '1 1' YEAR_MONTH) ADD_DATE3;

SELECT DATE_SUB('2021-01-20', INTERVAL 5 DAY) DATEADD,
	   SUBDATE('2021-01-20', INTERVAL 5 MONTH) ADD_DATE1,
       SUBDATE('2021-01-20', 5 ) ADD_DATE2,
       SUBDATE('2021-01-20', INTERVAL '1 1' YEAR_MONTH) ADD_DATE3;

-- EXTRACT() -- 매개변수의 date에서 특정 날짜 단위를 추출한 결과 반환
SELECT EXTRACT(YEAR_MONTH    FROM '2020-01-20 13:32:03') YEARMON,
       EXTRACT(DAY_HOUR      FROM '2020-01-20 13:32:03') DAYHOUR,
       EXTRACT(MINUTE_SECOND FROM '2020-01-20 13:32:03') MINSEC;

-- int('10') type casting
SELECT CAST(10 AS CHAR)                 CONV_CHAR,
       CAST('-10' AS SIGNED )           CONV_INT, -- 양수, 음수 다 받는 자료형
       CAST('10.2131' AS DECIMAL)       CONV_DEC1,
       CAST('10.2131' AS DECIMAL(6, 2)) CONV_DEC2, -- 고정소수점
       CAST('10.2131' AS DOUBLE)        CONV_DOUBLE, -- 부동소수점 -> 앞으로는 뺄거래요
       CAST('2021-10-31' AS DATE)       CONV_DATE,
       CAST('2021-10-31' AS DATETIME)   CONV_DATETIME;

-- CONVERT() 함수도 CAST() 함수와 마찬가지로 형 변환하나, CAST() 함수와 달리 AS type 대신 type을 두 번째 매개변수로 받음
SELECT CONVERT(10, CHAR)                 CONV_CHAR,
       CONVERT('-10', SIGNED)            CONV_INT,
       CONVERT('10.2131', DECIMAL)       CONV_DEC1,
       CONVERT('10.2131', DECIMAL(6, 4)) CONV_DEC2,
       CONVERT('10.2131', DOUBLE)        CONV_DOUBLE,
       CONVERT('2021-10-31', DATE)       CONV_DATE,
       CONVERT('2021-10-31', DATETIME)   CONV_DATETIME;


 -- 흐름제어 함수
# 흐름 제어(flow control) 함수란 특정 조건을 확인해 조건에 부합하는 경우와 그렇지 않은 경우에 다른 값을 반환하는 함수
# 흐름 제어 함수에는 IF(), IFNULL(), NULLIF() 함수가 있고, 흐름 제어 함수와 비슷한 역할을 하는 CASE 연산자도 있다
SELECT IF(2 > 1, 1, 0) IF1,  -- IF(조건, 참일때 리턴값, 거짓일 때 리턴값)
       IF('A' = 'a', 'SAME', 'NOT SAME') IF2, -- window의 MYSQL에서는 대소문자 구분 X
       IF(1 = 2, 1, 'A') IF3;

-- NULLIF() 함수는 두 매개변수 expr1과 expr2 값이 같으면 NULL을, 같지 않으면 expr1을 반환
SELECT NULLIF(1, 1) NULLIF1,
       NULLIF(1, 0) NULLIF2,
       NULLIF(NULL, NULL) NULLIF3;

SELECT CASE 1 WHEN 0 THEN 'A' -- CASE 값 WHEN 첫번째 명제 THEN 첫번째 명제가 참일 경우 출력할 값
              WHEN 1 THEN 'B' --         WHEN 두번째 명제 THEN 두번째 명제가 참일 경우 출력할 값
       END CASE1,             --         ELSE 앞의 모든 명제가 거짓인 경우 출력할 값
							  -- END 해당 조건을 부르기 위한 ALIAS
       CASE 9 WHEN 0 THEN 'A'
              WHEN 1 THEN 'B'
              ELSE 'None'
       END CASE2,
       CASE WHEN 25 BETWEEN 1 AND 19 THEN '10대' -- 범위 지정도 가능합니다
            WHEN 25 BETWEEN 20 AND 29 THEN '20대'
            WHEN 25 BETWEEN 30 AND 39 THEN '30대'
            ELSE '30대 이상'
       END CASE3;

-- DATABASE()와 SCHEMA() 함수는 현재 접속해 있는 데이터베이스 이름을, USER() 함수는 현재 로그인한 사용자 이름을 반환
SELECT DATABASE(), SCHEMA(), USER(); -- MYSQL에서는 DATABASE(), SCHEMA()가 동일합니다

-- 실습.
# 1. box_office 테이블에서 2015년 이후 개봉한 영화 중 연도별로 2번 이상
# 관객수 100만을 넘긴 영화의 감독과 해당 관객의 영화를 본 관객수를
# 연도별, 감독별로 구하는 쿼리를 작성하세요.

-- 나의 답 : 아래 코드 수정 필요 => 오답
select Year(release_date), director, movie_name
from mywork.box_office
where audience_num >= 1000000 and Year(release_date) >= 2015
group by Year(release_date), director, movie_name;
-- having count(movie_name)>=2;

SELECT YEAR(release_date), director, SUM(audience_num), COUNT(*), movie_name
  FROM box_office
 WHERE YEAR(release_date) >= 2015
   AND audience_num >= 1000000
 GROUP BY 1, 2
HAVING COUNT(*) > 1
 ORDER BY 1, 2;

-- 정답
select Year(release_date), director, sum(audience_num)
from mywork.box_office
where audience_num >= 1000000 and Year(release_date) >= 2015
group by Year(release_date), director
having count(director) >= 2
ORDER BY 3 DESC;


# 2. 2019년 1분기(QUARTER 함수 사용) 개봉 영화 중 매출액이 천만 원 이상인 영화의 월별, 영화 유형별 매출액 소계를 구하는 쿼리
select Month(release_date), movie_type, sum(sale_amt)
from mywork.box_office
where YEAR(release_date)=2019 AND QUARTER(release_date) = 1 AND sale_amt >= 10000000
group by Month(release_date), movie_type
with ROLLUP;

-- 정답
select Month(release_date), movie_type, sum(sale_amt)
from mywork.box_office
where YEAR(release_date)=2019 AND QUARTER(release_date) = 1 AND sale_amt >= 10000000
group by Month(release_date), movie_type
with ROLLUP;

SELECT MONTH(release_date), IF(GROUPING(movie_type) = 1, '소계', movie_type) 영화유형, SUM(sale_amt)
FROM box_office
WHERE YEAR(release_date) = 2019 AND QUARTER(release_date) = 1
 AND sale_amt >= 10000000
GROUP BY MONTH(release_date), movie_type WITH ROLLUP;


/* 3. 2019년 개봉 영화 중 매출액이 천만 원 이상인 영화의 월별(MONTH), 영화 유형별 매출액 소계를 구하되
	7월 1일 전에 개봉한 영화이면 상반기,
	7월 1일 이후에 개봉한 영화이면 하반기라고 함께 출력하는 쿼리 */
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY','')); #
select @@sql_mode;

-- select if(Month(release_date)<7, 상반기, 하반기) 상하반기, Month(release_date)
-- movie_type, sum(sale_amt)
-- from mywork.box_office
-- where Year(release_date) = 2019 AND sale_amt >= 10000000
-- group by Month(release_date), movie_type;

select if(Month(release_date)<7, '상반기', '하반기') as `상하반기`,
movie_type, sum(sale_amt) as `Total Sales`
from mywork.box_office
where Year(release_date) = 2019 AND sale_amt >= 10000000
group by Month(release_date), movie_type
WITH ROLLUP;

-- 정답
# sql_mode 를 수정한다면, group by에 없는 값이여도 가능
# sql_mode 를 수정하지 않는다면, group by도 select 구문에 필요한 컬럼이 존재해야함!

/*
SELECT @@sql_mode;
SET SESSION sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

select month(release_date), movie_type, sum(sale_amt), case when month(release_date) <= 6 then '상반기' else '하반기' end as a
from mywork.box_office
where year(release_date) = 2019 and sale_amt >= 10000000
group by month(release_date), movie_type, a
;

select month(release_date), movie_type, sum(sale_amt), case when month(release_date) <= 6 then '상반기' else '하반기' end
from mywork.box_office
where year(release_date) = 2019 and sale_amt >= 10000000
group by month(release_date), movie_type;
*/

SELECT MONTH(release_date) 월별, movie_type 영화유형, SUM(sale_amt) 총계, IF(MONTH(release_date) > 6, '하반기', '상반기')
FROM box_office
WHERE YEAR(release_date) = 2019
 AND sale_amt >= 10000000
GROUP BY MONTH(release_date), movie_type, IF(MONTH(release_date) > 6, '하반기', '상반기')
ORDER BY 1;

select month(release_date), movie_type, sum(sale_amt), case when month(release_date) <= 6 then '상반기' else '하반기' end as a
from mywork.box_office
where year(release_date) = 2019 and sale_amt >= 10000000
group by month(release_date), movie_type, a;


-- 4. 부제가 있는 영화 찾기 ':' 2015년 이후의 개봉영화 중에서 부제가 달려있는 영화의 개수 세어보기
select count(*)
from mywork.box_office
where Year(release_date) >= 2015 and movie_name like '%:%';

-- 정답
SELECT year(release_date), COUNT(movie_name) -- 총 영화의 개수로 한번 나눠서 비율을 봐야
FROM box_office
WHERE year(release_date) >= 2015 AND movie_name LIKE '%:%' -- _ 는 딱 한개
GROUP BY year(release_date)
ORDER BY 1;

-- 추가 문제 풀이 => todo: 수정 필요
-- 6. 부제가 있는 영화 찾기 ':' 2015년 이후의 개봉영화 중에서 부제가 달려있는 영화의 개수 세어보기
SELECT year(release_date), COUNT(movie_name),  -- 총 영화의 개수로 한번 나눠서 비율을 봐야
FROM box_office
WHERE year(release_date) >= 2015 AND movie_name LIKE '%:%' -- _ 는 딱 한개
GROUP BY year(release_date)
ORDER BY 1;

select year(release_date), count(movie_name) as A
from box_office
where year(release_date) >= 2015
group by year(release_date)
order by year(release_date);

-- 정답
-- 6. 부제가 있는 영화 찾기 ':' 2015년 이후의 개봉영화 중에서 부제가 달려있는 영화의 개수 세어보기
SELECT year(release_date), COUNT(movie_name) -- 총 영화의 개수로 한번 나눠서 비율을 봐야
FROM box_office
WHERE year(release_date) >= 2015
GROUP BY year(release_date)
ORDER BY 1;

SELECT
    YEAR(release_date),
    movie_name,
    IF(movie_name LIKE '%:%', 1, 0)
FROM
    box_office
WHERE
    YEAR(release_date) >= 2015
ORDER BY 1;

SELECT year(release_date), COUNT(movie_name) 전체개봉편수, SUM(IF(movie_name LIKE '%:%', 1, 0)) 부제있는편수,  ROUND(SUM(IF(movie_name LIKE '%:%', 1, 0))/COUNT(movie_name)*100, 2) "전체영화 중 부제있는 영화 비율" -- 총 영화의 개수로 한번 나눠서 비율을 봐야
FROM box_office
WHERE year(release_date) >= 2015 -- _ 는 딱 한개
GROUP BY  year(release_date)
ORDER BY 1;


/*  5. 감독이 두 명 이상이면 콤마(,)로 이어져 있습니다(예, ‘홍길동,김감독’). 감독이 1명이면 그대로,
   두 명 이상이면 콤마 대신 ‘/’ 값으로 대체해(예, ‘홍길동/김감독’) 출력하는 쿼리를 작성해 보세요. */
SELECT
    REPLACE(director, ',', '/') director
FROM
    mywork.box_office
WHERE
    director LIKE '%,%';

-- 정답
SELECT director, REPLACE(director, ',', '/')
FROM box_office;

-- *은 웬만하면 쓰지 않는다. 속도 면에서도, 용량 면에서, 유지보수 면에도 좋지 않기 때문에
SELECT *, REPLACE(director, ',', '/')
FROM box_office;

SELECT CONCAT(years, '년에 제작된 영화 편수는 ', count(movie_name), '편 입니다') AS 결과
FROM box_office
WHERE years = 2019;
