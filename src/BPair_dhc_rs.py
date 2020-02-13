__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')


class pair_dhc_rs(object):

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