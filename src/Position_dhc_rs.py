__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')


class position_dhc_rs(object):

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior