use fisa;

-- 스칼라 서브쿼리 : 결과가 하나의 값으로 도출
-- 내부쿼리 -> 외부쿼리 동작
-- 내부쿼리에서는 외부쿼리의 from절에서 사용한 테이블 참조 가능
-- 외부쿼리에서는 내부쿼리에서 사용한 테이블 참조 불가능
-- 1. SELECT절에서는 스칼라 서브쿼리만 쓸 수 있음

SELECT d.dname='ACCOUNTING'
FROM dept d
WHERE e.deptno = d.deptno;

SELECT e.ename
FROM emp e;

-- 내부쿼리에서는 외부쿼리의 from절에서 사용한 테이블 참조 가능
SELECT e.ename, e.deptno, (SELECT d.dname='ACCOUNTING' 
FROM dept d WHERE e.deptno = d.deptno) AS ACCOUNTING
FROM emp e;

-- 외부쿼리에서는 내부쿼리에서 사용한 테이블 참조 불가능
SELECT e.ename, d.deptno, (SELECT d.dname='ACCOUNTING' 
FROM dept d WHERE e.deptno = d.deptno) AS ACCOUNTING
FROM emp e;

-- 2. FROM 절에서의 서브쿼리 => 별명을 사용(from절에 쓰인 내부쿼리에서)
-- 파생(derived) 서브 쿼리: FROM 절에 있는 서브쿼리 → 조건에 맞는 파생 테이블을 반환, 별명을 붙여서 외부쿼리에서 사용합니다
-- 꼭 별칭을 붙여서 외부 쿼리문에서는 별칭으로 사용 가능
-- 서브 쿼리가 반환하는 결과 집합을 하나의 테이블처럼 사용하는 쿼리문
-- 서브 쿼리 안에서 사용가능
-- 내부 쿼리에서는 외부쿼리의 from절에서 사용한 테이블 참조 불가능
-- 외부 쿼리에서는 내부쿼리에서 사용한 테이블 참조 불가능
-- FROM -> WHERE -> SELECT 


-- 서브 쿼리
SELECT 
    b.deptno, b.empno, c.ename
FROM
    emp b,
    emp c
WHERE
    b.empno = c.empno;

-- 외부 쿼리
SELECT 
    a.deptno, a.dname
FROM
    dept a
ORDER BY 1;


SELECT 
    a.deptno, a.dname, mgr.empno
FROM
    dept a,
    (SELECT 
        b.deptno, b.empno, c.ename
    FROM
        emp b, emp c
    WHERE
        b.empno = c.empno) mgr # 별명 필요!
WHERE
    a.deptno = mgr.deptno
ORDER BY 1;

 -- emp 테이블에서 SMITH 직원명 검색해서 
 -- 어떤 부서인지 dept 테이블에서 찾아서 출력하기
 
-- join으로 해결
select d.deptno, d.dname
from emp e, dept d 
where e.deptno=d.deptno and e.ename='SMITH';

-- 서브 쿼리로 해결
select d.deptno, d.dname
from dept d
where d.deptno = (select e.deptno from emp e where e.ename='SMITH');

-- smith 씨와 동일한 research 부서를 가진 모든 사원의 이름 출력
select p.ename
from emp p
where p.deptno = (select e.deptno
from emp e
where e.ename='SMITH');

-- SMITH 씨랑 급여가 같거나 더 많은 사원명과 급여를 검색해주세요
-- SMITH 씨를 넣어서도, 제외해서도 출력해보세요 
select * from emp;

select e.ename, e.sal
from emp e
where e.sal >= (select m.sal
from emp m
where m.ename = 'SMITH');

select e.ename, e.sal
from emp e
where e.sal >= (select m.sal
from emp m
where m.ename = 'SMITH') and e.ename != 'SMITH';

-- SMITH 씨랑 급여가 같거나 더 많은 사원명과 급여를 검색해주세요
SELECT ename, sal, deptno -- 사원명과 급여
FROM emp
WHERE sal >= ALL (SELECT sal 
FROM emp
WHERE ename = 'SMITH') -- 조건 1 스미스 급여만 검색해야 합니다. 서브쿼리에 사용한 컬럼수가 메인쿼리에서 비교할 컬럼수와 일치
	AND ename != 'SMITH' -- 조건 2. 스미스 씨는 아니어야 합니다 
    AND deptno != (SELECT deptno 
FROM emp
WHERE ename = 'SMITH');-- 조건 3. 부서가 스미스와 같지 않아야합니다. 


-- 급여가 3000불 이상인 사원이 소속된 부서(10, 20)에 속한 사원 이름, 급여를 출력
select e.ename, e.sal
from emp e
where e.sal >= 3000 and e.deptno in (10, 20);

-- job이 매니저인 사람이 어느 부서에만 있는지 서브쿼리 통해 출려 
select deptno, dname, loc from dept where deptno in (
select deptno
from emp 
where job = 'MANAGER');


use mywork;
-- 다른 연산자 없이 단독으로 사용. 실습
SELECT ranks, movie_name, director
  FROM box_office
 WHERE YEAR(release_date) = 2019
   AND movie_name IN (SELECT movie_name
                        FROM box_office
                       WHERE YEAR(release_date) = 2018);

SELECT ranks, movie_name, release_date, sale_amt, rep_country
  FROM box_office
 WHERE YEAR(release_date) = 2019
   AND ranks BETWEEN 1 AND 100
   AND rep_country NOT IN (SELECT rep_country
                             FROM box_office
                            WHERE YEAR(release_date) = 2018
                              AND ranks BETWEEN 1 AND 100);

-- EXISTS 연산자는 메인쿼리 테이블의 값 중에서 서브쿼리의 결과 
-- 집합에 존재하는 건이 있는지를 확인하는 역할
SELECT ranks, movie_name, director
  FROM box_office a
 WHERE YEAR(release_date) = 2019
   AND EXISTS (SELECT 1
                 FROM box_office b
                WHERE YEAR(release_date) = 2018
                  AND a.movie_name = b.movie_name);


  SELECT ranks, movie_name, director
    FROM box_office
   WHERE YEAR(release_date) = 2019
     AND movie_name NOT IN (SELECT movie_name
                          FROM box_office
                         WHERE YEAR(release_date) = 2018);

  SELECT ranks, movie_name, director
    FROM box_office a
   WHERE YEAR(release_date) = 2019
     AND EXISTS (SELECT 1
                   FROM box_office b
                  WHERE YEAR(release_date) = 2018
                    AND a.movie_name = b.movie_name);

use fisa;

SELECT ename, sal, deptno
FROM emp
WHERE deptno IN (SELECT deptno
				FROM emp
				WHERE sal >= 3000); 

SELECT ename, sal, deptno
FROM emp e1
WHERE EXISTS (SELECT 1  # 0, 3, 4, 2 ...를 넣어도 동작함! => 무엇이어도 상관없는 => 공갈문자!
				FROM emp e2
                where e1.deptno = e2.deptno); 

SELECT ename, sal, deptno
FROM emp e1
WHERE e1.sal >= 3000
and EXISTS (SELECT 1  # 0, 3, 4, 2 ...를 넣어도 동작함! => 무엇이어도 상관없는 => 공갈문자!
				FROM emp e2
                where e1.deptno = e2.deptno);
        
SELECT ename, sal, deptno
FROM emp
WHERE sal >= 3000 AND EXISTS(SELECT 1
FROM emp
WHERE deptno in (10, 20));

SELECT ename, sal, deptno
FROM emp e1
WHERE sal >= 3000 AND deptno IN (10, 20) AND 
EXISTS (SELECT 1 FROM emp e2);

-- 각 부서별로 sal가 가장 높은 사람 # todo: 아래 내용 다시 보기
-- select deptno, ename, max(sal)
-- from emp
-- group by deptno
-- having max(sal);

-- select deptno, ename, count(ename) from emp group by deptno;

-- 각 부서별로 SAL가 가장 높은 사람은 누구일까요? 
SELECT  MAX(sal), deptno
FROM emp
GROUP BY deptno; -- deptno라는 단위로 묶였는데 ename을 보고 싶다고 해서 

SELECT ename, sal, deptno
FROM emp
WHERE sal IN (SELECT MAX(sal)
FROM emp
GROUP BY deptno); -- 서브쿼리에 group by를 사용할 수 있다 
				  -- group by로는 볼 수 없던 행별 정보를 서브쿼리로 추출한 테이블로 필터링해서 꺼낼 수 있다 
                  
SELECT ename, sal, deptno
FROM emp
WHERE (deptno, sal) IN (SELECT deptno, MAX(sal)
FROM emp
GROUP BY deptno);      
-- IN 연산자는 여러개 컬럼의 값을 비교해서 꺼낼 수 있습니다
-- 단 순서가 맞아야 합니다 

-- FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
-- 행이 많으면 속도가 느려지기 때문에 가장 행을 앞단에서 줄일 수 있는 순서
-- 테이블은 메인쿼리에서 먼저 가져옵니다 
-- 여기에 더해서 서브쿼리가 먼저 동작하기 때문에 서브쿼리를 최대한 간소한 결과가 나오도록 작성해주시면 좋습니다 


                       
-- 어차피 동작도 서브쿼리부터 하고, 서브쿼리가 길어서 뭘 하는지 안 보인다면 
-- 따로 빼줘도 좋지 않을까요 
-- CTE, Common Table Expression FROM 절에서는 사용하기 위한 파생 테이블의 별명을 붙여서 사용할 수 있습니다 
use fisa;

with mgr as (SELECT b.deptno, b.empno, c.ename
					  FROM emp b, emp c
					 WHERE b.empno = c.empno) -- as 뒤에 있는 쿼리로 만들어진 테이블을 메인 쿼리에서 mgr이라고 부르겠다는 의미
SELECT a.deptno, a.dname, mgr.empno
FROM dept a
WHERE a.deptno = mgr.deptno
ORDER BY 1;


use MYWORK;
SELECT ranks, movie_name, director
  FROM box_office
 WHERE YEAR(release_date) = 2019
   AND movie_name NOT IN (SELECT movie_name
                        FROM box_office
                       WHERE YEAR(release_date) = 2018);

use MYWORK;

-- CTE는 FROM 절에서만 쓸 수 있다 
WITH where2 AS (SELECT movie_name
                        FROM box_office
                       WHERE YEAR(release_date) = 2018)
                       
SELECT ranks, movie_name, director
  FROM box_office
 WHERE YEAR(release_date) = 2019
   AND movie_name NOT IN where2;