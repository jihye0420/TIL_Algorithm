use fisa;

-- 스칼라 서브쿼리 : 결과가 하나의 값으로 도출
-- 내부쿼리 -> 외부쿼리 동작
-- 내부쿼리에서는 외부쿼리의 from절에서 사용한 테이블 참조 가능
-- 외부쿼리에서는 내부쿼리에서 사용한 테이블 참조 불가능
-- SELECT절에서는 스칼라 서브쿼리만 쓸 수 있음

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

-- FROM 절에서의 서브쿼리 => 별명을 사용(from절에 쓰인 내부쿼리에서)
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