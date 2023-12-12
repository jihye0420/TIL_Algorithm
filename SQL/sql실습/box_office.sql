-- 실습.
# 1. box_office 테이블에서 2015년 이후 개봉한 영화 중 연도별로 2번 이상
# 관객수 100만을 넘긴 영화의 감독과 해당 관객의 영화를 본 관객수를
# 연도별, 감독별로 구하는 쿼리를 작성하세요.
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

# 2. 2019년 1분기(QUARTER 함수 사용) 개봉 영화 중 매출액이 천만 원 이상인 영화의 월별, 영화 유형별 매출액 소계를 구하는 쿼리
select Month(release_date), movie_type, sum(sale_amt)
from mywork.box_office
where QUARTER(release_date) = 1 AND sale_amt >= 10000000
group by Month(release_date), movie_type
with ROLLUP;

/* 3. 2019년 개봉 영화 중 매출액이 천만 원 이상인 영화의 월별(MONTH), 영화 유형별 매출액 소계를 구하되
	7월 1일 전에 개봉한 영화이면 상반기,
	7월 1일 이후에 개봉한 영화이면 하반기라고 함께 출력하는 쿼리 */
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

select if(Month(release_date)<7, 상반기, 하반기) 상하반기, Month(release_date)
movie_type, sum(sale_amt)
from mywork.box_office
where Year(release_date) = 2019 AND sale_amt >= 10000000
group by Month(release_date), movie_type;

select if(Month(release_date)<7, '상반기', '하반기') as `상하반기`,
movie_type, sum(sale_amt) as `Total Sales`
from mywork.box_office
where Year(release_date) = 2019 AND sale_amt >= 10000000
group by Month(release_date), movie_type
WITH ROLLUP;

-- 4. 부제가 있는 영화 찾기 ':' 2015년 이후의 개봉영화 중에서 부제가 달려있는 영화의 개수 세어보기
select count(*)
from mywork.box_office
where Year(release_date) >= 2015 and movie_name like '%:%';


/*  5. 감독이 두 명 이상이면 콤마(,)로 이어져 있습니다(예, ‘홍길동,김감독’). 감독이 1명이면 그대로,
   두 명 이상이면 콤마 대신 ‘/’ 값으로 대체해(예, ‘홍길동/김감독’) 출력하는 쿼리를 작성해 보세요. */
select REPLACE(director, ',', '/') director
from mywork.box_office
where director like '%,%';


