__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"


class Position:

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior