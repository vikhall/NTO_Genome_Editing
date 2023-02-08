def check_primer(seq, min_gc=50, max_gc=60, min_len=18, max_len=25):
    gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
    length = len(seq)

    return (min_gc <= gc <= max_gc) and (min_len <= length <= max_len)


def is_self_compliment(seq, compl):
    rev_dict = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    seq_rev_compl = ''.join([rev_dict[s] for s in seq[::-1]])

    if seq_rev_compl[:compl] in seq:
        return True

    return False


def calculate_tm(seq):
    return round(64.9 + 41 * (seq.count('G') + seq.count('C') - 16.4) / (seq.count('A') + seq.count('T') + seq.count('G') + seq.count('C')))


def get_primer(seq, length, min_gc=50, max_gc=60, min_temp=50, max_temp=60, max_self_compl=4):
    for i in range(0, len(seq) - length - 1):
        primer = seq[i:i + length]

        if check_primer(primer, min_gc, max_gc) and not is_self_compliment(primer, max_self_compl + 1) and (
                min_temp <= calculate_tm(primer) <= max_temp):
            return primer

    return False


def get_reverse_primer(seq, forward, length, min_ampl, max_ampl, min_gc=50, max_gc=60, min_temp=50, max_temp=60,
                       max_self_compl=4):
    start_pos = seq.find(forward) + min_ampl - length
    end_pos = end if (end := seq.find(forward) + max_ampl) <= len(seq) else len(seq)

    target_seq = seq[start_pos:end_pos]

    rev_dict = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    target_seq_rev_compl = ''.join([rev_dict[s] for s in target_seq[::-1]])

    return get_primer(target_seq_rev_compl, length)