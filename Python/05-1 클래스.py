"""
* 클래스
: 객체변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지
"""


class FourCal:
    # 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


"""
* 클래스 상속
: 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
"""


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

    # 메소드 오버라이딩 : 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second


"""
* 클래스 변수
: 클래스변수는 객체변수와 달리 클래스로 만든 모든 객체에 공유된다는 특징
"""


class Family:
    lastname = "김"


"""
>>> a = Family()
>>> b = Family()
>>> a.lastname
김
>>> b.lastname
김

>>> Family.lastname = "박"
>>> a.lastname
박
>>> b.lastname
박

>>> a.lastname = "최"
>>> a.lastname
최

>>> Family.lastname
박
>>> b.lastname
박

"""
