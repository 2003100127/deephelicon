__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import pandas as pd
from src.Position_dhc_rs import position_dhc_rs
from src.Separation_dhc_rs import separation_dhc_rs


class length_dhc_rs(position_dhc_rs):

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        super(length_dhc_rs, self).__init__(seq_sep_inferior, seq_sep_superior)

    def num2arr(self, length):
        arr = []
        for i in range(length):
            for j in range(length):
                if i < j:
                    arr.append([i + 1, j + 1])
        return arr

    def toPair(self, length):
        df_ = pd.DataFrame(self.num2arr(length))
        pairs = separation_dhc_rs(
            df=df_,
            first=0,
            second=1,
            is_sort=False,
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior
        ).extract().values.tolist()
        return pairs