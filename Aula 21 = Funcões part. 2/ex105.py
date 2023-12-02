def grades(*students_grades, sit=False):

    """
    -> Function to analyse grades and situations of several students
    :param students_grades: one or more student's grades (accepts several)
    :param sit: optional value to indicate if "situation" should be or not added.
    :return: a dictionary with a lot of information about the class.
    """

    dict_grades = dict()

    dict_grades['total'] = len(students_grades)
    dict_grades['major'] = max(students_grades)
    dict_grades['minor'] = min(students_grades)
    dict_grades['average'] = sum(students_grades) / len(students_grades)

    if sit:
        if dict_grades['average'] >= 7:
            dict_grades['sit'] = 'GOOD'

        elif 7 > dict_grades['average'] > 4:
            dict_grades['sit'] = 'REASONABLE'

        elif dict_grades['average'] <= 4:
            dict_grades['sit'] = 'BAD'

    return dict_grades


resp = grades(3.5, 2, 6.5, sit=True)

print(resp)
help(grades)
