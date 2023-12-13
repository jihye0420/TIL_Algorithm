-- 7.DDL.sql - DATABASE DEFINITION LANGAUGE 
-- table 생성(create)과 삭제(drop), table 구조 수정(alter)
-- DDL(Data Definition Language)

/* TCL
 * - 트랜잭선 처리 명령어
 *  - insert/update/delete(DML) 문장에 한해서만 영향을 줌
 *  - table create/drop/alter(DDL) 명령어와 무관
 * - commit
 * - rollback 
 */

/*
 DB에 데이터를 CRUD 작업 가능하게 해주는 기본 구성
   
[1] table 생성 명령어
    create table table명(
    칼럼명1 칼럼타입[(사이즈)] [제약조건] ,
    칼럼명2....
    ); 

[2] table 삭제 명령어
  drop table table명;
  - 삭제 시도시 table 미존재시 에러 발생

[3] table 구조 수정 명령어
  alter table table명
*/

use fisa;

-- mysql상에서의 table 목록 검색 
show tables; 

-- 1. table삭제 
-- 존재해야만 실행 에러가 없는 drop 문장
DROP TABLE test;

-- 존재 여부 확인 후에 존재할 경우에만 삭제하는 drop 문장
DROP TABLE IF EXISTS test;

-- 2. table 생성  
-- name(varchar(5) NULL 안 들어가도록, age(int) 칼럼 보유한 people table 생성
-- name은 최대 5개 글자 크기의 문자열 데이터 저장 
DROP TABLE IF EXISTS people; 

CREATE TABLE people (
	name varchar(5) NOT NULL,
    age int
);

-- 2-1. people 테이블에 값이 들어가게 데이터 튜플을 2개 넣어보시고,
-- INSERT INTO 테이블명 VALUES (넣어야하는값1, 넣어야하는값2, ....);
-- INSERT INTO 테이블명 (값을 넣을 컬럼명) VALUES (넣어야하는값1);
INSERT INTO people VALUES ('김연지', 5);
INSERT INTO people (name, age) VALUES ('김연재', 6);
INSERT INTO people (name) VALUES(234); -- 자동으로 name 컬럼의 자료형인 varchar로 형변환

-- 2-2. 절대 안 들어갈 것 같은 경우의 수를 고려하여 데이터 튜플을 3개 넣어보세요 
INSERT INTO people VALUES('김수한무짱구', 5); -- 자료형이 안 맞고
INSERT INTO people VALUES('짱구'); -- 개수가 안맞고
INSERT INTO people VALUES('짱짱구', 4294967296); -- int 자릿수가 안 맞고 
INSERT INTO people VALUES(NULL, 42949); -- NULL이 들어갈 수 없는 컬럼에 NULL을 넣어서 안 맞고
INSERT INTO people (name) VALUES('짱짱짱구', 42949); -- 명시한 컬럼개수와 값의 개수가 맞지 않아서 안 들어가고
INSERT INTO people (name) VALUES(429496);  -- 자리수가 안 맞아서 안 들어갑니다 
insert into people values (null, 10);
insert into people values ('김', 12, '2');
insert into people values ('김이박', '박이김');

-- 3. 서브 쿼리 활용해서 emp01 table 생성(이미 존재하는 table기반으로 생성)
-- 구조와 데이터는 복제 가능하나 제약조건은 적용 불가
-- 제약조건 만드는 방법 1. 테이블을 만들 때 걸어주는 방법 
DROP TABLE IF EXISTS emp01; 

CREATE TABLE emp01 SELECT * FROM emp;
SELECT * FROM emp03;
CREATE TABLE emp02 AS SELECT * FROM emp;

-- 거짓 조건(WHERE)식 적용시에는 table 구조만 복제
CREATE TABLE emp03 AS SELECT * FROM emp WHERE 1=0;
DESC emp03;
DESC emp;

--               2. 이미 만들어진 테이블에 ALTER 명령어 사용 
-- ALTER 테이블/데이터베이스명 ADD / DROP 제약조건, 추가할조건을 걸어줍니다
ALTER TABLE emp03 ADD 부서명 VARCHAR(10); -- 이미 있는 테이블에 컬럼 추가
DESC emp03;
ALTER TABLE emp03 DROP 부서명; -- 이미 있는 테이블에서 컬럼 삭제 
ALTER TABLE emp03 MODIFY 부서명 VARCHAR(100); -- 이미 있는 컬럼의 조건(자료형) 변경  

-- 제약조건도 같은 명령어 구조를 사용해서 추가하거나 삭제합니다. 
ALTER TABLE emp03 ADD CONSTRAINT PRIMARY KEY (empno); -- CONSTRAINT 제약조건 (걸 컬럼명)
DESC emp03;
ALTER TABLE emp03 DROP PRIMARY KEY; -- 이미 있는 제약조건을 삭제, Primary Key는 테이블에 하나뿐이라 따로 이름을 지정해줄 필요가 없습니다  

-- 4. 서브쿼리 활용해 특정 칼럼(empno)만으로 emp02 table 생성
DROP TABLE IF EXISTS emp02; 
CREATE TABLE emp02 SELECT empno FROM emp;
SELECT * FROM emp02;

INSERT INTO emp02 VALUES (1111);

-- emp02는 emp와 상관있을까? 상관없음. DB는 '데이터'를 처리하기 위한 서비스. 깊은복사 
SELECT * FROM emp;

-- 5. deptno=10 조건문 반영해서 empno, ename, deptno로 emp03 table 생성
DROP TABLE IF EXISTS emp03; 
CREATE TABLE emp03 SELECT empno, ename, deptno FROM emp WHERE deptno=10;
SELECT empno, ename, deptno FROM emp WHERE deptno=10;
SELECT * FROM emp03;


-- 6. 데이터 insert없이 table 구조로만 새로운 emp04 table생성 
-- 사용되는 조건식 : where=거짓, 제약조건이 실제로 복사되지 않는지 확인해보세요 
CREATE TABLE emp04 SELECT empno, ename, deptno FROM emp WHERE 1=10;
SELECT * FROM emp04;

-- 7. ALTER - 이미 존재하는 table의 구조를 변경하는 sql 명령어
-- 만약 원래 데이터가 들어있는 테이블에 컬럼을 추가하면 어떻게 될까요?
-- emp03에 부서명 varchar(5) 컬럼을 넣어주세요 
ALTER TABLE emp03 ADD 부서명 varchar(5); 
-- NULL이 들어간 새 테이블이 만들어집니다 
SELECT * FROM emp03;

-- 새 컬럼 추가(ADD), 삭제(DROP)
ALTER TABLE emp03 DROP 부서명;
 
-- 이미 값이 있는 컬럼을 DROP하면 어떻게 될까요? 
ALTER TABLE emp03 DROP deptno; -- 걍 사라져버립니다 

-- 이미 있는 컬럼의 자료형(OR 크기) 수정(MODIFY)
-- ename int / ename varchar(2) 
ALTER TABLE emp03 MODIFY ename int; 
-- 줄일 때는 이미 있는 값보다 더 줄일 수 있을까?? 
ALTER TABLE emp03 MODIFY ename VARCHAR(2); 
SELECT * FROM emp03;

-- 형변환이 가능한 자료형끼리는 이미 값이 있어도 변환해줍니다 
ALTER TABLE emp03 MODIFY empno VARCHAR(10); 

-- 새 제약조건 추가, 삭제
-- empno UNIQUE 
ALTER TABLE emp03 ADD CONSTRAINT PRIMARY KEY (empno); -- CONSTRAINT 제약조건 (걸 컬럼명)
ALTER TABLE emp03 ADD CONSTRAINT UNIQUE (empno); -- 중복된 값이 없으므로 
 DESC emp03;
-- 이미 값이 있는 컬럼을 DROP하면 어떻게 될까요? 
ALTER TABLE emp03 DROP PRIMARY KEY; -- 이미 있는 제약조건을 삭제, Primary Key는 테이블에 하나뿐이라 따로 이름을 지정해줄 필요가 없습니다  
ALTER TABLE emp03 DROP INDEX empno; 
-- 내부적으로 값을 빨리 조회하기 위한 인덱스 역할을 하기 때문에 
-- UNIQUE로 제약조건을 걸고 INDEX로 삭제합니다 


-- 8. emp01 table에 job이라는 특정 칼럼 추가(job varchar(10))
-- 최대 10byte 문자열 저장 가능한 job 컬럼 생성 및 추가 
SELECT * FROM emp01;
ALTER TABLE  emp01 ADD job varchar(10); -- 이미 있는 컬럼명으로는 새 컬럼 추가할 수 없음 
ALTER TABLE  emp01 ADD job_ varchar(10);

-- 9. 이미 존재하는 칼럼 사이즈 변경 시도해 보기
-- 데이터 미 존재 칼럼의 사이즈 수정(크게/작게 다 수정 가능)
-- modify : 컬럼 변경
ALTER TABLE emp01 MODIFY job varchar(10); 

-- job 크기를 10으로 변경


-- 10. 이미 데이터가 존재할 경우 칼럼 사이즈가 큰 사이즈의 컬럼으로 변경 가능 
-- alter table emp01 modify job varchar(3);  실패 
desc emp01;


-- 11. job 칼럼 삭제 
-- 데이터 존재시에도 자동 삭제 
-- drop 

-- add시 필요 정보(컬럼명 타입(사이즈)) / modify 필요 정보(컬럼명 타입(사이즈)) / drop 필요 정보(컬럼명)
DELETE FROM emp01 WHERE ename='SMITH'; -- 행단위 삭제
DELETE FROM emp01; -- 모든 값이 삭제 


-- 11. table 자체가 아닌  순수 데이터만 완벽하게 삭제하는 명령어 
truncate emp02;
select * from emp01;
-- commit 불필요


-- delete 



commit; -- 데이터의 무결성을 보장하기 위해서, 속도, 효율성 
-- WORKBENCH는 기본적으로 autocommit이 걸려있어서 자동으로 db에 변경이 되었는데요 
SELECT @@autocommit;
SET @@autocommit=0;

-- DB는 빠른 속도, 적은 용량 중심으로 구현이 되어 있기 때문에 
commit; -- AUTOCOMMIT이 지정되어 있지 않다면 UPDATE, DELETE 같은 작업은 실제로 COMMIT 하기 전에는 원DB에는 반영되지 않습니다 
rollback;   -- commit 이후에 작업된 내용에 한해서만 복원(임시 메모리에 저장되었던 작업을 무효화), 삭제 작업 무효화

DROP TABLE IF EXISTS emp01;
CREATE TABLE emp01 SELECT empno, ename FROM emp;
select * from emp01;
delete from emp01 where ename='ALLEN';
select * from emp01;
delete from emp01;
select * from emp01;
rollback;  -- delete 문장 무효화, 데이터 복구
select * from emp01; 
-- 마지막 commit 덩어리 이후의 문장이 모두 무효화되었으므로 ALLEN도 남아있음

delete from emp01 where ename='ALLEN';
commit; -- commit을 완료해버렸으므로
select * from emp01;
rollback; 
select * from emp01; -- ALLEN 복구 불가 

TRUNCATE emp01; -- TRUNCATE는 실행 즉시 COMMIT 해버리므로 ROLLBACK 명령어가 통하지 않음
rollback; 
select * from emp01; 

SET @@autocommit=1;
SELECT @@autocommit;