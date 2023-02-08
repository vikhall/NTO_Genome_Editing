def calculate_lig(c2_fragm: float, c2_plasm: float, c1_fragm=0.5, c1_plasm=0.1, v1=20.0):
    """
    Эта функция рассчитывает реакцию лигирования
    :param c2_fragm: Концентрация фрагмента (float)
    :param c2_plasm: Концентрация плазмиды (float)
    :param c1_fragm: Концентрация фрагмента в растворе (float)
    :param c1_plasm: Концентрация плазмиды в растворе (float)
    :param v1: Объем раствора реакции (float)
    :return: None
    """
    c1v1_fragm = c1_fragm * v1
    c1v1_plasm = c1_plasm * v1

    v2_fragm = round(c1v1_fragm / c2_fragm, 2)
    v2_plasm = round(c1v1_plasm / c2_plasm, 2)
    vh20 = round(20 - 1 - 2 - v2_fragm - v2_plasm, 2)

    if vh20 > 0:
        print(v2_fragm, v2_plasm, vh20)
    else:
        print('невозможно приготовить реакционную смесь при данных концентрациях растворов')