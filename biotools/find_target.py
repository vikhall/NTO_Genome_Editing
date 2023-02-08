import regex as re

def find_target(seq, pam, pos, length):
    """
    Эта функция выполняет поиска таргета для системы геномного редактирования CRISPR/Cas9
    :param seq: последовательность, в которой будет выполняться поиск таргета
    :param pam: последовательность PAM
    :param pos: позиция PAM относительно таргета (R - на 3'-конце, L - на 5'-конце)
    :param length: длина таргета
    :return:
    """
    rev_dict = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    seq_rev_compl = ''.join([rev_dict[s] for s in seq[::-1]])

    nucl_dict = {
        'A': 'A',
        'T': 'T',
        'G': 'G',
        'C': 'C',
        'R': '[AG]',
        'Y': '[CT]',
        'N': '[ATGC]'
    }

    pattern = ''.join([nucl_dict[n] for n in pam])

    if pos == 'R':
        pattern = ".{" + str(length) + "}" + pattern
        target_f = re.findall(pattern, seq, overlapped=True)
        target_f = list(map(lambda x: x[:-len(pam)], target_f))

        target_r = re.findall(pattern, seq_rev_compl, overlapped=True)
        target_r = list(map(lambda x: x[:-len(pam)], target_r))

    else:
        pattern = pattern + ".{" + str(length) + "}"
        target_f = re.findall(pattern, seq, overlapped=True)
        target_f = list(map(lambda x: x[len(pam):], target_f))

        target_r = re.findall(pattern, seq_rev_compl, overlapped=True)
        target_r = list(map(lambda x: x[len(pam):], target_r))

    print(target_f + target_r)

    return target_f + target_r
