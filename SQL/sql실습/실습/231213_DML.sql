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

-- 1. table삭제 
-- 존재해야만 실행 에러가 없는 drop 문장

-- 존재 여부 확인 후에 존재할 경우에만 삭제하는 drop 문장


-- 2. table 생성  
-- name(varchar(5), age(int) 칼럼 보유한 people table 생성
-- name은 최대 5개 글자 크기의 문자열 데이터 저장 


-- 2-1. people 테이블에 값이 들어가게 데이터 튜플을 2개 넣어보시고,


-- 2-2. 절대 안 들어갈 것 같은 경우의 수를 고려하여 데이터 튜플을  3개 넣어보세요 


-- 3. 서브 쿼리 활용해서 emp01 table 생성(이미 존재하는 table기반으로 생성)
-- 구조와 데이터는 복제 가능하나 제약조건은 적용 불가
-- 제약조건 만드는 방법 1. 테이블을 만들 때 걸어주는 방법 
--               2. 이미 만들어진 테이블에 ALTER 명령어 사용 



-- 거짓 조건(WHERE)식 적용시에는 table 구조만 복제



-- 4. 서브쿼리 활용해서 특정 칼럼(empno)만으로 emp02 table 생성


-- 5. deptno=10 조건문 반영해서 empno, ename, deptno로 emp03 table 생성


-- 6. 데이터 insert없이 table 구조로만 새로운 emp04 table생성 
-- 사용되는 조건식 : where=거짓, 제약조건이 실제로 복사되지 않는지 확인해보세요 


-- 7. ALTER - 이미 존재하는 table의 구조를 변경하는 sql 명령어

-- 만약 원래 데이터가 들어있는 테이블에 컬럼을 추가하면 어떻게 될까요?
-- NULL이 들어간 새 데이터프레임이 만들어집니다 

-- 새 컬럼 추가(ADD), 삭제(DROP)

-- 이미 값이 있는 컬럼을 DROP하면 어떻게 될까요? 

-- 이미 있는 컬럼의 자료형(OR 크기) 수정(MODIFY)

-- 줄일 때는 이미 있는 값보다 더 줄일 수 있을까?? 

-- 새 제약조건 추가, 삭제



-- 8. emp01 table에 job이라는 특정 칼럼 추가(job varchar(10))

-- 최대 10byte 문자열 저장 가능한 job 컬럼 생성 및 추가 


-- 9. 이미 존재하는 칼럼 사이즈 변경 시도해 보기
-- 데이터 미 존재 칼럼의 사이즈 수정(크게/작게 다 수정 가능)
-- modify : 컬럼 변경

-- job 크기를 10으로 변경


-- 10. 이미 데이터가 존재할 경우 칼럼 사이즈가 큰 사이즈의 컬럼으로 변경 가능 
-- alter table emp01 modify job varchar(3);  실패 
desc emp01;


-- 11. job 칼럼 삭제 
-- 데이터 존재시에도 자동 삭제 
-- drop 

-- add시 필요 정보(컬럼명 타입(사이즈)) / modify 필요 정보(컬럼명 타입(사이즈)) / drop 필요 정보(컬럼명)


-- 11. table 자체가 아닌  순수 데이터만 완벽하게 삭제하는 명령어 
-- commit 불필요


-- delete 



commit; -- 데이터의 무결성을 보장하기 위해서, 속도, 효율성 
-- WORKBENCH는 기본적으로 autocommit이 걸려있어서 자동으로 db에 변경이 되었는데요 
SELECT @@autocommit;
SET @@autocommit=1;

commit; -- AUTOCOMMIT이 지정되어 있지 않다면 UPDATE, DELETE 같은 작업은 실제로 COMMIT 하기 전에는 원DB에는 반영되지 않습니다 
rollback;   -- commit 이후에 작업된 내용에 한해서만 복원(임시 메모리에 저장되었던 작업을 무효화), 삭제 작업 무효화


