# 구현
def eat(food):
    answer = ''
    if food == '양고기':
        answer = '죠아!!!'
    elif food == '초밥':
        answer = '죠아!!!'
    elif food == '???':
        answer = '!!!'
    else:
        answer = '만보걷기'
    return answer


if __name__ == '__main__':
    print(eat('양고기'))