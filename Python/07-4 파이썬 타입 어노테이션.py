"""
동적 언어와 정적 언어
동적 언어 : 프로그램 실행 중 변수의 타입을 동적으로 바꿀 수 있는 언어
정적 언어 : 한 번 변수의 타입을 지정하면 지정한 타입 외에 다른 타입은 사용할 수 없는 언어
"""

"""
파이썬 타입 어노테이션 (python type annotation) == 타입 힌트(팅) (type hint(ing)) 
: 동적 언어의 단점을 극복하기 위해 3.5 버전부터 타입 어노테이션 기능을 지원
: 타입에 대한 힌트를 알려 주는 정도의 기능만 지원
* 정수는 int, 문자열은 str, 리스트는 list, 튜플은 tuple, 딕셔너리는 dict, 집합은 set, 불은 bool
"""
num: int = 1


def add(a: int, b: int) -> int:
    return a + b


result = add(3, 3.4)
print(result)  # 6.4 출력

"""
typing 모듈
: 내장 타입을 이용한 복잡한 타입 어노테이션을 추가할 때 typing 모듈 추가
* List, Dict, Tuple, Set, Final, Union, Optional
* Final : 재할당이 불가능한 변수, 상수에 대한 타입 어노테이션 추가
* Union : 여러 개의 타입이 허용될 수 있는 상황
* Optional : None이 허용되는 함수의 매개변수에 대한 타입을 명시할 때 유용
* Optional[int] == Union[int, None]
"""
from typing import List, Set, Dict, Tuple, Final, Union, Optional

nums: List[int] = [1]

unique_nums: Set[int] = {6, 7}

vision: Dict[str, float] = {'left': 1.0, 'right': 0.9}

john: Tuple[int, str, List[float]] = (25, "John Doe", [1.0, 0.9])

TIME_OUT: Final[int] = 10


def toString(num: Union[int, float]) -> str:
    return str(num)


def repeat(message: str, times: Optional[int] = None) -> list:
    if times:
        return [message] * times
    else:
        return [message]


"""
* Callable : 함수에 대한 타입 어노테이션
ex) Callable[[str], str] : str 타입의 인자를 하나 받고, 결과값을 str로 반환하는 함수
"""

from typing import Callable


def repeat(greet: Callable[[str], str], name: str, times: int = 2) -> None:
    for _ in range(times):
        print(greet(name))


greet: Callable[[str], str] = lambda name: f"Hi, {name}!"

repeat(greet, "Dale")

"""
타입 추상화
: 함수의 매개 변수에 대한 타입 어노테이션을 추가해줄 때는 타입을 추상적으로 명시해주는 것이 유리
ex) List[int] 대신에 Iterable[int]로 명시
* Iterable 뿐만 아니라 Sequence, Mapping, MutableMapping와 같은 여러 가지 추상 타입을 지원
"""
from typing import Iterable, List


def toStrings(nums: Iterable[int]) -> List[str]:
    return [str(x) for x in nums]  # 이 함수는 리스트 뿐만 아니라 튜플, 세트까지 처리할 수 있는 유연한 API
