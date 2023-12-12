# SQL 변수는 테이블명, 컬럼명과 구분하기 위해 @를 앞에 달아줌
SET @변수이름 = 변수의 값; -- 변수 선언 및 값 대입
SELECT @변수이름; -- 변수의 값 출력

SET @count = 5;
SELECT code, name, continent, region, population
  FROM world.country
 WHERE population > 100000000
 ORDER BY @count ASC; 

SET @count = 1;
select @count;

SELECT YEAR(release_date), director, SUM(audience_num), COUNT(*) -- * 대신 아무 컬럼이나 넣어도 행 수를 리턴하는 것은 같습니다.
  FROM box_office
 WHERE YEAR(release_date) >= 2015
   AND audience_num >= 1000000
 GROUP BY 1, 2
HAVING COUNT(*) > count
 ORDER BY 1, 2;

SET @count = 1;
SELECT YEAR(release_date), director, SUM(audience_num), COUNT(*)
  FROM box_office
 WHERE YEAR(release_date) >= 2015
   AND audience_num >= 1000000
 GROUP BY count, 2
HAVING COUNT(*) > count
 ORDER BY 1, 2;

SELECT YEAR(release_date), director, SUM(audience_num), COUNT(*)
  FROM box_office
 WHERE YEAR(release_date) >= 2015
   AND audience_num >= 1000000
 GROUP BY count, 2
HAVING COUNT(*) > 1
 ORDER BY count, 2;
 
# SQL 변수에는 group by, having, where, order by절에서는 동작하지 않습니다.
-- 동적 SQL 
PREPARE mySQL FROM 
'SELECT YEAR(release_date), director, SUM(audience_num), COUNT(*)
  FROM box_office
 WHERE YEAR(release_date) >= 2015
   AND audience_num >= 1000000
 GROUP BY 1, 2
HAVING COUNT(*) > ?
 ORDER BY 1, 2;';
EXECUTE mySQL USING @count; 
 
PREPARE mySQL1 FROM 'SELECT YEAR(release_date), director, SUM(audience_num), COUNT(*)
  FROM mywork.box_office
 WHERE YEAR(release_date) >= 2015
   AND audience_num >= 1000000
 GROUP BY 1, 2
HAVING COUNT(*) > ?
 ORDER BY ?, 2;';
EXECUTE mySQL1 USING @count, @count;  -- 순서대로 여러개 넣음 






