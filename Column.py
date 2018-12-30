class Column():
    """Class of leadingout of column is in a cantilever"""
    def __init__(self, divided, divizor, list_of_part, list_of_products, list_of_differences):
        self.divided = divided
        self.divizor = divizor
        self.list_of_part = list_of_part
        self.list_of_products = list_of_products
        self.list_of_differences = list_of_differences
        self.result_string = ''

    def column(self):
        self.result_string = self.division_column(self.divided, self.divizor, self.list_of_part, self.list_of_products, self.list_of_differences)
        return self.result_string

    def division_column(self, divided, divizor, list_of_part, list_of_products, list_of_differences):
        bool = True
        p = 0
        position_of_element_ls_df = 0
        position_of_element_ls_prd = 1
        count_gap = 0
        dif_is_without_writing = 0
        divizor_with_lower_dash = '_' + divizor + '_'
        part = self.association_of_part()

        list_of_differences.insert(0, divided)

        if int(divided) == 0:
            print(' ' + divided + ' ' + '|' + divizor_with_lower_dash)
            self.result_string += ' ' + divided + ' ' + '|' + divizor_with_lower_dash
            print('_' + list_of_products[p] + '_' '|' + part)
            self.result_string += '_' + list_of_products[p] + '_' '|' + part
            print(' ' + list_of_differences[p+1] + ' ')
            self.result_string += ' ' + list_of_differences[p+1] + ' '
            return self.result_string

        #add a lower dash to the differences
        differences = self.addition_of_lower_dash()

        #addition_of_lower_dashes
        product = self.addition_of_lower_dashes()

        while bool:
            #write down the first two terms of column
            if p == 0:
                if len(differences[p]) < len(product[p]):
                    print(differences[p] + ' ' * int(len(product[p]) - len(differences[p])) + '|' + divizor_with_lower_dash)
                    self.result_string += differences[p] + ' ' * int(len(product[p]) - len(differences[p])) + '|' + divizor_with_lower_dash
                    print(product[p] + '|' + part)
                    self.result_string += product[p] + '|' + part
                    if int(list_of_differences[p]) > int(list_of_products[p]):
                        dif_is_without_writing = str(int(list_of_differences[p]) - int(list_of_products[p]))
                        dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                        count_gap = dif_is_without_writing_len
                    else:
                        count_gap = len(product[p]) - len(differences[p])

                    position_of_element_ls_df = len(list_of_products[p]) + count_gap

                else:
                    print(differences[p] + '|' + divizor_with_lower_dash)
                    self.result_string += differences[p] + '|' + divizor_with_lower_dash
                    print(product[p] + ' ' * int(len(differences[p]) - len(product[p])) + '|' + part)
                    self.result_string += product[p] + ' ' * int(len(differences[p]) - len(product[p])) + '|' + part
                    if int(list_of_differences[p]) > int(list_of_products[p]):
                        first_difference = list_of_differences[p]
                        first_difference_part = first_difference[:len(list_of_products[p])]

                        if int(first_difference_part) < int(list_of_products[p]):
                            first_difference_part = first_difference[:len(list_of_products[p]) + 1]
                        dif_is_without_writing = str(abs(int(first_difference_part) - int(list_of_products[p])))
                        next_element = len(list_of_products[p]) #f

                        if int(dif_is_without_writing) == 0:
                            boll = True
                            while boll:
                                if len(differences[p + 1]) - position_of_element_ls_prd >= 1:
                                    last = int(differences[p + 1][len(differences[p + 1]) - position_of_element_ls_prd])
                                    if int(last) == int(list_of_differences[p][next_element]) and int(last) != 0:
                                        string_first_index = list_of_differences[p]
                                        first_index = string_first_index.index(list_of_differences[p][next_element],len(list_of_products[p]))
                                        if next_element != len(list_of_products[p]):
                                            if int(position_of_element_ls_prd) != 1:
                                                count_gap = first_index - position_of_element_ls_prd + 1
                                                if int(list_of_differences[p][count_gap]) != int(differences[p+1][1]):
                                                    count_gap += 1
                                            else:
                                                count_gap = len(string_first_index[:first_index + 1]) - len(list_of_differences[p + 1])
                                        else:
                                            count_gap = first_index
                                        break
                                else:
                                    count_gap = len(list_of_products[p])
                                    break

                                if int(last) == int(list_of_differences[p][next_element]):
                                    if last == 0:
                                        position_of_element_ls_prd += 1
                                        if next_element < len(list_of_differences[p]):
                                            next_element += 1
                                            count_gap += 2
                                            continue
                                    else:
                                        count_gap += 1
                                        boll = False

                                else:
                                    if int(last) == 0:
                                        position_of_element_ls_prd += 1
                                        continue
                                    else:
                                        next_element += 1
                                        if next_element < len(list_of_differences[p]):
                                            continue
                                        else:
                                            dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                                            count_gap = dif_is_without_writing_len
                                            boll = False
                        else:

                            if int(first_difference_part) > int(list_of_products[p]):
                                if len(first_difference_part) > len(list_of_products[p]):
                                    dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing) + 1)
                                else:
                                    dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                                count_gap = dif_is_without_writing_len
                                position_of_element_ls_df = len(list_of_products[p])
                                p += 1
                                continue
                            else:
                                first_difference_part_len = len(list_of_products[p]) + 1
                                while first_difference_part_len < len(list_of_differences[p]):
                                    first_difference_part = first_difference[:first_difference_part_len]
                                    if int(first_difference_part) > int(list_of_products[p]):
                                        dif_is_without_writing_len = int(len(first_difference_part) - len(list_of_products[p]))
                                        break
                                    else:
                                        first_difference_part_len += 1

                                count_gap = dif_is_without_writing_len
                    else:
                        count_gap = len(product[p]) - len(differences[p])

                    position_of_element_ls_df = count_gap
                p += 1

            #write down other terms of column
            elif p < len(list_of_differences) - 1:
                if position_of_element_ls_df < len(list_of_differences[0]):
                    i = position_of_element_ls_df
                    # compares elements to the last number
                    while i < len(list_of_differences[0]):
                        last = differences[p][len(differences[p]) - 1]
                        if int(last) == int(list_of_differences[0][i]):
                            if int(list_of_differences[p - 1]) > int(list_of_products[p - 1]) and len(list_of_differences[p]) > len(list_of_products[p]):
                                print(' ' * int(count_gap) + differences[p])
                                self.result_string += ' ' * int(count_gap) + differences[p]
                                print(' ' * int(count_gap + 1) + product[p])
                                self.result_string += ' ' * int(count_gap + 1) + product[p]
                                count_gap += 1
                            else:
                                print(' ' * int(count_gap) + differences[p])
                                self.result_string += ' ' * int(count_gap) + differences[p]
                                print(' ' * int(count_gap) + product[p])
                                self.result_string += ' ' * int(count_gap) + product[p]

                            #determine broke through for the next pair of numbers
                            if int(list_of_differences[p]) > int(list_of_products[p]):
                                dif_is_without_writing = str(int(list_of_differences[p]) - int(list_of_products[p]))
                                dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                                count_gap += dif_is_without_writing_len
                                i += 1
                                next_element += 1
                            elif int(list_of_differences[p]) == int(list_of_products[p]):
                                dif_is_without_writing = str(int(list_of_differences[p]) - int(list_of_products[p]))
                                if int(dif_is_without_writing) == 0:
                                    next_element = i
                                    position_of_element_ls_prd = 1
                                    boll = True
                                    while boll:
                                        if len(differences[p + 1]) - position_of_element_ls_prd >= 1:
                                            last = int(differences[p + 1][len(differences[p + 1]) - position_of_element_ls_prd])
                                            if int(last) == int(list_of_differences[0][next_element + 1]) and int(last) != 0:
                                                string_first_index = list_of_differences[0]
                                                first_index = string_first_index.index(str(last), next_element + 1)
                                                if next_element != len(list_of_products[p]):
                                                    if int(position_of_element_ls_prd) != 1:
                                                        count_gap = first_index
                                                    else:
                                                        count_gap = len(string_first_index[:first_index + 1]) - len(list_of_differences[p + 1])
                                                else:
                                                    count_gap = first_index
                                                break
                                        else:
                                            count_gap += len(list_of_products[p])
                                            break

                                        #if the last zero then take nearby numbers
                                        if int(last) == int(list_of_differences[0][next_element + 1]):
                                            if last == 0:
                                                position_of_element_ls_prd += 1
                                                if next_element < len(list_of_differences[0]):
                                                    next_element += 1
                                                    count_gap += 2
                                                    continue
                                            else:
                                                count_gap += 1
                                                boll = False

                                        else:
                                            if int(last) == 0:
                                                position_of_element_ls_prd += 1
                                                continue
                                            else:
                                                next_element += 1
                                                if next_element < len(list_of_differences[0]):
                                                    count_gap += 1
                                                    continue
                                                else:
                                                    dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                                                    count_gap += dif_is_without_writing_len
                                                    boll = False
                                    #determine position of next element
                                    if i != next_element:
                                        i = next_element + 1
                                    else:
                                        i += 1
                                #an item of elements is on the list of differences
                                position_of_element_ls_df = i
                            else:
                                count_gap += len(product[p]) - len(differences[p])
                                i += 1

                            p += 1
                            break
                        else:

                            if int(list_of_differences[p - 1]) > int(list_of_products[p - 1]) and len(list_of_differences[p]) > len(list_of_products[p]):
                                print(' ' * int(count_gap) + differences[p])
                                self.result_string += ' ' * int(count_gap) + differences[p]
                                print(' ' * int(count_gap + 1) + product[p])
                                self.result_string += ' ' * int(count_gap + 1) + product[p]
                                count_gap += 1
                            else:
                                print(' ' * int(count_gap) + differences[p])
                                self.result_string += ' ' * int(count_gap) + differences[p]
                                print(' ' * int(count_gap) + product[p])
                                self.result_string += ' ' * int(count_gap) + product[p]

                            #determine broke through for the next pair of numbers
                            if int(list_of_differences[p]) > int(list_of_products[p]):
                                dif_is_without_writing = str(int(list_of_differences[p]) - int(list_of_products[p]))
                                dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                                count_gap += dif_is_without_writing_len
                                i += 1
                                next_element += 1
                            elif int(list_of_differences[p]) == int(list_of_products[p]):
                                dif_is_without_writing = str(int(list_of_differences[p]) - int(list_of_products[p]))
                                if int(dif_is_without_writing) == 0:
                                    position_of_element_ls_prd = 1
                                    boll = True
                                    while boll:
                                        if len(differences[p + 1]) - position_of_element_ls_prd >= 1:
                                            last = int(differences[p + 1][len(differences[p + 1]) - position_of_element_ls_prd])
                                            if int(last) == int(list_of_differences[0][next_element + 1]) and int(last) != 0:
                                                string_first_index = list_of_differences[0]
                                                first_index = string_first_index.index(str(last), next_element + 1)
                                                if next_element != len(list_of_products[p]):
                                                    if int(position_of_element_ls_prd) != 1:
                                                        count_gap = first_index
                                                    else:
                                                        count_gap = len(string_first_index[:first_index + 1]) - len(list_of_differences[p + 1])
                                                else:
                                                    count_gap = first_index
                                                break
                                        else:
                                            count_gap += len(list_of_products[p])
                                            break

                                        if int(last) == int(list_of_differences[0][next_element]):
                                            if last == 0:
                                                position_of_element_ls_prd += 1
                                                if next_element < len(list_of_differences[0]):
                                                    next_element += 1
                                                    count_gap += 2
                                                    continue
                                            else:
                                                count_gap += 1
                                                boll = False

                                        else:
                                            if int(last) == 0:
                                                position_of_element_ls_prd += 1
                                                continue
                                            else:
                                                next_element += 1
                                                if next_element < len(list_of_differences[0]):
                                                    continue
                                                else:
                                                    dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                                                    count_gap += dif_is_without_writing_len
                                                    boll = False
                                    if i != next_element:
                                        i = next_element + 1
                                    else:
                                        i += 1
                            else:
                                count_gap += len(product[p]) - len(differences[p])
                                i += 1

                            position_of_element_ls_df = i
                            p += 1
                            break

                #if an index exceeds lengths of the first element of differences
                else:
                    #if divided after the first action
                    if len(differences) == 2:
                        print(' ' * int(len(product[p - 1]) - 2) + differences[p])
                        self.result_string += ' ' * int(len(product[p - 1]) - 2) + differences[p]
                        bool = False
                    #if divided less divizor 1/12
                    else:
                        if int(list_of_differences[p - 1]) > int(list_of_products[p - 1]):
                            if len(list_of_differences[p]) > len(list_of_products[p]):
                                print(' ' * int(count_gap) + differences[p])
                                self.result_string += ' ' * int(count_gap) + differences[p]
                                print(' ' * int(count_gap + 1) + product[p])
                                self.result_string += ' ' * int(count_gap + 1) + product[p]
                                count_gap += 1
                            else:
                                print(' ' * int(count_gap) + differences[p])
                                self.result_string += ' ' * int(count_gap) + differences[p]
                                print(' ' * int(count_gap) + product[p])
                                self.result_string += ' ' * int(count_gap) + product[p]

                        else:
                            print(' ' * int(count_gap + 1) + differences[p])
                            self.result_string += ' ' * int(count_gap + 1) + differences[p]
                            print(' ' * int(count_gap + 1) + product[p])
                            self.result_string += ' ' * int(count_gap + 1) + product[p]

                    if int(list_of_differences[p]) > int(list_of_products[p]):
                        dif_is_without_writing = str(int(list_of_differences[p]) - int(list_of_products[p]))
                        dif_is_without_writing_len = int(len(list_of_products[p]) - len(dif_is_without_writing))
                        count_gap += dif_is_without_writing_len
                    else:
                        count_gap += len(product[p]) - len(differences[p])
                    p += 1

            else:
                #completion of the program
                if len(list_of_differences[0]) <= len(divizor):
                    if int(list_of_differences[p - 1]) == int(list_of_products[p - 1]):
                        count_gap = int(count_gap) + int(len(list_of_products[p - 1]) - 1)
                        print(' ' * int(count_gap) + differences[p])
                        self.result_string += ' ' * int(count_gap) + differences[p]
                    else:
                        print(' ' * int(count_gap) + differences[p])
                        self.result_string += ' ' * int(count_gap) + differences[p]

                    if int(list_of_differences[len(list_of_differences) - 1]) != 0:
                        print(' ' * int(count_gap) + '...')
                        self.result_string += ' ' * int(count_gap) + '...'
                    bool = False
                else:
                    if int(list_of_differences[len(list_of_differences) - 1]) != 0:
                        print(' ' * int(count_gap) + '...')
                        self.result_string += ' ' * int(count_gap) + '...'
                    else:
                        print(' ' * int(count_gap) + differences[p])
                        self.result_string += ' ' * int(count_gap) + differences[p]
                    bool = False
        return self.result_string

    #association of part
    def association_of_part(self):
        part = ''
        for i in range(len(self.list_of_part)):
            part += self.list_of_part[i]
        return part

    def addition_of_lower_dash(self):
        differences = []
        for j in range(len(self.list_of_differences)):
            if j < len(self.list_of_differences) - 1:
                differences.append('_' + str(self.list_of_differences[j]))
            else:
                if int(self.list_of_differences[j]) != 0:
                    differences.append('_' + str(self.list_of_differences[j]))
                else:
                    differences.append(self.list_of_differences[j])
        return differences

    def addition_of_lower_dashes(self):
        product = []
        for j in range(len(self.list_of_products)):
            product.append('_' + str(self.list_of_products[j]) + '_')
        return product