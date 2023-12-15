-- -- 어제 해결하지 못했던 상황을 trigger로 해결해보세요 

-- 0. 주문수량 음수값 들어올 때 : 명우

-- 1. order, product 수량 초과 시 에러 

-- 2. order 테이블에서 주문을 취소하였을 때 백업용 (삭제)

-- 3. order 상품 주문을 변경(주문 qauntity, 상품 번호)하였을 때 백업용 => (주문에 대한 변경)

-- 4. 주문을 하지 않았을 때(데이터 잘못 되었을 때 나는 에러를 백업용으로 처리) / 0.0 order product_id, cus_id 존재하지 않아도 에러처리

-- 5. 회원정보 삭제 시 백업용 (백업)

-- 6. 회원정보 grade를 변경 시 백업용 (백업)

-- 2번 : 지혜
-- 6번 : 광열
-- 0번 : 명우
-- 5번 : 예선

-- 2. order 테이블에서 주문을 취소하였을 때 백업용 (삭제)

/* AWS market 에서 확인 */
USE enf;
SELECT * FROM customer;
SELECT * FROM `order`;
SELECT * FROM product;

SELECT * FROM backup_order;
-- DROP TRIGGER IF EXISTS test_trg_jihye;

-- DELIMITER // 
-- CREATE TRIGGER test_trg_jihye  -- 트리거 이름
--     AFTER DELETE -- 삭제후에 작동하도록 지정
--     ON `order` -- 트리거를 부착할 테이블
--     FOR EACH ROW -- 각 행마다 적용시킴
-- BEGIN
-- 	SET @msg = '주문 정보가 삭제되어 해당 데이터 백업합니다!!!!!!!' ; -- 트리거 실행시 작동되는 코드들
-- END // 
-- DELIMITER ;

DROP TABLE IF EXISTS backup_order;
CREATE TABLE backup_order
	(ord_id int,
    cus_id int,
    prod_id int,
    ord_quantity int,
    del_date datetime);

DROP TRIGGER IF EXISTS backtable_update_trg;
DELIMITER // 
CREATE TRIGGER backtable_update_trg  -- 트리거 이름
    AFTER DELETE -- 변경 후에 작동하도록 지정
    ON `order` -- 트리거를 부착할 테이블
    FOR EACH ROW 
BEGIN
    INSERT INTO backup_order VALUES( OLD.ord_id, OLD.cus_id, OLD.prod_id, 
        OLD.ord_quantity, NOW());
	SET @msg = '주문 정보가 삭제되어 해당 데이터 백업합니다!!!!!!!' ; -- 트리거 실행시 작동되는 코드들
END // 
DELIMITER ;

DELETE FROM `order` WHERE ord_id=7;
SELECT * FROM backup_order;
SELECT @msg;

-- jihye 2
DROP TRIGGER IF EXISTS test_trg_jihye;

DELIMITER //
CREATE TRIGGER test_trg_jihye
	BEFORE INSERT
	ON `order`
	FOR EACH ROW
BEGIN
    DECLARE prod_qty INT;

    SELECT prod_quantity INTO prod_qty
    FROM product
    WHERE prod_id = NEW.prod_id;

    IF NEW.ord_quantity > prod_qty THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'ord_Quantity cannot be more than prod_Quantity.';
    END IF;
END //
DELIMITER ;

-- 명우
DELIMITER //
CREATE TRIGGER check_quantity
	BEFORE INSERT 			-- 삭제 되면 작동
	ON `enf`.`order`		-- 어떤 테이블에?
    FOR EACH ROW			-- 각 row(행) 마다 적용

-- 테이블에 백업데이터 삽입
BEGIN
	iF NEW.ord_quantity < 0 THEN
		SET @msg= '주문 수량이 정확하지않아요' ; -- 트리거 실행시 작동되는 코드들
	end if;
END // 
DELIMITER ;

INSERT INTO `order` (cus_id, prod_id, ord_quantity) VALUES (5, 5, 111);
INSERT INTO `order` (cus_id, prod_id, ord_quantity) VALUES (5, 5, -1);


-- DROP TRIGGER IF EXISTS customer_before_insert_trg;

-- INSERT INTO orders VALUES (100, 1, 2, 100);
-- DELETE FROM orders WHERE ord_id=100;

-- SELECT * FROM backup_order;
-- SET @msg = 0;
-- SELECT @msg;


-- select * from customers;
-- INSERT INTO customers (cus_username, cus_birthdate) VALUES ('tester1', '1111-11-11');
-- -- 회원에게 입력받은 생년월일을 확인하여 올바른 값으로 변경하는 예제 

-- DROP TRIGGER IF EXISTS test_trg_jihye;

-- DELIMITER // 
-- CREATE TRIGGER test_trg_jihye  -- 트리거 이름
--     AFTER INSERT -- 입력 후에 작동하도록 지정
--     ON `order` -- 트리거를 부착할 테이블
--     FOR EACH ROW 
-- BEGIN
--     IF NEW.order_quantity < product.prod_quantity THEN
-- 		-- insert 되지 않도록 쿼리문 작성
--     END IF;
-- END // 
-- DELIMITER ;

-- INSERT INTO customers VALUES (NULL, 'tester2', '1899-01-01');
-- SELECT * FROM customers;
-- INSERT INTO customers VALUES (NULL, 'tester3', '2100-01-01');
-- SELECT * FROM customers;



