-- 10.view.sql
DROP DATABASE IF EXISTS fisa;
CREATE DATABASE fisa DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

USE fisa;

drop table IF EXISTs emp;
drop table IF EXISTs dept;
DROP TABLE IF EXISTS salgrade;

CREATE TABLE dept (
    deptno               int  NOT NULL ,
    dname                varchar(20),
    loc                  varchar(20),
    CONSTRAINT pk_dept PRIMARY KEY ( deptno )
 );
 
CREATE TABLE emp (
    empno                int  NOT NULL  AUTO_INCREMENT,
    ename                varchar(20),
    job                  varchar(20),
    mgr                  smallint ,
    hiredate             date,
    sal                  numeric(7,2),
    comm                 numeric(7,2),
    deptno               int,
    CONSTRAINT pk_emp PRIMARY KEY ( empno ) -- 중복되지 않고, 고유한 값을 가지고 있는 컬럼 '기본키' 
 );
 
CREATE TABLE salgrade
 ( 
	GRADE INT,
	LOSAL numeric(7,2),
	HISAL numeric(7,2) 
);

-- dept 테이블에 없는 부서에는 emp 테이블의 deptno에 값이 들어오면 튕겨낼거야 
-- fk_emp_dept 
ALTER TABLE emp 
ADD CONSTRAINT fk_emp_dept FOREIGN KEY ( deptno ) REFERENCES dept( deptno ) 
ON DELETE NO ACTION ON UPDATE NO ACTION; 


-- 부서번호, 부서이름, 부서가 있는 지역 
insert into dept values(10, 'ACCOUNTING', 'NEW YORK');
insert into dept values(20, 'RESEARCH', 'DALLAS');
insert into dept values(30, 'SALES', 'CHICAGO');
insert into dept values(40, 'OPERATIONS', 'BOSTON');

desc dept;
desc emp;
desc salgrade;

-- STR_TO_DATE() : 단순 문자열을 날짜 형식의 타입으로 변환 
insert into emp values( 7839, 'KING', 'PRESIDENT', null, STR_TO_DATE ('17-11-1981','%d-%m-%Y'), 5000, null, 10);
insert into emp values( 7698, 'BLAKE', 'MANAGER', 7839, STR_TO_DATE('1-5-1981','%d-%m-%Y'), 2850, null, 30);
insert into emp values( 7782, 'CLARK', 'MANAGER', 7839, STR_TO_DATE('9-6-1981','%d-%m-%Y'), 2450, null, 10);
insert into emp values( 7566, 'JONES', 'MANAGER', 7839, STR_TO_DATE('2-4-1981','%d-%m-%Y'), 2975, null, 20);
insert into emp values( 7788, 'SCOTT', 'ANALYST', 7566, DATE_ADD(STR_TO_DATE('13-7-1987','%d-%m-%Y'), INTERVAL -85 DAY)  , 3000, null, 20);
insert into emp values( 7902, 'FORD', 'ANALYST', 7566, STR_TO_DATE('3-12-1981','%d-%m-%Y'), 3000, null, 20);
insert into emp values( 7369, 'SMITH', 'CLERK', 7902, STR_TO_DATE('17-12-1980','%d-%m-%Y'), 800, null, 20);
insert into emp values( 7499, 'ALLEN', 'SALESMAN', 7698, STR_TO_DATE('20-2-1981','%d-%m-%Y'), 1600, 300, 30);
insert into emp values( 7521, 'WARD', 'SALESMAN', 7698, STR_TO_DATE('22-2-1981','%d-%m-%Y'), 1250, 500, 30);
insert into emp values( 7654, 'MARTIN', 'SALESMAN', 7698, STR_TO_DATE('28-09-1981','%d-%m-%Y'), 1250, 1400, 30);
insert into emp values( 7844, 'TURNER', 'SALESMAN', 7698, STR_TO_DATE('8-9-1981','%d-%m-%Y'), 1500, 0, 30);
insert into emp values( 7876, 'ADAMS', 'CLERK', 7788, DATE_ADD(STR_TO_DATE('13-7-1987', '%d-%m-%Y'),INTERVAL -51 DAY), 1100, null, 20);
insert into emp values( 7900, 'JAMES', 'CLERK', 7698, STR_TO_DATE('3-12-1981','%d-%m-%Y'), 950, null, 30);
insert into emp values( 7934, 'MILLER', 'CLERK', 7782, STR_TO_DATE('23-1-1982','%d-%m-%Y'), 1300, null, 10);


INSERT INTO SALGRADE VALUES (1,700,1200);
INSERT INTO SALGRADE VALUES (2,1201,1400);
INSERT INTO SALGRADE VALUES (3,1401,2000);
INSERT INTO SALGRADE VALUES (4,2001,3000);
INSERT INTO SALGRADE VALUES (5,3001,9999);

COMMIT;

SELECT * FROM DEPT;
SELECT * FROM EMP;
SELECT * FROM SALGRADE;

COMMIT;
/*
1. view 에 대한 학습
	- 물리적으로는 미 존재, 단 논리적으로 존재
	- 하나 이상의 테이블을 조회한 결과 집합의 독립적인 데이터베이스 객체
	- 논리적(존재하는 table들에 종속적인 가상 table)

2. 개념
	- 보안을 고려해야 하는 table의 특정 컬럼값 은닉
	또는 여러개의 table의 조인된 데이터를 다수 활용을 해야 할 경우
	특정 컬럼 은닉, 다수 table 조인된 결과의 새로운 테이블 자체를 
	가상으로 db내에 생성시킬수 있는 기법 

3. 문법
	- create와 drop : create view/drop view
	- crud는 table과 동일
	
	CREATE VIEW view_name AS
	SELECT column1, column2, ...
	FROM table_name
	WHERE condition;
*/

-- mysql 테이블 복사 -> 원본이 새로 생겨나는 개념
-- emp, 연봉이 오르거나, 부서 추가 
CREATE VIEW emp_ AS select * FROM emp;

SELECT * FROM emp_; -- 바로가기 

-- 맨 마지막 행에 1800불 커미션은 안 받는 사람의 정보를 하나 넣어주세요
INSERT INTO emp VALUES (9999, '신짱구', '유치원생', 0, NOW(), 1800, NULL, 40);

-- 1. emp table과 dept table 기반으로 empno, ename, deptno, dname으로 view 생성
CREATE VIEW  emp_dept_v AS SELECT e.empno, e.ename, d.deptno, d.dname 
FROM emp e, dept d
WHERE e.deptno = d.deptno; 

DROP VIEW emp_dept_v;
-- view 생성

select * from emp_dept_v;
select * from dept;
SELECT * FROM emp;

-- dept table의 SALES라는 데이터를 영업으로 변경 후 view 검색
UPDATE dept SET dname='영업' WHERE dname='SALES'; 

-- 새로운 값을 넣고 emp와 dept에 어떤 영향이 있는지 직접 확인해보세요 

-- view는 가짜테이블 밖에서는 테이블인지 아닌지 알 수 없어요.
-- view에서도 값을 변경하거나 삭제하거나 추가할 수 있을까?

-- 순서대로 넣었어도 원본에 있는 컬럼 중 어디에 들어갈 지 적어두셔야 합니다.
-- 2개 이상의 테이블이 걸려있는 view에 대해서는  
INSERT INTO emp_dept_v (empno, ename, deptno, dname) VALUES (NULL, '김연지', 70, '미정'); 
-- emp와 dept에 함께 걸려서 변경할 수 있는 컬럼 x 
UPDATE emp_dept_v SET deptno=30 WHERE ename='짱구'; -- 짱구 부서를 30으로 변경해보시고 dept 
-- emp에만 접근해서 변경할 수 있는 컬럼 o 
UPDATE emp_dept_v SET ename='신짱구' WHERE ename='짱구'; 
-- dept에만 접근해서 변경할 수 있는 컬럼 o 
UPDATE emp_dept_v SET dname='운영' WHERE ename='신짱구'; -- 짱구 이름을 신짱구 -> 짱구로 변경해 보시고 emp 
DELETE FROM emp_dept_v WHERE ename='신짱구'; -- 짱구 정보 행 
-- view에 변경된 사항이 원본에 영향을 미칠까??
-- view에서 값을 변경할 수 있다면 원본의 제약조건의 영향을 받을까??

SELECT * FROM emp;
DESC emp;
DESC dept;
DESC emp_dept_v;
SELECT * FROM emp_dept_v;

-- emp의 empno는 key성질을 여전히 유지할 수 있으므로
-- key preserved table이나, 
-- dept의 deptno는 더 이상 unique 성질을 유지하지 못해
-- key-preserved table이 아니게 됩니다. 
-- 즉 emp table에 속한 empno, ename, deptno만이 변경 가능해집니다. 
-- JOIN VIEW는 많이 사용됩니다. 
-- 값을 변경할 때 1개의 PK만 남게 되므로 1개 테이블의 값만 변경이 가능해진다.

-- 2. view 삭제

-- 3. ? emp table에서 comm을 제외한 emp01_v 라는 view 생성
select * from emp;

CREATE VIEW emp01_v AS SELECT empno, ename, job, mgr, hiredate, sal, deptno FROM emp; 
SELECT * FROM emp01_v;
-- 1개의 테이블에서 유래한 VIEW는 어떻게 동작하는지 

-- ALLEN 이름을 알렌
UPDATE emp01_v SET ename='알렌' WHERE ename='ALLEN'; 

-- 연봉도 올려주시고
UPDATE emp01_v SET sal=sal+100 WHERE ename='알렌'; 

-- 알렌씨를 삭제도 해 주세요 
DELETE FROM emp01_v WHERE ename='알렌'; 
insert into  emp01_v values( 7499, 'ALLEN', 'SALESMAN', 7698, STR_TO_DATE('20-2-1981','%d-%m-%Y'), 1600, 30);


-- 4. dept01_v에 crud : dep01_v와 dept01 table 변화 동시 검색
-- view만 수정해도 원본 table의 데이터가 동기화
-- *** DML은 view에 적용 가능, 원본 table에도 적용 
-- dept01_v에서 50번 부서, '교육', '상암' 
-- emp01_v에다가 여러분의 정보를 넣어주십시오 50번 
CREATE VIEW dept01_v AS SELECT * FROM dept;
SELECT * FROM dept01_v;
INSERT INTO dept01_v VALUES (50, '교육', '상암');
SELECT * FROM dept;
insert into  emp01_v values(NULL, '김연지', '강사', NULL, NOW(), 1000, 50);
SELECT * FROM emp01_v;

-- 5. 모든 end user(클라이언트, 실제로 가장 마지막 단에서 데이터를 조회하게 되는 사용자들) 가 
-- 빈번히 사용하는 sql문장으로 "해당 직원의 모든 정보 검색"하기
-- 내 이름이 아니라 다른 직원 정보를 조회할 때도 보여줘야 할 것 같은 정보와
-- 그렇지 않은 정보를 구분해서 관리해보세요 


	
/* 윈도우 함수 - 익숙해지면 참 좋아요! 
 행과 행 간을 비교, 연산, 정의하기 위한 함수. -- 2019년, 2018년, 2020년 
 분석함수 또는 순위함수라고 부릅니다.
 다른 함수들처럼 중첩해서 사용할 수는 없지만 서브쿼리에서는 사용가능합니다.
 
SELECT WINDOW_FUNCTION(ARGUMENTS) OVER([PARTITION BY 컬럼] [ORDER BY 컬럼] [WINDOWING 절])
FROM 테이블명;

순위 함수:	RANK, DENSE_RANK, ROW_NUMBER	 
   90     1
80 80     2      
   75     4 

3000
2000
1000
1800
1222
4000   3000

일반 집계 함수:	SUM, MAX, MIN, AVG, COUNT	
그룹 내 행 순서 함수: FIRST_VALUE, LAST_VALUE, LAG, LEAD
그룹 내 비율 함수:	RATIO_TO_REPROT, PERCENT_RANK, CUME_DIST, NTILE 등
*/
-- 용량이 아주 큰 DB를 만들어야 할 때 
-- PARTITION BY 라는 구문을 이용하면 80년생 이하는 사람은 emp01, 85년생 이하인 사람 emp02 
-- 논리적으로는 하나의 테이블이지만, 공간을 나누어서 저장을 하게 하는 경우도 있습니다 

# 1) RANK
-- ORDER BY를 포함한 쿼리문에서 특정 컬럼의 순위를 구하는 함수
-- PARTITION 내에서 순위를 구할 수도 있고 전체 데이터에 대한 순위를 구할 수도 있다. 
-- 동일한 값에 대해서는 같은 순위를 부여하며 중간 순위를 비운다.

select * FROM mywork.box_office;
SELECT job, ename, sal, RANK() OVER (PARTITION BY JOB ORDER BY SAL DESC) 
FROM emp;
 
/* 2) DENSE_RANK (밀집, 밀도)
1
2 2
3 

RANK와 작동법은 동일, 동일한 값에 대해서는 
같은 순위를 부여하고 중간 순위를 비우지 않는다. 
동일한 값이 있는 경우 순위는 1,1,2,3,3,4
*/

SELECT job, ename, sal, DENSE_RANK() OVER (PARTITION BY JOB ORDER BY SAL DESC) 
FROM emp;

-- SALESMAN 부서에 신짱아 800 
INSERT INTO emp VALUES (NULL, '신짱아', 'SALESMAN', NULL, NOW(), 800, NULL, 30);
 /* 3) ROW_NUMBER
RANK, DENSE_RANK는 동일한 값에 대해 동일 순위를 부여하지만 
ROW_NUMBER은 동일한 값이어도 고유한 순위를 부여한다.
-- 'A1234' 이전에는 -> 1, 2, 3, 4, 5 -> PK를 임의로 만들어줄 때 사용한다 
*/
SELECT job, ename, sal, ROW_NUMBER() OVER (PARTITION BY JOB ORDER BY SAL DESC) 
FROM emp;

-- abc 순으로 정렬한(collation) 열번호가 매겨짐 
SELECT job, ename, sal, ROW_NUMBER() OVER (ORDER BY ename ASC) 이름순위
FROM emp;

-- 겹치지 않는 번호를 부여해야 할 때, 순위별로 나눌 때도 사용을 하긴 합니다 
-- 순서는 먼저 테이블에 들어간 값이 우선 순위를 부여받습니다 


/* 윈도우 안에서 특정 값을 찾아내는 함수 
1) FIRST_VALUE
파티션별 윈도우에서 가장 먼저 나온 값을 구한다. MIN과 같음.

2) LAST_VALUE
파티션별 윈도우에서 가장 마지막에 나온 값을 구한다.

3) LAG
이전 몇 번째 행의 값을 가져오는 함수. 인자를 최대 3개까지 가진다.
두번째 인자는 몇 번째 앞의 행을 가져올지 결정하는 것이며 DEFAULT값은 1이다. 
세번째 인자는 가져올 행이 없을 경우 DEFAULT값을 지정해준다.

4) LEAD
이후 몇 번째 행의 값을 가져오는 함수로 LAG와 마찬가지로 인자를 최대 3개까지 갖는다. */
SELECT job, ename, sal, FIRST_VALUE(sal) OVER (PARTITION BY job ORDER BY sal ASC) 첫번째값
FROM emp; -- MIN 

SELECT job, ename, sal, FIRST_VALUE(sal) OVER (ORDER BY sal DESC) 첫번째값
FROM emp; -- MIN 

SELECT job, ename, sal, LAST_VALUE(sal) OVER (ORDER BY sal ASC) 첫번째값
FROM emp; -- MAX

SELECT job, ename, sal, FIRST_VALUE(sal) OVER (ORDER BY sal DESC) 마지막값
FROM emp; -- MAX 

SELECT job, ename, sal, FIRST_VALUE(sal) OVER (ORDER BY sal ASC) 마지막값
FROM emp; -- MIN

-- 2번째 인자로는 지금 기준으로 몇개 밀려난 순서에서 값을 가지고 올 것인지를 정해줍니다 
SELECT job, ename, sal, LAG(sal) OVER (ORDER BY sal ASC) LAG_
FROM emp; -- MIN
 
 SELECT job, ename, sal, LAG(sal, 3) OVER (ORDER BY sal ASC) LAG_
FROM emp; -- MIN

 -- NULL인 경우 들어갈 디폴트값이 세번째 인자로 
 SELECT job, ename, sal, LAG(sal, 3, 0) OVER (ORDER BY sal ASC) LAG_
FROM emp; -- MIN
 
 
 SELECT job, ename, sal, LEAD(sal, 3, 0) OVER (ORDER BY sal ASC) LEAD_
FROM emp; -- MIN
DESC emp; 

SELECT job, ename, sal, LEAD(sal, 3, '값없음') OVER (ORDER BY sal ASC) LEAD_
FROM emp; -- MIN

/* 4. 그룹 내 비율 함수
-- 백분위 PERCENT_RANK, 누적비율 CUME_DIST, 상위에서 몇번째-NTILE  
*/

-- 최대값 기준으로 현재 행의 값이 몇 퍼센트 백분위인지 
SELECT job, ename, sal, PERCENT_RANK() OVER (ORDER BY sal ASC) PR_
FROM emp; 

-- 부서별로 직원들이 최대임금 대비 몇퍼센트 정도 임금을 받고 있는지

SELECT job, ename, sal, deptno, ROUND(PERCENT_RANK() OVER (PARTITION BY deptno ORDER BY sal ASC), 2) PR_
FROM emp; 


-- 누적비율 CUME_DIST
SELECT job, ename, sal, deptno, ROUND(CUME_DIST() OVER (PARTITION BY deptno ORDER BY sal ASC), 2) 누적비율
FROM emp; 
	
-- NTILE : 전체 데이터를 특정 기준으로 N개의 그룹으로 나눌 때 
SELECT job, ename, sal, NTILE(5) OVER (ORDER BY sal)
FROM emp; 

SELECT * FROM salgrade;

/* 일반 집계 함수:	SUM, MAX, MIN, AVG, COUNT	
순위 함수: RANK 1 1 3, DENSE_RANK 1 1 2, ROW_NUMBER
그룹 내 행 순서 함수: FIRST_VALUE, LAST_VALUE, LAG, LEAD
그룹 내 비율 함수:	PERCENT_RANK, CUME_DIST, NTILE 등
*/
-- 2번째로 돈 많이 받는 사람
-- 
SELECT ENAME
  FROM (SELECT ENAME, DENSE_RANK() OVER(ORDER BY SAL DESC) AS RN 
		  FROM EMP) AS R
 WHERE RN = 2;
 
 select job, ename, sal, RANK() OVER (order by sal desc)
from emp limit 2;

select * from (select job, ename, sal, RANK() OVER (order by sal desc)
from emp limit 2) s 
order by sal asc
limit 1;

select * from emp;

-- 부서별로 돈을 가장 적게 받는 사람
SELECT e.ename, e.sal, e.sal_min
FROM (SELECT ename, sal, FIRST_VALUE(sal) OVER (PARTITION BY deptno ORDER BY sal ASC) AS sal_min
FROM emp) AS e
WHERE e.sal=e.sal_min; 

select * from(
select job, ename, sal, RANK() OVER (partition by deptno order by sal asc) rank_
from emp) e
where rank_ = 1;

-- 부서별로 가장 돈을 많이 받는 사람 만 따로 쿼리로 만들어서 결과를 출력해주세요
select t.deptno, t.ename, t.sal
from (select deptno, ename, sal, 
	FIRST_VALUE(sal) over (partition by deptno order by sal desc) as max_sal
from emp) as t
where sal = max_sal;


select * from(
select job, ename, sal, RANK() OVER (partition by deptno order by sal desc) rank_
from emp) e
where rank_ = 1;

-- 부서별로 가장 돈을 많이 받는 사람을 'MAXIMUM'이라는 컬럼에 별도로 출력해주세요 
	select * from(
select job, ename as MAXIMUM, sal, RANK() OVER (partition by deptno order by sal desc) sal_
from emp) e
where sal_ = 1;

CREATE VIEW test AS select * from(
select job, ename as MAXIMUM, sal, RANK() OVER (partition by deptno order by sal desc) sal_
from emp) e
where sal_ = 1;
SELECT * FROM test;

-- VIEW는 주로 조회용으로 많이 씁니다. 원본테이블에서 숨기고 싶은 컬럼을 제외하고 출력할 때 
	
	
	
	
	
	
	



	
	
	
	
	
	
	
	
	
	
	
	
	
	


