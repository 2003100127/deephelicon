__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class Pair:

    def __init__(self, sequence, position, window_size):
        self.sequence = sequence
        self.aa_pairs = position
        self.window_size = window_size
        self.len_seq = len(self.sequence)
        self.num_pairs = len(self.aa_pairs)

    def aaid(self):
        window_aa_ids = [[[] for _ in range(2)] for _ in range(self.num_pairs)]
        for i in range(self.num_pairs):
            for aa1_left_id in range(self.window_size):
                window_aa_ids[i][0].append(self.aa_pairs[i][0] - (aa1_left_id + 1))
            for aa1_right_id in range(self.window_size):
                window_aa_ids[i][0].append(self.aa_pairs[i][0] + (aa1_right_id + 1))
            window_aa_ids[i][0].append(self.aa_pairs[i][0])

        for i in range(self.num_pairs):
            for aa2_left_id in range(self.window_size):
                window_aa_ids[i][1].append(self.aa_pairs[i][3] - (aa2_left_id + 1))
            for aa2_right_id in range(self.window_size):
                window_aa_ids[i][1].append(self.aa_pairs[i][3] + (aa2_right_id + 1))
            window_aa_ids[i][1].append(self.aa_pairs[i][3])
        for i in range(self.num_pairs):
            for j in range(self.window_size * 2 + 1):
                if window_aa_ids[i][0][j] < 1 or window_aa_ids[i][0][j] > self.len_seq:
                    window_aa_ids[i][0][j] = None
                if window_aa_ids[i][1][j] < 1 or window_aa_ids[i][1][j] > self.len_seq:
                    window_aa_ids[i][1][j] = None
        return window_aa_ids