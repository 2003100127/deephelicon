__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class Index:

    def __init__(self, sequence):
        self.sequence = sequence
        self.len_seq = len(self.sequence)

    def get(self):
        ids = []
        for id in range(self.len_seq):
            ids.append(id + 1)
        return ids