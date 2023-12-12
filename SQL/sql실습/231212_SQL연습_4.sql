use fisa;

-- 1. dept table의 구조 검색
select * from dept; # 부서 정보
DESC dept;

-- dept, emp, salgrade table의 모든 데이터 검색
select * from dept; # 부서 정보
SELECT * from emp; # 직원 정보
select * from salgrade; # 등급별 min, max값을 저장해둔 테이블


-- *** 1. 동등 조인 ***
-- = 동등 비교연산자 사용해서 검색
SELECT ename, job, loc --  ename, job, deptno는 emp 테이블,  deptno, loc는 dept 테이블에 있습니다
FROM emp, dept
WHERE emp.deptno = dept.deptno;

SELECT ename, job, d.deptno, loc --  ename, job, deptno는 emp 테이블,  deptno, loc는 dept 테이블에 있습니다
FROM emp AS e , dept AS d
WHERE e.deptno = d.deptno;

SELECT e.ename, e.job, d.deptno, d.loc --  ename, job, deptno는 emp 테이블,  deptno, loc는 dept 테이블에 있습니다
FROM emp e, dept d
WHERE e.deptno = d.deptno;

-- 2. SMITH 의 이름(ename), 사번(empno), 근무지역(부서위치)(loc) 정보를 검색
-- emp/dept
-- 비교 기준 데이터를 검색조건에 적용해서 검색
-- table명이 너무 복잡한 경우 별칭 권장
select e.ename, e.empno, d.loc
from emp e, dept d
where e.ename = 'SMITH' and e.deptno = d.deptno;

-- 3. deptno가 동일한 모든 데이터(*) 검색
select *
from emp e, dept d
where e.deptno = d.deptno;

-- 4. 2+3 번 항목 결합해서 SMITH에 대한
--  모든 정보(ename, empno, sal, comm, deptno, loc) 검색하기
select e.ename, e.empno, e.sal, e.comm, d.deptno, d.loc
from emp e, dept d
where e.ename = 'SMITH'  and e.deptno = d.deptno;

-- 5.  SMITH에 대한 이름(ename)과 부서번호(deptno), 
-- 부서명(dept의 dname) 검색하기
select e.ename, d.deptno, d.dname
from emp e, dept d
where e.ename='SMITH' and e.deptno = d.deptno;

-- 6. 조인을 사용해서 뉴욕('NEW YORK')에 근무하는 사원의 이름(ename)과 급여(sal)를 검색 
select e.ename, e.sal, d.loc
from emp e, dept d
where d.deptno = e.deptno and d.loc='NEW YORK';

-- 7. 조인 사용해서 ACCOUNTING 부서(dname)에 소속된 사원의
-- 이름과 입사일 검색
select e.ename, e.hiredate
from emp e, dept d
where d.deptno = e.deptno and d.dname='ACCOUNTING'
order by 1 DESC;

-- 8. 직급(job)이 MANAGER인 사원의 이름(ename), 부서명(dname) 검색
select e.ename, d.dname
from emp e, dept d
where d.deptno = e.deptno and e.job='MANAGER';


-- 동등조인 review
-- 9. 사원(emp) 테이블의 부서 번호(deptno)로 
-- 부서 테이블(dept)을 참조하여 사원명(ename), 부서번호(deptno),
-- 부서의 이름(dname) 검색
select e.ename, e.deptno, d.dname
from emp e, dept d
where d.deptno = e.deptno;

-- *** 2. not-equi 조인 ***

-- salgrade table(급여 등급 관련 table)
select e.ename, e.sal, s.grade
from emp e, salgrade s
where e.sal BETWEEN s.losal AND s.HISAL;

-- 10. 사원의 급여가 몇 등급인지 검색
-- between ~ and : 포함 
select e.ename, e.sal, s.grade
from emp e, salgrade s
where e.sal BETWEEN s.losal AND s.HISAL;

-- SMITH 씨의 GRADE를 출력해주시고
select e.ename, s.grade, e.sal
from emp e, salgrade s
where e.ename='SMITH' and e.sal BETWEEN s.losal AND s.hisal;

-- 부서번호 30인 사람들의 각 이름, GRADE와 SAL, 상한선, 하한선 출력해주세요
select e.ename, s.grade, e.sal, s.losal, s.hisal, e.deptno
from emp e, salgrade s
where e.deptno=30 and e.sal BETWEEN s.losal AND s.hisal;


-- *** 3. self 조인 ***
-- 11. SMITH 직원의 매니저 이름 검색
-- emp e : 사원 table로 간주 / emp m : 상사 table로 간주
select m.empno, m.ename
from emp e, emp m
where e.mgr = m.empno and e.ename='SMITH';
-- 12. 매니저 이름이 KING(m ename='KING')인 
-- 사원들의 이름(e ename)과 직무(e job) 검색
select m.ename, e.job, m.ename
from emp e, emp m
where e.mgr = m.empno and m.ename='KING';

-- 13. SMITH와 동일한 부서에서 근무하는 사원의 이름 검색
-- 단, SMITH 이름은 제외하면서 검색 # todo: 확인
select e.ename, e.deptno
from emp e, emp m
where e.deptno = m.deptno and e.ename!='SMITH' and m.ename='SMITH';


-- *** 4. outer join ***
/* 두 개 이상의 테이블을 조인할 때 
emp m의 deptno는 참조되는 컬럼(PK)
emp d의 deptno는 참조하는 컬럼(외래키, FK)의 역할을 하게 됩니다

SELECT 컬럼명
FROM A테이블 LEFT JOIN B테이블
WHERE A테이블.컬럼 = B테이블.컬럼 
-- A테이블에는 있고, B테이블에는 없는 값들이 NULL로 출력이 된다 
*/ 



-- 14-1. 모든 사원명, 매니저 명 검색,  -- INNER JOIN은 두 테이블 컬럼에 모두 있어야만 출력. NULL인 값은 조회하지 않습니다 
select e.ename, e.job, m.ename
from emp e
inner join emp m
on e.mgr = m.empno;

select e.ename, e.job
from emp e, emp m
where e.mgr=m.empno;

-- select e.ename
-- from emp e
-- outer join emp m
-- on e.mgr = m.empno;


-- 14-2. 모든 사원명(KING포함), 매니저 명 검색, 
-- 단 매니저가 없는 사원(KING)도 검색되어야 함
-- LEFT JOIN 사용
SELECT *  
FROM emp e LEFT OUTER JOIN emp m
on e.mgr = m.empno;
-- RIGHT JOIN 사용
SELECT *  
FROM emp m RIGHT OUTER JOIN emp e
on e.mgr = m.empno;


-- 15. 모든 직원명(ename), 부서번호(deptno), 부서명(dname) 검색
-- 부서 테이블의 40번 부서와 조인할 사원 테이블의 부서 번호가 없지만,
-- outer join이용해서 40번 부서의 부서 이름도 검색하기 
SELECT e.ename, d.deptno, d.dname  
FROM emp e RIGHT JOIN dept d
ON e.deptno=d.deptno;

-- 16. 모든 부서번호가 검색(40)이 되어야 하며 급여가 3000이상(sal >= 3000)인 사원의 정보 검색
-- 특정 부서에 소속된 직원이 없을 경우 사원 정보는 검색되지 않아도 됨
-- 검색 컬럼 : deptno, dname, loc, empno, ename, job, mgr, hiredate, sal, comm
SELECT d.deptno, d.dname, d.loc, e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm 
FROM emp e RIGHT JOIN dept d
ON e.deptno=d.deptno and e.sal>=3000;

/*

검색 결과 예시

+--------+------------+----------+-------+-------+-----------+------+------------+---------+------+
| deptno | dname      | loc      | empno | ename | job       | mgr  | hiredate   | sal     | comm |
+--------+------------+----------+-------+-------+-----------+------+------------+---------+------+
|     10 | ACCOUNTING | NEW YORK |  7839 | KING  | PRESIDENT | NULL | 1981-11-17 | 5000.00 | NULL |
|     20 | RESEARCH   | DALLAS   |  7788 | SCOTT | ANALYST   | 7566 | 1987-04-19 | 3000.00 | NULL |
|     20 | RESEARCH   | DALLAS   |  7902 | FORD  | ANALYST   | 7566 | 1981-12-03 | 3000.00 | NULL |
|     30 | SALES      | CHICAGO  |  NULL | NULL  | NULL      | NULL | NULL       |    NULL | NULL |
|     40 | OPERATIONS | BOSTON   |  NULL | NULL  | NULL      | NULL | NULL       |    NULL | NULL |
+--------+------------+----------+-------+-------+-----------+------+------------+---------+------+
*/

-- 세일즈 부서는 sal + comm 이 실제 월급입니다
-- sal + comm 이 2000불 이상인 모든 직원을 검색해 출력해 주세요
SELECT e.ename, e.job
FROM emp e join dept d
ON e.deptno=d.deptno
WHERE (e.sal+e.comm)>=2000 and d.deptno=30;

SELECT d.deptno, d.dname, d.loc, e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm 
FROM emp e right JOIN dept d
ON e.deptno=d.deptno and (e.sal+if(e.comm is null, 0, e.comm))>=2000;
