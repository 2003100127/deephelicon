__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class BPair:

    def __init__(self, sequence, window_size, window_aa_ids):
        self.sequence = sequence
        self.window_size = window_size
        self.window_aa_ids = window_aa_ids
        self.num_pairs = len(self.window_aa_ids)
        self.stretch_window = int((self.window_size * 2 + 1) * (self.window_size * 2) / 2)

    def patch(self, length, step=1):
        arr = []
        for i in range(-length, length + 1, step):
            for j in range(-length, length + 1, step):
                arr.append([i, j])
        return arr