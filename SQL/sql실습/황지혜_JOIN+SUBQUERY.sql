## SQL 실행순서
-- FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

use fisa;
-- 모든 부서의 정보와 함께 커미션이 있는 직원들의 커미션과 이름을 조회해 보세요.
select d.deptno, d.dname, d.loc, e.ename, e.comm
from emp e, dept d
where e.comm is not null and e.comm != 0 and e.deptno=d.deptno;

-- 모든 부서의 부서별 연봉에 대한 총합과 평균과 표준편차를 구하고
-- 모든 부서의 사원수를 구해 보세요.
select d.deptno, d.dname, d.loc, 
		sum(e.sal) as 총합, avg(e.sal) as 평균, STDDEV(e.sal) as 표준편차, count(e.ename) as 사원수
from emp e, dept d
where e.deptno=d.deptno
group by d.deptno
order by 1;
# 만약 sales 팀이라면, sal+comm 포함! => # todo: 해보기

-- 각 관리자의 부하직원수와 부하직원들의 평균연봉을 구해 보세요.
select m.mgr, m.ename as 매니저, count(e.ename) '부하직원수', avg(e.sal) '평균연봉'
from emp e, emp m
where e.empno = m.mgr and m.mgr is not null
group by m.mgr;

# Sub-Query 
-- 쿼리 안쪽에 쿼리를 넣을수 있다.
-- where 절에서의 서브쿼리
-- scott과 같은 부서에 있는 직원 이름을 검색해 보세요.
select ename
from emp
where deptno = (select deptno from emp where ename='scott');

-- 직무(job)가 Manager인 사람들이 속한 부서의 부서번호와 부서명 , 지역을 조회해 보세요.
	-- manager 사람들이 다수이기 때문에 where절에 in 을 활용!
select deptno, dname, loc
from dept 
where deptno in (select deptno from emp where job='MANAGER');

# from 절에서의 서브쿼리
-- emp 테이블에서 급여가 2000이 넘는 사람들의 이름과 부서번호, 부서이름, 지역 조회해 보세요.
select ee.ename, d.deptno, d.dname, d.loc
from dept d, (select ename, deptno from emp where sal >= 2000) ee -- 별칭 필요!!!
WHERE d.deptno = ee.deptno;

-- emp 테이블에서 커미션이 있는 사람들의 이름과 부서번호, 부서이름, 지역을 조회해 보세요.
select ee.ename, d.deptno, d.dname, d.loc
from dept d, (select e.deptno, e.ename from emp e where e.comm is not null and e.comm != 0) ee
where d.deptno = ee.deptno;

-- join 절에서의 서브쿼리
-- 모든 부서의 부서이름과, 지역, 부서내의 평균 급여를 조회해 보세요. => 다시 시도중...
select d.dname, d.loc, avg(e.sal) '평균 급여'
from dept d, emp e
where e.deptno=d.deptno
group by d.deptno;

