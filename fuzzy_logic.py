import numpy


decision_matrix = []
weight = []

table1 = [
    [0, 0, 2],  # VLR
    [2, 3, 4],  # LR
    [4, 5, 6],  # R
    [6, 7, 8],  # HR
    [8, 9, 10]  # VHR
]

table3 = [
    [0, 0, 0.2],  # VL
    [0.2, 0.3, 0.4],  # L
    [0.4, 0.5, 0.6],  # M
    [0.6, 0.7, 0.8],  # H
    [0.8, 0.9, 1]  # VH
]


def sayHello():
    print("hello")


def linguistic_pos_table1(name):
    if name == "VHR":
        return 4
    elif name == "HR":
        return 3
    elif name == "R":
        return 2
    elif name == "LR":
        return 1
    else:
        return 0


def linguistic_pos_table3(name):
    if name == "VH":
        return 4
    elif name == "H":
        return 3
    elif name == "M":
        return 2
    elif name == "L":
        return 1
    else:
        return 0


def create_table4_C1(options, table4_full):
    table4 = []
    table4_format = []

    for i in range(len(options)):
        if i == 0:
            if options[i] == 1:
                table4.append(table4_full[0:3])
                continue
            else:
                table4.append(table4_full[3:6])
                continue
        elif i == 1:
            if options[i] == 1:
                table4.append(table4_full[6:9])
                continue
            elif options[i] == 2:
                table4.append(table4_full[9:12])
                continue
            else:
                table4.append(table4_full[12:15])
                continue
        elif i == 2:
            if options[i] == 1:
                table4.append(table4_full[15:18])
                continue
            elif options[i] == 2:
                table4.append(table4_full[18:21])
                continue
            else:
                table4.append(table4_full[21:24])
                continue
        elif i == 3:
            if options[i] == 1:
                table4.append(table4_full[24:27])
                continue
            elif options[i] == 2:
                table4.append(table4_full[27:30])
                continue
            else:
                table4.append(table4_full[30:33])
                continue
        elif i == 4:
            if options[i] == 1:
                table4.append(table4_full[33:36])
                continue
            else:
                table4.append(table4_full[36:39])
                continue
        elif i == 5:
            if options[i] == 1:
                table4.append(table4_full[39:42])
                continue
            else:
                table4.append(table4_full[42:45])
                continue
        elif i == 6:
            if options[i] == 1:
                table4.append(table4_full[45:48])
                continue
            elif options[i] == 2:
                table4.append(table4_full[48:51])
                continue
            else:
                table4.append(table4_full[51:54])
                continue
        elif i == 7:
            if options[i] == 1:
                table4.append(table4_full[54:57])
                continue
            elif options[i] == 2:
                table4.append(table4_full[57:60])
                continue
            elif options[i] == 3:
                table4.append(table4_full[60:63])
                continue
            else:
                table4.append(table4_full[63:66])
                continue
        elif i == 8:
            if options[i] == 1:
                table4.append(table4_full[66:69])
                continue
            elif options[i] == 2:
                table4.append(table4_full[69:72])
                continue
            elif options[i] == 3:
                table4.append(table4_full[72:75])
                continue
            else:
                table4.append(table4_full[75:78])
                continue
        elif i == 9:
            if options[i] == 1:
                table4.append(table4_full[78:81])
                continue
            else:
                table4.append(table4_full[81:84])
                continue
        else:
            if options[i] == 1:
                table4.append(table4_full[84:87])
                continue
            else:
                table4.append(table4_full[87:90])
                continue

    for i in range(len(table4)):
        for j in range(len(table4[i])):
            table4_format.append(table4[i][j])
    return table4_format


def create_table4_Crest(options, table4_full):
    table4 = []
    table4_format = []

    for i in range(len(options)):
        if i == 0:
            if options[i] == 5:
                table4.append(table4_full[0:3])
                continue
            elif options[i] == 4:
                table4.append(table4_full[3:6])
                continue
            elif options[i] == 3:
                table4.append(table4_full[6:9])
                continue
            elif options[i] == 2:
                table4.append(table4_full[9:12])
                continue
            else:
                table4.append(table4_full[12:15])
                continue
        elif i == 1:
            if options[i] == 5:
                table4.append(table4_full[15:18])
                continue
            elif options[i] == 4:
                table4.append(table4_full[18:21])
                continue
            elif options[i] == 3:
                table4.append(table4_full[21:24])
                continue
            elif options[i] == 2:
                table4.append(table4_full[24:27])
                continue
            else:
                table4.append(table4_full[27:30])
                continue
        elif i == 2:
            if options[i] == 5:
                table4.append(table4_full[30:33])
                continue
            elif options[i] == 4:
                table4.append(table4_full[33:36])
                continue
            elif options[i] == 3:
                table4.append(table4_full[36:39])
                continue
            elif options[i] == 2:
                table4.append(table4_full[39:42])
                continue
            else:
                table4.append(table4_full[42:45])
                continue
        elif i == 3:
            if options[i] == 5:
                table4.append(table4_full[45:48])
                continue
            elif options[i] == 4:
                table4.append(table4_full[48:51])
                continue
            elif options[i] == 3:
                table4.append(table4_full[51:54])
                continue
            elif options[i] == 2:
                table4.append(table4_full[54:57])
                continue
            else:
                table4.append(table4_full[57:60])
                continue
        elif i == 4:
            if options[i] == 5:
                table4.append(table4_full[60:63])
                continue
            elif options[i] == 4:
                table4.append(table4_full[63:66])
                continue
            elif options[i] == 3:
                table4.append(table4_full[66:69])
                continue
            elif options[i] == 2:
                table4.append(table4_full[69:72])
                continue
            else:
                table4.append(table4_full[72:75])
                continue
        elif i == 5:
            if options[i] == 5:
                table4.append(table4_full[75:78])
                continue
            elif options[i] == 4:
                table4.append(table4_full[78:81])
                continue
            elif options[i] == 3:
                table4.append(table4_full[81:84])
                continue
            elif options[i] == 2:
                table4.append(table4_full[84:87])
                continue
            else:
                table4.append(table4_full[87:90])
                continue
        elif i == 6:
            if options[i] == 5:
                table4.append(table4_full[90:93])
                continue
            elif options[i] == 4:
                table4.append(table4_full[93:96])
                continue
            elif options[i] == 3:
                table4.append(table4_full[96:99])
                continue
            elif options[i] == 2:
                table4.append(table4_full[99:102])
                continue
            else:
                table4.append(table4_full[102:105])
                continue
        elif i == 7:
            if options[i] == 5:
                table4.append(table4_full[105:108])
                continue
            elif options[i] == 4:
                table4.append(table4_full[108:111])
                continue
            elif options[i] == 3:
                table4.append(table4_full[111:114])
                continue
            elif options[i] == 2:
                table4.append(table4_full[114:117])
                continue
            else:
                table4.append(table4_full[117:120])
                continue
        elif i == 8:
            if options[i] == 5:
                table4.append(table4_full[120:123])
                continue
            elif options[i] == 4:
                table4.append(table4_full[123:126])
                continue
            elif options[i] == 3:
                table4.append(table4_full[126:129])
                continue
            elif options[i] == 2:
                table4.append(table4_full[129:132])
                continue
            else:
                table4.append(table4_full[132:135])
                continue
        elif i == 9:
            if options[i] == 5:
                table4.append(table4_full[135:138])
                continue
            elif options[i] == 4:
                table4.append(table4_full[138:141])
                continue
            elif options[i] == 3:
                table4.append(table4_full[141:144])
                continue
            elif options[i] == 2:
                table4.append(table4_full[144:147])
                continue
            else:
                table4.append(table4_full[147:150])
                continue
        elif i == 10:
            if options[i] == 1:
                table4.append(table4_full[150:153])
                continue
            else:
                table4.append(table4_full[153:156])
                continue
        elif i == 11:
            if options[i] == 1:
                table4.append(table4_full[156:159])
                continue
            else:
                table4.append(table4_full[159:162])
                continue
        elif i == 12:
            if options[i] == 1:
                table4.append(table4_full[162:165])
                continue
            else:
                table4.append(table4_full[165:168])
                continue
        elif i == 13:
            if options[i] == 1:
                table4.append(table4_full[168:171])
                continue
            else:
                table4.append(table4_full[171:174])
                continue
        elif i == 14:
            if options[i] == 1:
                table4.append(table4_full[174:177])
                continue
            else:
                table4.append(table4_full[177:180])
                continue
        elif i == 15:
            if options[i] == 1:
                table4.append(table4_full[180:183])
                continue
            else:
                table4.append(table4_full[183:186])
                continue
        elif i == 16:
            if options[i] == 1:
                table4.append(table4_full[186:189])
                continue
            else:
                table4.append(table4_full[189:192])
                continue
        elif i == 17:
            if options[i] == 1:
                table4.append(table4_full[192:195])
                continue
            else:
                table4.append(table4_full[195:198])
                continue
        elif i == 18:
            if options[i] == 1:
                table4.append(table4_full[198:201])
                continue
            else:
                table4.append(table4_full[201:204])
                continue
        elif i == 19:
            if options[i] == 1:
                table4.append(table4_full[204:207])
                continue
            else:
                table4.append(table4_full[207:210])
                continue
        else:
            return

    for i in range(len(table4)):
        for j in range(len(table4[i])):
            table4_format.append(table4[i][j])
    return table4_format


def fuzzy_matrix(table4_format):
    global decision_matrix
    decision_matrix = []
    for i in range(len(table4_format)):
        fuzzy_numbers = []
        for j in range(len(table4_format[i])):
            ind = linguistic_pos_table3(table4_format[i][j])
            fuzzy_numbers.append(table3[ind])
        fuzzy_decision_matrix(fuzzy_numbers)


def fuzzy_decision_matrix(numbers):
    global decision_matrix
    trans = numpy.transpose(numbers)
    for i in range(len(trans)):
        if i == 0:
            min_value = min(trans[i])
        elif i == 1:
            avg_value = round(sum(trans[i])/len(trans[i]), 2)
        else:
            max_value = max(trans[i])
    row = [min_value, avg_value, max_value]
    decision_matrix.append(row)


def criteria_weights(table2):
    global weight
    weight = []
    for i in range(len(table2)):
        weights = []
        for j in range(len(table2[i])):
            ind = linguistic_pos_table1(table2[i][j])
            weights.append(table1[ind])
        cal_weights(weights)


def cal_weights(numbers):
    global weight
    trans = numpy.transpose(numbers)
    for i in range(len(trans)):
        if i == 0:
            min_value = min(trans[i])
        elif i == 1:
            avg_value = round(sum(trans[i])/len(trans[i]), 2)
        else:
            max_value = max(trans[i])
    row = [min_value, avg_value, max_value]
    weight.append(row)


def calculate(decision_matrix, table2):
    global weight
    decision_matrix_format = []
    i = 0
    while (i < len(decision_matrix)):
        decision_matrix_format.append(decision_matrix[i:i+3])
        i += 3
    print("Fuzzy Decision Matrix: ")
    for i in decision_matrix_format:
        print(i, end="\n")

    criteria_weights(table2)
    print("\nCriteria Weights: ")
    for i in weight:
        print(i, end="\n")

    max_value_list = []
    for i in range(len(decision_matrix_format)):
        max_value = 0
        for j in range(len(decision_matrix_format[i])):
            if max_value < max(decision_matrix_format[i][j]):
                max_value = max(decision_matrix_format[i][j])
            else:
                continue
        max_value_list.append(max_value)

    normalized_fuzzy_decision_matrix = []
    arr = numpy.array(decision_matrix_format)

    for i in range(len(arr)):
        normalized_fuzzy_decision_matrix.append(numpy.round(
            arr[i]/max_value_list[i], decimals=2).tolist())

    print("\nNormalized Fuzzy Decision Matrix: ")
    for i in normalized_fuzzy_decision_matrix:
        print(i, end="\n")

    weighted_normalized_fuzzy_matrix = []
    for i in range(len(normalized_fuzzy_decision_matrix)):
        row = []
        for j in range(len(normalized_fuzzy_decision_matrix[i])):
            row_inner = []
            for k in range(len(normalized_fuzzy_decision_matrix[i][j])):
                row_inner.append(
                    round(normalized_fuzzy_decision_matrix[i][j][k]*weight[i][k], 2))
            row.append(row_inner)
        weighted_normalized_fuzzy_matrix.append(row)

    print("\nWeighted Normalized Fuzzy Decision Matrix: ")
    for i in weighted_normalized_fuzzy_matrix:
        print(i, end="\n")

    arr_value = numpy.array(weighted_normalized_fuzzy_matrix)
    max_value = []
    min_value = []
    for i in range(len(arr_value)):
        max_value.append(numpy.max(arr_value[i]))
        min_value.append(numpy.min(arr_value[i]))

    a_star = []
    a_minus = []
    for i, j in zip(max_value, min_value):
        row_max = [i, i, i]
        row_min = [j, j, j]
        a_star.append(row_max)
        a_minus.append(row_min)

    print("\nA* ")
    for i in a_star:
        print(i, end="\n")

    print("\nA- ")
    for i in a_minus:
        print(i, end="\n")

    a_starA_temp = []
    for i in range(len(weighted_normalized_fuzzy_matrix)):
        row = []
        for j in range(len(weighted_normalized_fuzzy_matrix[i])):
            val = 0
            for k in range(len(weighted_normalized_fuzzy_matrix[i][j])):
                val += (a_star[i][0] -
                        weighted_normalized_fuzzy_matrix[i][j][k]) ** 2
            val = val/3
            val = val ** 0.5
            row.append(round(val, 2))
        a_starA_temp.append(row)

    a_starA_temp = numpy.transpose(a_starA_temp)
    a_starA = a_starA_temp.tolist()

    print("\nd(Ai,A*): ")
    for i in a_starA:
        print(i, end="\n")

    a_minusA_temp = []
    for i in range(len(weighted_normalized_fuzzy_matrix)):
        row = []
        for j in range(len(weighted_normalized_fuzzy_matrix[i])):
            val = 0
            for k in range(len(weighted_normalized_fuzzy_matrix[i][j])):
                val += (a_minus[i][0] -
                        weighted_normalized_fuzzy_matrix[i][j][k]) ** 2
            val = val/3
            val = val ** 0.5
            row.append(round(val, 2))
        a_minusA_temp.append(row)

    a_minusA_temp = numpy.transpose(a_minusA_temp)
    a_minusA = a_minusA_temp.tolist()

    print("\nd(Ai,A-): ")
    for i in a_minusA:
        print(i, end="\n")

    di_minus_sum = []
    for i in range(len(a_minusA)):
        sum = 0
        for j in range(len(a_minusA[i])):
            sum += a_minusA[i][j]
        di_minus_sum.append(round(sum, 2))

    di_star_sum = []
    for i in range(len(a_starA)):
        sum = 0
        for j in range(len(a_starA[i])):
            sum += a_starA[i][j]
        di_star_sum.append(round(sum, 2))

    cc = []
    for i, j in zip(di_minus_sum, di_star_sum):
        val = i/(i+j)
        val = round(val, 2)
        cc.append(val)

    sorted_list = numpy.array(cc)
    sorted_list_indices = numpy.argsort(sorted_list)
    sorted_list_indices = sorted_list_indices[::-1].tolist()
    sorted_cc = sorted(cc, reverse=True)
    # print("\nCC: ")
    # for i,j in zip(sorted_cc,sorted_list_indices):
    #     print("CC"+str(j+1)+": ",i," -> A"+str(j+1))

    return sorted_cc, sorted_list_indices


def classification_C1(choices):
    global decision_matrix
    global weight
    options = choices

    questions = [
        "Are you getting periods regularly (on time)?",
        "What is the typical length of your menstrual cycle?",
        "What is the usual duration of the flow?",
        "How heavy would you say your menstrual flow is?",
        "During your menstruating period, did you have a tendency to grow dark, coarse hair on chest and chin?",
        "Have you gained weight in the recent times?",
        "Would you describe yourself as someone who eats junk foods frequently?",
        "How would you rate your meal times and eating patterns?",
        "How would you rate your sleep schedule/pattern?",
        "Does anybody in your immediate family (parents,siblings) have history of Diabetes?",
        "Does anybody in your immediate family (parents,siblings) have history of Hypertension?"
    ]

    answers = [
        ['Yes', 'No'],
        ['1 month', '45 days', '2-3 months'],
        ['Less than a day', '5-7 days', 'More than 7 days'],
        ['Less than 3 pads', '3-5 pads', 'More than 5 pads'],
        ['Yes', 'No'],
        ['Yes', 'No'],
        ['Very Frequently', 'Some times', 'Not at all'],
        ['Regular', 'Fairly regular', 'Quite irregular',
            'I am never able to follow any schedule'],
        ['I follow a regular sleep pattern', 'My sleep pattern is fairly regular',
            'My sleep pattern Quite irregular', 'I am never able to follow any schedule'],
        ['Diabetes-Yes', 'Diabetes-No'],
        ['Hypertension-Yes', 'Hypertension-No']
    ]

    table2 = [
        ['VHR', 'VHR', 'VHR'],  # C11
        ['VHR', 'VHR', 'VHR'],  # C12
        ['VHR', 'VHR', 'VHR'],  # C13
        ['VHR', 'VHR', 'VHR'],  # C14
        ['HR', 'HR', 'HR'],  # C15
        ['VHR', 'HR', 'VHR'],  # C16
        ['HR', 'HR', 'HR'],  # C17
        ['HR', 'HR', 'HR'],  # C18
        ['HR', 'HR', 'HR'],  # C19
        ['R', 'R', 'R'],  # C110
        ['R', 'R', 'R']  # C111
    ]

    table4_full_c1 = [
        # C11
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        # C12
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'M', 'L'],
        ['H', 'H', 'H'],
        ['L', 'L', 'M'],
        ['H', 'M', 'M'],
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        # C13
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['M', 'M', 'H'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['M', 'L', 'L'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['M', 'L', 'M'],
        # C14
        ['H', 'H', 'H'],
        ['L', 'L', 'M'],
        ['L', 'M', 'M'],
        ['L', 'L', 'L'],
        ['VH', 'VH', 'VH'],
        ['M', 'M', 'H'],
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'M', 'M'],
        # C15
        ['VH', 'H', 'H'],
        ['L', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['VL', 'L', 'L'],
        ['H', 'VH', 'H'],
        ['L', 'M', 'M'],
        # C16
        ['VH', 'H', 'H'],
        ['L', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['VL', 'L', 'L'],
        ['H', 'VH', 'H'],
        ['L', 'M', 'M'],
        # C17
        ['VH', 'H', 'H'],
        ['VL', 'L', 'L'],
        ['H', 'M', 'M'],
        ['L', 'M', 'M'],
        ['H', 'M', 'M'],
        ['M', 'H', 'H'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C18
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        ['VL', 'L', 'L'],
        ['VH', 'H', 'H'],
        ['L', 'M', 'M'],
        ['H', 'H', 'H'],
        ['L', 'L', 'L'],
        ['H', 'M', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'H', 'M'],
        # C19
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        ['VL', 'L', 'L'],
        ['VH', 'H', 'H'],
        ['L', 'M', 'M'],
        ['H', 'H', 'H'],
        ['L', 'L', 'L'],
        ['H', 'M', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'H', 'M'],
        # C110-DIABETES
        ['H', 'H', 'M'],
        ['L', 'L', 'M'],
        ['H', 'H', 'VH'],
        ['L', 'M', 'L'],
        ['H', 'H', 'M'],
        ['L', 'L', 'VL'],
        # C111-HYPERTENSION
        ['H', 'H', 'M'],
        ['L', 'L', 'M'],
        ['H', 'H', 'VH'],
        ['L', 'M', 'L'],
        ['H', 'H', 'M'],
        ['L', 'L', 'VL']
    ]

    # for i in range(len(questions)):
    #     print("\n", str(i+1), ")", questions[i])
    #     for j in range(len(answers[i])):
    #         print("\n", str(j+1), ".", answers[i][j])
    #     val = int(input("\n Enter option: "))
    #     options.append(val)

    table4_format = create_table4_C1(options, table4_full_c1)
    fuzzy_matrix(table4_format)
    c1, c1_indices = calculate(decision_matrix, table2)

    return c1, c1_indices


def classification_Crest(choices):
    global weight
    global decision_matrix
    options = choices

    questions = [
        # C2
        "How often did you feel tired out for no good reason?(D)",
        "How often did you feel nervous?(A)",
        "How often did you feel so nervous that nothing could calm you down?(A)",
        "How often did you feel hopeless?(D)",
        "How often did you feel restless or fidgety?(A)",
        "How often did you feel so restless you could not sit still?(A)",
        "How often did you feel depressed?(D)",
        "How often did you feel that everything was an effort?(D)",
        "How often did you feel so sad that nothing could cheer you up?(D)",
        "How often did you feel worthless?(D)",
        # C3
        "Intense and persistent fear in social situations in which you feel others might evaluate you?",
        "Fear of being humiliated and/or embarrassed in social situations?",
        "Feeling extremely self-conscious(being the center of attention)?",
        "Fears that others will notice your blushing, sweating?",
        "Do you try very hard to avoid social situations/interactions?",
        # C4
        "Do you spend a lot of time worrying about how your appearance(weight,facial hair,skin)?",
        "Do you experience dissatisfaction with your appearance/body?",
        "Do you avoid wearing certain clothes because it may make you feel fat?",
        "Do you often compare your appearance/self with others and feel low?",
        "Does your dissatisfaction and or self-consciousness with your appearance interfere with your activities and interactions (Eg avoidance of activities, or have to use many measures/such as make up)?"
    ]

    answers = [
        # C2
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        ['None of the time', 'A little of the time',
            'some of the time', 'Most of the time', 'All of the time'],
        # C3
        ['Yes', 'No'],
        ['Yes', 'No'],
        ['Yes', 'No'],
        ['Yes', 'No'],
        ['Yes', 'No'],
        # C4
        ['Yes', 'No'],
        ['Yes', 'No'],
        ['Yes', 'No'],
        ['Yes', 'No'],
        ['Yes', 'No'],
    ]

    table2 = [
        # C2
        ['VHR', 'VHR', 'VHR'],  # C21
        ['VHR', 'HR', 'VHR'],  # C22
        ['VHR', 'HR', 'VHR'],  # C23
        ['HR', 'HR', 'HR'],  # C24
        ['VHR', 'VHR', 'VHR'],  # C25
        ['HR', 'VHR', 'VHR'],  # C26
        ['HR', 'HR', 'HR'],  # C27
        ['HR', 'HR', 'HR'],  # C28
        ['HR', 'R', 'R'],  # C29
        ['HR', 'HR', 'R'],  # C210
        # C3
        ['HR', 'HR', 'HR'],  # C31
        ['HR', 'HR', 'HR'],  # C32
        ['HR', 'HR', 'HR'],  # C33
        ['HR', 'HR', 'HR'],  # C34
        ['HR', 'HR', 'HR'],  # C35
        # C4
        ['VHR', 'VHR', 'VHR'],  # C41
        ['VHR', 'VHR', 'VHR'],  # C42
        ['HR', 'HR', 'HR'],  # C43
        ['R', 'R', 'R'],  # C44
        ['LR', 'LR', 'LR']  # C45
    ]

    table4_full_crest = [
        # C21
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C22
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C23
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C24
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C25
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C26
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C27
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C28
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C29
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C210
        ['VH', 'VH', 'VH'],
        ['VL', 'VL', 'VL'],
        ['H', 'H', 'M'],
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'M', 'M'],
        ['H', 'H', 'M'],
        ['M', 'M', 'H'],
        ['M', 'M', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'M', 'M'],
        ['VL', 'VL', 'VL'],
        ['VH', 'VH', 'VH'],
        ['L', 'L', 'M'],
        # C31
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'H', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        # C32
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'H', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        # C33
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'H', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        # C34
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'H', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        # C35
        ['VH', 'VH', 'H'],
        ['VL', 'VL', 'L'],
        ['H', 'H', 'M'],
        ['VL', 'VL', 'L'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        # C41
        ['H', 'H', 'VH'],
        ['VL', 'L', 'VL'],
        ['H', 'H', 'M'],
        ['L', 'L', 'VL'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        # C42
        ['H', 'H', 'VH'],
        ['VL', 'L', 'VL'],
        ['H', 'H', 'M'],
        ['L', 'L', 'VL'],
        ['VH', 'VH', 'H'],
        ['L', 'L', 'M'],
        # C43
        ['H', 'H', 'M'],
        ['VL', 'L', 'L'],
        ['H', 'M', 'M'],
        ['L', 'L', 'M'],
        ['VH', 'H', 'H'],
        ['L', 'M', 'M'],
        # C44
        ['H', 'H', 'M'],
        ['VL', 'L', 'L'],
        ['H', 'M', 'M'],
        ['L', 'L', 'M'],
        ['VH', 'H', 'H'],
        ['L', 'M', 'M'],
        # C45
        ['H', 'H', 'M'],
        ['VL', 'L', 'L'],
        ['H', 'M', 'M'],
        ['L', 'L', 'M'],
        ['VH', 'H', 'H'],
        ['L', 'M', 'M'],
    ]

    # for i in range(len(questions)):
    #     if i == 0:
    #         print("\nAnxiety and Depression")
    #         print(
    #             "---------------------------------------------------------------------------")
    #     elif i == 10:
    #         print("\nSocial Phobia")
    #         print(
    #             "---------------------------------------------------------------------------")
    #     elif i == 15:
    #         print("\nBody Image")
    #         print(
    #             "---------------------------------------------------------------------------")
    #     else:
    #         pass
    #     if i >= 10 and i <= 14:
    #         print("\nAre you troubled by the following: ")
    #     print("\n", str(i+1), ")", questions[i])
    #     for j in range(len(answers[i])):
    #         print("\n", str(j+1), ".", answers[i][j])
    #     val = int(input("\n Enter option: "))
    #     options.append(val)

    table4_format = create_table4_Crest(options, table4_full_crest)
    fuzzy_matrix(table4_format)
    crest, crest_indicies = calculate(decision_matrix, table2)

    return crest, crest_indicies


def main():
    print("\n\nPCOS Questionnaire")
    print("---------------------------------------------------------------------------")
    c1, c1_indicies = classification_C1()
    print("\n\nMental Health Questionnaire")
    print("---------------------------------------------------------------------------")
    crest, crest_indicies = classification_Crest()

    print("---------------------------------------------------------------------------")
    print("\nA1 -> High Probability \nA2 -> Normal \nA3 -> Moderate Probability")
    print("\nCC PCOS: ")
    for i, j in zip(c1, c1_indicies):
        print("CC"+str(j+1)+": ", i, " -> A"+str(j+1))

    print("\nCC Mental Health: ")
    for i, j in zip(crest, crest_indicies):
        print("CC"+str(j+1)+": ", i, " -> A"+str(j+1))

    # 0-high
    # 1-normal
    # 2-moderate

    if c1_indicies[0] == 0:
        if crest_indicies[0] == 0:
            print("\nA1-High probability of both PCOS and Mental Health issues.")
        elif crest_indicies[0] == 1:
            print("\nA2-High probability of PCOS issues.")
        else:
            print(
                "\nA5-High probability of PCOS issues with moderate probability of Mental Health issues.")
    elif c1_indicies[0] == 1:
        if crest_indicies[0] == 0:
            print("\nA3-High probability of Mental Health issues.")
        elif crest_indicies[0] == 1:
            print("\nA4-Normal")
        else:
            print("\nA8-Moderate probability of Mental Health issues.")
    else:
        if crest_indicies[0] == 0:
            print(
                "\nA6-Moderate probability of PCOS issues with high probability of Mental Health issues.")
        elif crest_indicies[0] == 1:
            print("\nA7-Moderate probability of PCOS issues.")
        else:
            print(
                "\nA9-Moderate probability of both PCOS issues and Mental Health issues.")


def predictRes(res):

    c1, c1_indicies = classification_C1(res[:11])

    crest, crest_indicies = classification_Crest(res[11:])

    # 0-high
    # 1-normal
    # 2-moderate
    result = ""
    if c1_indicies[0] == 0:
        if crest_indicies[0] == 0:
            result += "High probability of both PCOS and Mental Health issues."
        elif crest_indicies[0] == 1:
            result += "High probability of PCOS issues."
        else:
            result += "High probability of PCOS issues with moderate probability of Mental Health issues."
    elif c1_indicies[0] == 1:
        if crest_indicies[0] == 0:
            result += "High probability of Mental Health issues."
        elif crest_indicies[0] == 1:
            result += "Normal"
        else:
            result += "Moderate probability of Mental Health issues."
    else:
        if crest_indicies[0] == 0:
            result += "Moderate probability of PCOS issues with high probability of Mental Health issues."
        elif crest_indicies[0] == 1:
            result += "Moderate probability of PCOS issues."
        else:
            result += "Moderate probability of both PCOS issues and Mental Health issues."

    return result


# main()
