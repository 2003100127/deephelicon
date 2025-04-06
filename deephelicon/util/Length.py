__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd
from deephelicon.util.Position import Position
from deephelicon.util.Separation import Separation


class Length(Position):

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        super(Length, self).__init__(seq_sep_inferior, seq_sep_superior)

    def num2arr(self, length):
        arr = []
        for i in range(length):
            for j in range(length):
                if i < j:
                    arr.append([i + 1, j + 1])
        return arr

    def toPair(self, length):
        df_ = pd.DataFrame(self.num2arr(length))
        pairs = Separation(
            df=df_,
            first=0,
            second=1,
            is_sort=False,
            seq_sep_inferior=self.seq_sep_inferior,
            seq_sep_superior=self.seq_sep_superior
        ).extract().values.tolist()
        return pairs