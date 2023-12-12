SELECT * FROM mywork.box_office;
select count(*) from box_office;

-- DML
# 1. 모든 값 조회
SELECT * FROM box_office; # 와일드 카드는 웬만하면 실무에서 사용하지 않는 것이 좋음 / 각각의 컬럼명을 써주는 것을 권장(속도와 유지보수 측면)
select count(*) from box_office; # 함수 사용
select movie_name, rep_country from box_office; # 컬럼명
select * from box_office where years=2004 or years=2005; # 조건절
select * from box_office where years between 2004 and 2005; # 조건절
select * from box_office where 2004<=years<=2005; # 두개 이상의 비교 연산자는 불가능!!!!!!!!!
select * from box_office where 2004<=years and years<=2005;
select * from box_office where 2004<=years && years<=2005;

-- 문자열
SELECT * FROM box_office where movie_name LIKE '천년';
SELECT * FROM box_office where movie_name LIKE '천년%'; # 천년으로 시작
SELECT * FROM box_office where movie_name LIKE '%천년'; # 천년으로 끝나는
SELECT * FROM box_office where movie_name LIKE '%천년%'; # 천년으로 시작, 끝나는 상관없이
SELECT * FROM box_office where movie_name LIKE '_천년';
SELECT * FROM box_office where movie_name LIKE '천년_';
SELECT * FROM box_office where movie_name LIKE '_천년';

SELECT * FROM box_office where movie_name LIKE '%여우%';
SELECT * FROM box_office where movie_name LIKE '%천년%';
SELECT * FROM box_office where movie_name LIKE '%천년%' OR movie_name LIKE '%여우%';
SELECT * FROM box_office where movie_name LIKE '%천년%' || movie_name LIKE '%여우%';
SELECT * FROM box_office where movie_name LIKE '%여우%' AND years=2007;
SELECT * FROM box_office where movie_name LIKE '%여우%' && years=2007;
select * from box_office 
 where movie_name 
 IN (select movie_name 
     from box_office 
     where movie_name like '%천년%' or '%여우%');

-- 1. 2018년 개봉한 한국 영화 조회하기
-- 2. 2019년 개봉 영화 중 관객수가 500만 명 이상인 영화 조회하기
-- 3. 2019년 개봉 영화 중 관객수가 500만 명 이상이거나 매출액이 400억 원 이상인 영화 조회하기
-- 4. 2012년에 제작됐지만, 2019년에 개봉된 영화를 조회하기.
-- 5. 위 데이터를 “특이사항”이라는 열 이름으로 출력하기.
# 1.
SELECT * FROM box_office where release_date like '2018%' AND rep_country LIKE '한국';
# 2.
SELECT * FROM box_office where release_date like '2019%' and audience_num >=5000000;
# 3.
SELECT * FROM box_office where release_date like '2019%' and (audience_num >=5000000 or sale_amt>=40000000000);
# 4.
SELECT * FROM box_office where years=2012 and release_date like '2019%';
# 5.
SELECT movie_name as '특이사항', years "제작 년도" from box_office where years=2012 and release_date like '2019%';


SELECT name, continent, region
  FROM world.country
 WHERE population > 50000000
 ORDER BY continent, region DESC;
 
SELECT code, name, continent, region, population
  FROM world.country
 WHERE population > 100000000
 ORDER BY 5 ASC; -- 컬럼명을 구체적으로 쓰는대신 컬럼의 순서를 명시하는 방법도 있음
 
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
 
-- 1. 2019년 개봉하고 500만 명 이상의 관객을 동원한 매출액 기준 상위 5편의 영화만 조회
-- 2. 2019년 제작한 영화 중 관객수 1~10위 영화를 조회
-- 3. box_office 테이블에서 2019년 제작된 영화 중 영화 유형(movie_type 칼럼)이 장편이 아닌 영화를 순위(ranks)대로 조회

# 1.
SELECT 
    *
FROM
    box_office
WHERE
    release_date LIKE '2019%'
        AND audience_num >= 5000000
ORDER BY sale_amt DESC
LIMIT 5;

# 2.
SELECT 
    *
FROM
    box_office
WHERE
    years = 2019
order by audience_num DESC
LIMIT 10;

# 3. box_office 테이블에서 2019년 제작된 영화 중 영화 유형(movie_type 칼럼)이 장편이 아닌 영화를 순위(ranks)대로 조회
SELECT 
    *
FROM
    box_office
WHERE
    years = 2019 AND movie_type != '장편'
ORDER BY ranks;


