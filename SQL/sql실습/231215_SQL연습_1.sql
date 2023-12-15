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

DESC emp;
INSERT INTO emp VALUES (1, '신짱구', '유치원생', 2, now(), 800, null, 70); 
-- 신짱구를 40번 부서로 넣은 후
INSERT INTO fisa.emp VALUES (1, '신짱구', '유치원생', 2, now(), 800, null, 40); 
 -- 50으로 변경해주시고, 삭제  
 SELECT * FROM fisa.emp;
 UPDATE fisa.emp SET deptno=50 WHERE ename='신짱구';
DELETE FROM fisa.emp WHERE ename='신짱구';

-- 지하철에 없는 역 번호가 있어서 고생을 많이했다 


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
*
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


-- 맨 마지막 행에 1800불 커미션은 안 받는 사람의 정보를 하나 넣어주세요


-- 1. emp table과 dept table 기반으로 empno, ename, deptno, dname으로 view 생성


-- view 생성

select * from emp_dept_v;
select * from dept;
-- dept table의 SALES라는 데이터를 영업으로 변경 후 view 검색

-- 새로운 값을 넣고 emp와 dept에 어떤 영향이 있는지 직접 확인해보세요 

-- emp의 empno는 key성질을 여전히 유지할 수 있으므로
-- key preserved table이나, 
-- dept의 deptno는 더 이상 unique 성질을 유지하지 못해
-- key-preserved table이 아니게 됩니다. 
-- 즉 emp table에 속한 empno, ename, deptno만이 변경 가능해집니다. 
-- JOIN VIEW는 많이 사용됩니다. 
-- 값을 변경할 때 1개의 PK만 남게 되므로 1개 테이블의 값만 변경이 가능해진다.

-- 2. view 삭제

-- 3. ? emp table에서 comm을 제외한 emp01_v 라는 view 생성


-- empno, ename, job 만으로 생성해보기

-- 4. dept01_v에 crud : dep01_v와 dept01 table 변화 동시 검색
-- view만 수정해도 원본 table의 데이터가 동기화
-- *** DML은 view에 적용 가능, 원본 table에도 적용 


-- 5. 모든 end user(클라이언트, 실제로 가장 마지막 단에서 데이터를 조회하게 되는 사용자들) 가 
-- 빈번히 사용하는 sql문장으로 "해당 직원의 모든 정보 검색"하기
-- emp, dept, salgrade 테이블을 참조하여 직원용 테이블을 VIEW로 구성해보세요
-- 내 이름이 아니라 다른 직원 정보를 조회할 때도 보여줘야 할 것 같은 정보와
-- 그렇지 않은 정보를 구분해서 관리해보세요 

	

	
	/* 윈도우 함수 - 익숙해지면 참 좋아요! 
 행과 행 간을 비교, 연산, 정의하기 위한 함수. -- 2019년, 2018년, 2020년 
 분석함수 또는 순위함수라고 부릅니다다.
 다른 함수들처럼 중첩해서 사용할 수는 없지만 서브쿼리에서는 사용가능합니다.
 
SELECT WINDOW_FUNCTION(ARGUMENTS) OVER([PARTITION BY 컬럼] [ORDER BY 컬럼] [WINDOWING 절])
FROM 테이블명;

순위 함수:	RANK, DENSE_RANK, ROW_NUMBER	 
90     1
80 80  2 
75     4 

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


  
/* 2) DENSE_RANK (밀집, 밀도)
1
2 2
3 

RANK와 작동법은 동일, 동일한 값에 대해서는 같은 순위를 부여하고 중간 순위를 비우지 않는다. 
동일한 값이 있는 경우 순위는 1,1,2,3,3,4
*/

 
 /* 3) ROW_NUMBER
RANK, DENSE_RANK는 동일한 값에 대해 동일 순위를 부여하지만 
ROW_NUMBER은 동일한 값이어도 고유한 순위를 부여한다.
*/


-- abc 순으로 정렬한(collation) 열번호가 매겨짐 


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

 
 -- 2번째 인자로는 지금 기준으로 몇개 밀려난 순서에서 값을 가지고 올 것인지를 정해줍니다 

 
 -- NULL인 경우 들어갈 디폴트값이 세번째 인자로 

 
/* 4. 그룹 내 비율 함수
-- 백분위, 누적비율, 상위에서 몇번째 
*/

	
	
	
	
	
	
	
	
	
	
	
	
	
	



	
	
	
	
	
	
	
	
	
	
	
	
	
	


