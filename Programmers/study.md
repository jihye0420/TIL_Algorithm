# 파이썬 형변환
# 리스트 함수
* 리스트 합집합, 교집합, 차집합, 대칭차집합
  ```python
  # 합집합
  lst1 = ['A', 'B', 'C', 'D']
  lst2 = ['C', 'D', 'E', 'F']
  union = list(set(lst1) | set(lst2))
  print(union) # ['C', 'F', 'A', 'E', 'B', 'D']
  union = list(set().union(lst1,lst2))
  print(union) # ['C', 'F', 'A', 'E', 'B', 'D']
  
  # 교집합
  intersection = list(set(lst1) & set(lst2))
  print(intersection) # ['C', 'D']
  intersection = list(set(lst1).intersection(lst2))
  print(intersection) # ['C', 'D']
  
  # 차집합
  complement = list(set(lst1) - set(lst2))
  print(complement) # ['B', 'A']
  complement = list(set(lst1).difference(lst2))
  print(complement) # ['A', 'B']
  
  # 대칭차집합
  sym_diff = list(set(lst1) ^ set(lst2))
  print(sym_diff) # ['F', 'E', 'A', 'B']
  sym_diff = list(set(lst1).symmetric_difference(lst2))
  print(sym_diff) # ['F', 'E', 'A', 'B']
  ```
# 딕셔너리 함수
# 문자열 함수
# datetime 함수
# 내장함수
* str.capitalize() : 첫 번째 글자만 대문자로 바꿔줌
- zip(iterable) : 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
    
    ```python
    >>> numbers = [1, 2, 3]
    >>> letters = ["A", "B", "C"]
    >>> for pair in zip(numbers, letters):
    ...     print(pair)
    ...
    (1, 'A')
    (2, 'B')
    (3, 'C')
    ```
* sorted() : 
* Counter() :
* bin(int): 정수를 이진수로 변환, 0b로 시작!
* 아스키: 알파벳을 비롯한 문자들을 통신하기 위해 일대일 대응시켜 숫자로 정해둔 코드 => 아스키 코드 <-> 문자
  * ord(문자): 아스키 코드로 변환
  * chr(아스키 코드): 문자로 변환
* abs(): 절대값 함수
* min(): 
* max():
- **combinations(iterable, r: int) → tuple : r개를 조합 (순서 고려하지 않고 뽑는 경우의 수)**
    
    ```python
    from itertools import combinations
    
    sets = ['A', 'B', 'C']
    
    data = combinations(sets, 2)
    
    for i in data:
       print(i)
    
    #print
    (A, B)
    (A, C)
    (B, C)
    ```
    
- **permutations(iterable, r: int) → tuple : r개를 순열 (순서 고려하여 뽑는 경우의 수)**
    
    ```python
    from itertools import permutations
    
    sets = [1,2,3]
    
    data = permutations(sets, 2)
    
    for i in data:
       print(i)
    
    #print
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)
    ```
    
- **map(function, iterable) :** map(적용시킬 함수, 적용할 값들) ⇒ list for문을 사용할 때 편리
    
    ```python
    >>> a = input().split()
    10 20 (입력)
    >>> a
    ['10', '20']
    
    >>> a = map(int, input().split())
    10 20 (입력)
    >>> a
    <map object at 0x03DFB0D0>
    >>> list(a)
    [10, 20]
    
    # ================================================================================
    
    # map 과 lambda
    
    # 일반 함수 이용
    def func_mul(x):
        return x * 2
    
    result1 = list(map(func_mul, [5, 4, 3, 2, 1]))
    print(f"map(일반함수, 리스트) : {result1}")
    
    # 람다 함수 이용
    result2 = list(map(lambda x: x * 2, [5, 4, 3, 2, 1]))
    print(f"map(람다함수, 리스트) : {result2}")
    ```

# python Type hinting

- 타입에 대한 주석을 이용하는 방식 → 타입 어노테이션(annotation) 새로운 방법으로 파이썬 코드의 타입 표시를 표준화
- 변수나 함수에 추가한 타입 어노테이션이 부정확한다고 해서 경고나 오류가 발생하는 것은 아님
    
    ```python
    # 타입에 대한 주석을 이용하는 방식
    num = 1  # type: int
    
    def repeat(message, times = 2):
        # type: (str, int) -> list
        return [message] * times
    
    # 타입 어노테이션(annotation)
    num: int = 1
    
    def repeat(message: str, times: int = 2) -> list:
        return [message] * times
    ```
    
    ```python
    from typing import List, Set, Dict, Tuple
    
    nums: List[int] = [1]
    
    unique_nums: Set[int] = {6, 7}
    
    vision: Dict[str, float] = {'left': 1.0, 'right': 0.9}
    
    john: Tuple[int, str, List[float]] = (25, "John Doe", [1.0, 0.9])
    
    # 함수
    def 함수명(<필수 인자>: <인자 타입>, <선택 인자>: <인자 타입> = <기본값>) -> <반환 타입>:
        ...
    
    def stringify(num: int) -> str:
        return str(num)
    
    def plus(num1: int, num2: float = 3.5) -> float:
        return num1 + num2
    
    def greet(name: str) -> None:
        return "Hi! " + str
    
    def repeat(message: str, times: int = 2) -> list:
        return [message] * times
    ```
    

## Typing 모듈

- typing 모듈을 사용해서 파이썬 코드에 타입 어노테이션을 추가
    - **List, Dict, Tuple, Set**
    
    ```python
    from typing import List, Dict, Tuple, Set
    
    nums: List[int] = [1, 2, 3]
    countries: Dict[str, str] = {"KR": "South Korea", "US": "United States", "CN": "China"}
    user: Tuple[int, str, bool] = (3, "Dale", True)
    chars: Set[str] = {"A", "B", "C"}
    ```
    
    - **Final** : 재할당이 불가능한 변수, 즉 상수에 대한 타입 어노테이션
    
    ```python
    from typing import Final
    
    TIME_OUT: Final[int] = 10
    ```
    
    - **Union** : 여러 개의 타입이 허용될 수 있는 상황
    
    ```python
    from typing import Union
    
    def toString(num: Union[int, float]) -> str:
        return str(num)
    ```
    
    - **Optional :** typing 모듈의 `Optional`은 `None`이 허용되는 함수의 매개 변수에 대한 타입을 명시할 때 유용
        - `Optional[int]` == `Union[int, None]`
    
    ```python
    from typing import Optional
    
    def repeat(message: str, times: Optional[int] = None) -> list:
        if times:
            return [message] * times
        else:
            return [message]
    ```
    
    - **Callable :** 함수를 일반 값처럼 변수에 저장하거나 함수의 인자로 넘기거나 함수의 반환값으로 사용, typing 모듈의 `Callable`은 이러한 함수에 대한 타입 어노테이션을 추가
    
    ```python
    # repeat 함수는 첫 번째 매개 변수 greet를 통해 함수를 인자로 받고 있음
    # 매개 변수에 타입 어노테이션 Callable[[str], str]를 추가해줌으로써, str 타입의 인자를 하나 받고, 결과값을 str로 반환하는 함수
    from typing import Callable
    
    def repeat(greet: Callable[[str], str], name: str, times: int = 2) -> None:
        for _ in range(times):
            print(greet(name))
    
    # 람다 함수를 작성할 때에도 동일한 타입 어노테이션을 사용할 수 있음 
    >>> greet: Callable[[str], str] = lambda name: f"Hi, {name}!"
    >>> repeat(greet, "Dale")
    Hi, Dale!
    Hi, Dale!
    ```
    
    - **타입 추상화** : 함수의 매개 변수에 대한 타입 어노테이션을 추가해줄 때는 타입을 추상적으로 명시해주는 것이 유리한 경우가 많음
        - typing 모듈은 `Iterable`뿐만 아니라 `Sequence`, `Mapping`, `MutableMapping`와 같은 여러가지 추상 타입을 지원
        - `toStrings()`함수는 `nums` 매개 변수의 타입을 `List[int]`대신에 `Iterable[int]`로 명시 ⇒ 따라서 이 함수는 리스트 뿐만 아니라 튜플, 세트까지 처리
        
        ```python
        from typing import Iterable, List
        
        def toStrings(nums: Iterable[int]) -> List[str]:
            return [str(x) for x in nums]
        ```
        

# 람다 함수
![image](https://user-images.githubusercontent.com/50284754/219025508-5c063286-ab97-4745-9458-780b8b30f28c.png)