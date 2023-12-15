use student_mgmt;

SELECT * FROM students;
SELECT COUNT(*) FROM students WHERE gender = 'man';  -- count = 
SELECT 'Many men' AS result; 
SELECT SYSDATE() AS 지금시간; 

show procedure status; -- 프로시저 목록 확인
show create procedure sakila.film_in_stock; -- 프로시저 내용 확인
drop procedure 프로시저이름; -- 프로시저 삭제

select * from student_mgmt.students;
select count(*) from students where gender='man'; # 남자인 개수


-- 1. gender가 'man'인 학생들의 수를 세는 스토어드 프로시저 예제
DELIMITER // # //로 시작 해서 //로 끝난다는 구분자 설정
CREATE PROCEDURE count_men() # count_men()이라는 프로시저 확인
BEGIN # 시작
    DECLARE count INT; # 지역 변수
    SELECT COUNT(*) INTO count FROM students WHERE gender = 'man';
    IF count > 3 THEN
        SELECT 'Many men' AS result; # print문과 같은 의미
    ELSE
        SELECT 'Few men' AS result;
    END IF;
END // # 끝
DELIMITER ;

-- 프로시저 삭제
drop procedure count_men;

select * from students;
call count_men(); -- CALL 함수명()

SHOW PROCEDURE STATUS;
SHOW CREATE PROCEDURE count_men; -- 내부적으로 변수명으로 관리됨 __function__
DROP PROCEDURE count_men;

-- ? 82년생 이상 학생 수를 세는 예제:  birth year가 1982년 이전인 학생들의 수를 세는 
-- 스토어드 프로시저 예제를 만들어보세요.
use student_mgmt;

select * from students;


# 82년생 2명 이상 있으면 나이 많은 사람 있음
-- IF 문을 사용하여 birth year가 1982년 이전이면 'Many older students'을 반환하고, 
-- 그렇지 않으면 'Few older students'를 반환합니다.
DELIMITER $$
CREATE PROCEDURE count_old()
BEGIN
    DECLARE count INT;
    SELECT COUNT(*) INTO count FROM students WHERE YEAR(birth) < 1982;
    IF count >= 8 THEN
        SELECT 'Many older students' AS result;
	ELSEIF count >= 5 and count < 8 THEN
        SELECT 'soso' AS result;
    ELSE
        SELECT 'Few older students' AS result;
    END IF;
END $$
DELIMITER ;

call count_old(); -- CALL 함수명()


-- if ~ elif~ else: 
-- if ~ else if~ else:
-- if ~ elseif~ else:

SELECT COUNT(*) FROM students;

DROP PROCEDURE count_older_students;



CALL print_math_scores();
DROP PROCEDURE print_math_scores;

/* 동적 SQL
- 상황에 따라 내용 변경이 필요할 때는 동적 SQL을 사용하면 변경되는 내용을 실시간으로 적용해 사용 가능.
- PREPARE~EXCUTE가 대표적입니다. PREPARE문에서는 ?로 향후 입력될 값을 비워놓고, EXCUTE문에서 USING으로 ?에 값을 전달. 
- 실행 후에는 DEALLOCATE PREPARE로 문장을 해제해주는 것이 좋음.
- 동적 쿼리는 보안상 취약할 수 있으므로, 사용 전 반드시 적절한 검증과 예외 처리를 수행해야 함.
- 예시: 보안이 중요한 출입문에서 출입증을 태그하는 순간마다 날짜와 시간을 생성하여 INSERT할 때
*/
DROP TABLE IF EXISTS gate_table;
CREATE TABLE gate_table (id INT AUTO_INCREMENT PRIMARY KEY, entry_time DATETIME);
INSERT INTO gate_table VALUES(NULL, SYSDATE());

PREPARE myQuery FROM 'INSERT INTO gate_table VALUES(NULL, SYSDATE())'; -- 동적 쿼리를 만듦 

EXECUTE myQuery;

SELECT * FROM gate_table;

DEALLOCATE PREPARE myQuery; # 메모리에서 제거

-- SELECT문에서 행의 개수를 제한하는 LIMIT문에는 변수를 사용할 수 없습니다. 
-- 이 때도 PREPARE, EXCUTE문을 사용합니다. 

use world;
select * from country;
SET @count = 3;
PREPARE mySQL FROM 'SELECT code, name, continent, region, population
  FROM country
 WHERE population > 100000000
 ORDER BY 1 ASC
 LIMIT ?';
EXECUTE mySQL USING @count;


/* Trigger

어떤 테이블에서 특정한 이벤트(update, insert, delete)가 발생했을 때, 
실행시키고자 하는 추가 쿼리 작업들을 자동으로 수행할 수 있게끔 트리거를 미리 설정해 두는 것. 

트리거는 직접 실행시킬 수 없고 오직 해당 테이블에 이벤트가 발생할 경우에만 실행됩니다. 
DML에만 작동되며, MySQL에서는 VIEW에는 트리거를 사용할 수 없습니다.

DELIMITER $$

CREATE TRIGGER 트리거이름
    AFTER DELETE -- 트리거를 달 동작
    ON 테이블 FOR EACH ROW
BEGIN
    -- 문장
END$$    

DELIMITER ;


- BEFORE/AFTER는 명령 키워드가 사용된 후에 처리할지 아니면 끝난 후 처리할지를 나타냅니다.
- 또한 처리할 내용 부분에서 OLD, NEW로 명령 키워드로 변경되는 테이블에 접근할 수 있습니다.
    - ( OLD : 변경되기 전 테이블, NEW : 변경된 후 테이블 )
- 프로시저는 특정 경우에만 동작시킨다면, 트리거는 매번 DML이 실행될 때마다 동작합니다.

*/

USE market;
SELECT * FROM customers;

DROP TRIGGER IF EXISTS test_trg;
DELIMITER // 
CREATE TRIGGER test_trg  -- 트리거 이름
    AFTER  DELETE -- 삭제후에 작동하도록 지정
    ON orders -- 트리거를 부착할 테이블
    FOR EACH ROW -- 각 행마다 적용시킴
BEGIN
	SET @msg = '주문 정보가 삭제됨' ; -- 트리거 실행시 작동되는 코드들
END // 
DELIMITER ;

DELETE FROM orders WHERE ord_id=??;
SELECT @msg;

DROP TABLE IF EXISTS backup_order;
CREATE TABLE backup_order
	(ord_id int,
    cus_id int,
    pro_id int,
    ord_quantity int,
    del_date datetime);

DROP TRIGGER IF EXISTS backtable_update_trg;
DELIMITER // 
CREATE TRIGGER backtable_update_trg  -- 트리거 이름
    AFTER DELETE -- 변경 후에 작동하도록 지정
    ON orders -- 트리거를 부착할 테이블
    FOR EACH ROW 
BEGIN
    INSERT INTO backup_order VALUES( OLD.ord_id, OLD.cus_id, OLD.pro_id, 
        OLD.ord_quantity, CURDATE());
END // 
DELIMITER ;

DELETE FROM orders WHERE ord_id=??;

SELECT * FROM backup_order;
-- 현재 문제 없나요??? 

DROP TRIGGER IF EXISTS customer_before_insert_trg;

DELIMITER // 
CREATE TRIGGER customer_before_insert_trg  -- 트리거 이름
    BEFORE INSERT -- 입력 전에 작동하도록 지정
    ON customers -- 트리거를 부착할 테이블
    FOR EACH ROW 
BEGIN
    IF NEW.cus_birthdate < 1900 THEN
        SET NEW.cus_birthdate = 0;
    ELSEIF NEW.cus_birthdate > YEAR(CURDATE()) THEN
        SET NEW.cus_birthdate = CURDATE();
    END IF;
END // 
DELIMITER ;

INSERT INTO customers VALUES (NULL, 'tester1', '1899-01-01');
SELECT * FROM customers;
INSERT INTO customers VALUES (NULL, 'tester3', '2100-01-01');
SELECT * FROM customers;
