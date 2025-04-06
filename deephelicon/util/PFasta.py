__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class PFasta:

    def __init__(self, sequence):
        self.sequence = sequence
        self.len_seq = len(self.sequence)

    def pair(self, pos_list):
        seq_dict = self.todict(self.sequence)
        len_pairs = len(pos_list)
        dist_matrix = []
        for i in range(len_pairs):
            fas_id1 = pos_list[i][0]
            fas_id2 = pos_list[i][1]
            dist_matrix.append([
                fas_id1,
                seq_dict[fas_id1],
                fas_id1,
                fas_id2,
                seq_dict[fas_id2],
                fas_id2,
                0
            ])
        return dist_matrix

    def todict(self, seq):
        seq_dict = {}
        len_seq = len(seq)
        for i in range(len_seq):
            seq_dict[i + 1] = seq[i]
        return seq_dict