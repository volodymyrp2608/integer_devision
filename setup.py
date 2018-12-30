import IntegerDivision

if __name__ == '__main__':
    try:
        divided = int(input('write down divided: '))
        divizor = int(input('write down divizor: '))
        if divizor == 0:
            print('Divisor is zero !!! Dividing by a zero is unpossible!!!')
        else:
            obj = IntegerDivision.Division(str(divided), str(divizor))
            IntegerDivision.Division.division_in_column(obj)
    except ValueError:
        print('Divided or divizor is not a number or a non-integer number !!!')