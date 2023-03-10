def get_rev_compl(seq: str):
    """
    Эта функция возвращает обратно комплиментарную последовательность
    :param seq: последовательность ДНК (должна содержать только символы ATGC)
    :return: обратно-комплиментарная последовательность
    """
    compl_dict = {'A':'T','T':'A','G':'C','C':'G'}

    return ''.join([compl_dict[s] for s in seq[::-1]])