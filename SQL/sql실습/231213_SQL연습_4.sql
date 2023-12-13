-- 8.DML.sql
/* 
- DML : Data Manupulation Language
            데이터 조작 언어
	   (select(DQL)/insert/update/delete 모두 다 DML)
	   - 이미 존재하는 table에 데이터 저장, 수정, 삭제, 검색 
	   - commit과 rollback(트랜잭션)이 적용되는 명령어
	   	insert/update/delete에만 적용
	   

1. insert sql문법
	1-1. 모든 칼럼에 데이터 저장시 
		insert into table명 values(데이터값1, ...)

	1-2.  특정 칼럼에만 데이터 저장시,
		명확하게 칼럼명 기술해야 할 경우 
		insert into table명 (칼럼명1, ...) values(칼럼과매핑될데이터1...)


2. update -> 특정 조건에 맞는 행을 찾아서 수정 
	2-1. 모든 table(다수의 row)의 데이터 한번에 수정
		- where조건문 없는 문장
		- update table명 set 칼럼명=수정데이타; -- job이라는 컬럼을 만들고 : 회사원, 연봉 컬럼에 모두 100만원을 올려주는 경우 

	2-2. 특정 row값만 수정하는 방법
		- where조건문으로 처리하는 문장
		- update table명 set 칼럼명=수정데이타[, 컬럼명2=수정데이터2,..] where 조건sql;
		
		
3. delete		
	- 존재하는 데이터 삭제

*/

use fisa;

-- *** insert ****
-- 1. 칼럼명 기술없이 데이터 입력
-- table 자체가 생성시에 컬럼 순으로 데이터 값들도 설정해서 저장


-- 데이터 구조만 복제해서 새로 생성
-- empno, ename, deptno emp 테이블을 가지고오는데 구조만 가져와 보세요.



-- 2. 칼럼명 기술후 데이터 입력 
-- 저장하고자 하는 데이터의 순서를 컬럼명 명시하면서 변경 가능


-- null을 허용하는 컬럼에 값 미저장시 특정 컬럼만 명시해서 값 저장 가능
-- DEFALUT 값이 정해진 컬럼을 명시해서 값을 넣지 않으면 DEFAULT 값이 들어갑니다 
/* 제약조건 없는 table에 사원명과 부서번호만 저장시도 : 정상 저장
 * mysql의 empno라는 int타입의 컬럼값이 검색시 0으로 적용되어 있음
 * oracle db의 경우 널 / mysql은 타입에 맞는 즉 정수타입의 기본값으로 자동 저장  
 */




-- 3. 하나의 table에 한번에 데이터 insert하기 
-- , 구분자로 () 표현을 적용해서 저장


-- 4. 데이터만 삭제 - rollback으로 복구 불가능한 데이터 삭제 명령어



-- *** update ***
-- 1. 테이블의 모든 행 변경 UPDATE 테이블명 SET 컬럼명=값



-- deptno값을 모두 50으로 변경



-- 10번 부서 번호를 50으로 변경


#      테이블      변경할 컬럼=변경할 값     조건이 되는 컬럼=기존의 값 


-- 2. ? emp01 table의 모든 사원의 급여를 10%(sal*1.1) 인상하기
-- ? emp table로 부터 empno, sal, hiredate, ename 순으로 table 생성


-- UPDATE 테이블명 SET 변경할컬럼=변경할값 WHERE 조건을탐색할컬럼=기존값;



-- ? 3. emp01의 모든 사원의 입사일을 오늘로 바꿔주세요
select now(), sleep(2), now(); -- 명령문이 실행될 때 한번만 시간을 기록합니다 
select sysdate(), sleep(2), sysdate(); -- 함수가 실행되는 순간의 시간을 기록합니다 



-- ? 4. 급여가 3000이상(where sal >= 3000)인 사원의 급여만 10%인상



-- 5. ?emp01 table 사원의 급여가 1000이상인 사원들의 급여만 500원씩 삭감 
-- insert/update/delete 문장에 한해서만 commit과 rollback 영향을 받음


-- 6. ? emp01 table에 DALLAS(dept의 loc)에 위치한 부서의 소속 사원들의 급여를 1000인상
-- 서브쿼리 사용


-- emp와 dept를 서브쿼리를 통해 연결해서 emp의 부서원정보는 모두 조회되되, 
-- loc이 같이 출력되도록 쿼리문을 작성해주세요




-- 7. ? emp01 table의 SMITH 사원의 부서 번호를 30으로, 직급은 MANAGER 수정
-- 두개 이상의 칼럼값 동시 수정

-- *** delete ***
-- 8. 하나의 table의 모든 데이터 삭제


-- 9. 특정 row 삭제(where 조건식 기준)
-- deptno가 30번 부서의 모든 사원들 삭제

-- 10. emp01 table에서 comm 존재 자체가 없는(null) 사원 모두 삭제


-- 11. emp01 table에서 comm이 null이 아닌 사원 모두 삭제



-- 12. emp01 table에서 부서명이 RESEARCH 부서(dept table의 dname)에 소속된 사원 삭제 
-- 서브쿼리 활용



-- 13. table 전체 내용 삭제

