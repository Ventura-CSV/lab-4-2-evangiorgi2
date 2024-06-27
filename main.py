def main():
 
    total = 0
    for i in range(5):
        number = int(input('Enter a number: '))
        total += number
    print('Total {0}'.format(total))
    
    return total


if __name__ == '__main__':
    main()
