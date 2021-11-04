# 1. 문자열 "The Espresso Spirit"을 다음과 같이 선언하자.
#     str = "The Espresso Spirit"
#
#    그리고 한번은 모두 대문자로 바꿔서 출력하고, 또 한번은 모두 소문자로 바꿔서 출력해보자.
#    그리고 마지막에 원본 그대로 출력을 한번 더 하자.

str = "The Espresso Spirit"
print(str.upper())
print(str.lower())
print(str)

def birth_only(birth):
    return birth[:6]

a= birth_only("070609-2011xxx")
print(a)

a=birth_only("090716-1012xxx")
print(a)

# alt enter :단축키