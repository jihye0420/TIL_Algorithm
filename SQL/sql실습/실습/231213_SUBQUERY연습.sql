## SQL 실행순서
-- FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

USE fisa;

SELECT * FROM dept;
DESC dept;

SELECT * FROM emp;
DESC dept;

-- 모든 부서의 정보와 함께 커미션이 있는 직원들의 커미션과 이름을 조회해 보세요.
SELECT ename, comm, deptno
FROM emp 
WHERE comm > 0;

SELECT ename, comm, deptno
FROM emp 
WHERE comm IS NOT NULL; -- NULL은 값이 아니라 값없음 이기 때문에 IS 로 확인합니다. 

-- 모든 부서의 부서별 연봉에 대한 총합과 평균과 표준편차를 구하고
-- 모든 부서의 사원수를 구해 보세요.
SELECT deptno, AVG(sal), SUM(sal), STD(sal), COUNT(*)
FROM emp
GROUP BY deptno;	


-- 각 관리자의 부하직원수와 부하직원들의 평균연봉을 구해 보세요.
SELECT * FROM emp;

SELECT * FROM emp WHERE job = 'MANAGER';

--  관리자 별로 부하직원수를 찾을 때 

SELECT mgr, SUM(sal), COUNT(*)
FROM emp
GROUP BY mgr;

# Sub-Query 
-- 쿼리 안쪽에 쿼리를 넣을수 있다.
-- where 절에서의 서브쿼리
-- scott과 같은 부서에 있는 직원 이름을 검색해 보세요.

SELECT deptno
				FROM emp
				WHERE ename='SCOTT';

SELECT ename, deptno
FROM emp
WHERE deptno = (SELECT deptno
				FROM emp
				WHERE ename='SCOTT')
	AND ename != 'SCOTT';
    

-- 직무(job)가 Manager인 사람들이 속한 부서의 부서번호와 부서명 , 지역을 조회해 보세요.
	-- manager 사람들이 다수이기 때문에 where절에 in 을 활용!


SELECT deptno, dname, loc
FROM dept
WHERE deptno IN (SELECT deptno
				FROM emp
				WHERE job='MANAGER');

SELECT deptno, dname, loc
FROM dept
WHERE deptno IN (10, 20, 30);

# from 절에서의 서브쿼리
-- emp 테이블에서 급여가 2000이 넘는 사람들의 이름과 부서번호, 부서이름, 지역 조회해 보세요.

SELECT e.ename, d.deptno, d.dname, d.loc -- FROM절의 파생테이블은 외부쿼리에서도 사용할 수 있습니다 
FROM (SELECT ename, deptno
		FROM emp
		WHERE sal>=2000) e, dept d -- 별칭을 꼭 가집니다 
WHERE e.deptno=d.deptno;

-- emp 테이블에서 커미션이 있는 사람들의 이름과 부서번호, 부서이름, 지역을 조회해 보세요.
SELECT e.ename, e.deptno, d.dname, d.loc
FROM (SELECT *
		FROM emp
		WHERE comm>0) e, dept d
WHERE e.deptno=d.deptno;

SELECT *
		FROM emp
		WHERE comm>0;


-- join 절에서의 서브쿼리

-- 모든 부서의 부서이름과, 지역, 부서내의 평균 급여를 조회해 보세요.
SELECT d.deptno, d.dname, d.loc, e.average_sal
FROM (SELECT e.deptno, AVG(sal) AS average_sal
	FROM emp e, dept d
	GROUP BY e.deptno) e, dept d
WHERE e.deptno=d.deptno;

SELECT e.deptno, AVG(e.sal)
	FROM emp e
	GROUP BY e.deptno; 
    
SELECT d.dname, d.loc, e.sal_avg -- 컬럼명으로 호출해서 외부에서도 값을 사용할 수 있습니다 
FROM (SELECT e.deptno, AVG(e.sal) AS sal_avg -- 컬럼명으로 빼주면 
	FROM emp e
	GROUP BY e.deptno) e, dept d
WHERE d.deptno=e.deptno;

SELECT AVG(e.sal)
	FROM emp e
	GROUP BY e.deptno