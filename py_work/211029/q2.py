def main():
    num = int(input("숫자 입력하세요"))
    if num<0:
        print("입력한 값은 0보다 작습니다.")
    elif num >= 0 and num < 10:
        print("입력한 값은 0이상 10미만입니다.")
    elif num>=10 and num<20:
        print("입력한 값은 10이상 20미만입니다.")
    elif num >= 20:
        print("입력한 값은 20이상입니다.")

main()
