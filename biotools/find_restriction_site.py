import re


def find_restriction_site(site: str, sequence: str):
    """
    Эта функция ищет сайт узнавания растриктазы в последовательности
    :param site: Сайт узнавания рестриктазы (str)
    :param sequence: Последовательность, в которой будет выполняться поиск (str)
    :return: bool: присутствует ли сайт узнавания в последовательность (True/False)
    """
    nucl_dict = {
        'A': 'A',
        'T': 'T',
        'G': 'G',
        'C': 'C',
        'R': '[AG]',
        'Y': '[CT]',
        'N': '[ATGC]'
    }
    pattern = ''

    for s in site:
        pattern += nucl_dict[s]

    return bool(re.search(pattern, sequence))