def main():
    print('hi\nwelcome to calculator')
    while True:
        print('1. sum')
        print('2. min')
        print('3. mul')
        print('4. dev')
        print('5. exit')
        
        choose = int(input('enter order: '))
        num1 = float(input('enter num : '))
        num2 = float(input('enter num : '))
        match choose:
            case 1:
                print(f'{num1}+{num2} = {num1+num2}')
            case 2:
                print(f'{num1}-{num2} = {num1-num2}')

            case 3 :
                print(f'{num1}x{num2} = {num1*num2}')

            case 4 :
                if num2 != 0 :
                    print(f'{num1}/{num2} = {num1/num2}')
                else:
                    print('cant calculate it becuse num2 is 0')

            case 5 :
                break

if __name__ == "__main__":
    main()