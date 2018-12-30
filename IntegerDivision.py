import Column
class Division():
    """Class determines that components of column"""
    def __init__(self, divided, divizor):
        self.divided = divided
        self.divizor = divizor
        self.first_numbers_divided = ''
        self.product = ''
        self.difference = ''
        self.list_of_products = []
        self.list_of_differences = []
        self.list_of_part = []
        self.number_of_signs_is_after_comma = 0
        self.add_zero_part = 0

    def division_in_column(self):
        self.first_zero_of_product(self.divided, self.divizor)
        self.list_result = self.integer_devision(self.divided, self.divizor)
        obj_1 = Column.Column(self.divided, self.divizor, self.list_of_part, self.list_of_products, self.list_of_differences)
        self.string_result = Column.Column.column(obj_1)
        return self.string_result

    def integer_devision(self, divided, divizor):
        try:
            i = 0
            p = 2
            k = 0
            bool = True
            part = ''

            if int(divided) == 0:
                return self.first_zero(divided)

            #check or the first number the divided more divizor
            if int(divided[i]) >= int(divizor):
                # find part
                part += str(int(divided[i]) // int(divizor[i]))
                self.list_of_part.append(part)

                # find product
                self.product = str(int(part) * int(divizor))
                self.list_of_products.append(self.product)

                # find difference
                self.difference = str(int(divided[i]) - int(self.product))
                k += 1
            #if the first number divided no more divizor then take yet second
            else:
                while bool:
                    k = 0
                    if p <= len(divided):
                        self.first_numbers_divided = divided[:p]
                        if int(self.first_numbers_divided) >= int(divizor):

                            # find part
                            part += str(int(self.first_numbers_divided) // int(divizor))
                            self.list_of_part.append(part)

                            # find product
                            product = str(int(part) * int(divizor))
                            self.list_of_products.append(product)

                            # find difference
                            self.difference = str(int(self.first_numbers_divided) - int(product))
                            k += p
                            bool = False
                        else:
                            p += 1

                    else:
                        self.list_of_part.append('0')
                        self.difference = divided[:p]
                        k += p
                        break

            #if a difference is less divizor
            if int(self.difference) < int(divizor):
                #if divided after the first action 12/12
                if k == len(divided) and int(self.difference) == 0:
                    self.list_of_differences.append(self.difference)
                elif k < len(divided):
                    new_difference = self.difference

                    # if copy off two numbers then add a zero to part
                    count_zero = 0
                    #print(k)
                    for l in range(k, len(divided)):
                        new_difference += divided[l]
                        if int(new_difference) >= int(divizor):
                            if count_zero >= 1:
                                self.zero(count_zero)
                            break
                        else:
                            if int(new_difference) == 0:
                                continue
                            else:
                                count_zero += 1

                    # form new divided for a call
                    if int(self.difference) == 0:
                        count_zero_in_divided = 0
                        # check or a number has zeros
                        for h in range(k, len(divided)):
                            if int(divided[h]) == 0:
                                count_zero_in_divided += 1
                            else:
                                break

                        if count_zero_in_divided >= 1:
                            self.zero(count_zero_in_divided)
                            if count_zero_in_divided == len(divided[k:len(divided)]):
                                self.list_of_differences.append('0')

                        self.difference = divided[k:]
                    else:
                        self.difference += divided[k:]

                    # add to the list of differences
                    for j in range(len(self.difference)):
                        if int(self.difference[:j + 1]) < int(divizor):
                            continue
                        else:
                            self.list_of_differences.append(str(int(self.difference[:j + 1])))
                            break
                #a number of ділеться is with a remain
                else:
                    if ',' not in self.list_of_part:
                        self.list_of_part.append(',')

                    self.difference += '0'
                    if int(self.difference) >= int(divizor):
                        self.list_of_differences.append(self.difference)

                    self.number_of_signs_is_after_comma = self.number_after_comma()
                    #period of column
                    if self.number_of_signs_is_after_comma == 10:
                        return self.list_of_part, self.list_of_products, self.list_of_differences
            else:
                self.list_of_differences.append(self.difference)

            if int(self.difference) > 0:
                return self.integer_devision(self.difference, self.divizor)
            else:
                return self.list_of_part, self.list_of_products, self.list_of_differences
        except:
            print('Сталася помилка!!!')

    #if the divided equals a zero
    def first_zero(self, divided):
        if int(divided) == 0:
            self.list_of_part.append('0')
            self.list_of_products.append('0')
            self.list_of_differences.append('0')
            return self.list_of_part, self.list_of_products, self.list_of_differences

    #if divided less divizor
    def first_zero_of_product(self, divided, divizor):
        if int(divided) < int(divizor):
            self.list_of_products.append('0')
        return self.list_of_products

    #addition of zeros is in part
    def zero(self, count_zero):
        self.list_of_part.append('0' * count_zero)
        return 1

    #an amount of signs is after a comma (period)
    def number_after_comma(self):
        self.number_of_signs_is_after_comma += 1
        return self.number_of_signs_is_after_comma