__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd


class Segment:

    def __init__(self, seq_sep_inferior=None, seq_sep_superior=None):
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior

    def toPair(self, fas_lower, fas_upper):
        if fas_lower == [] and fas_upper == []:
            return []
        else:
            df_ = pd.DataFrame(self.iudsna(fas_lower, fas_upper))
            pairs = self.extract(
                df=df_,
                first=0,
                second=1,
            ).values.tolist()
            return pairs

    def extract(self, df, first, second):
        df_ = df
        if self.seq_sep_inferior is not None and self.seq_sep_superior is None:
            query = (df_[second] - df_[first] > self.seq_sep_inferior)
        elif self.seq_sep_inferior is None and self.seq_sep_superior is not None:
            query = (df_[second] - df_[first] < self.seq_sep_superior)
        elif self.seq_sep_inferior is not None and self.seq_sep_superior is not None:
            ss_inf = df_[second] - df_[first] > self.seq_sep_inferior
            ss_sup = df_[second] - df_[first] < self.seq_sep_superior
            query = (ss_inf & ss_sup)
        else:
            query = (0 < df_[second] - df_[first])
        df_ = df_.loc[query].sort_values(
            by=[first, second],
            ascending=True
        )
        df_ = df_.loc[query]
        df_ = df_.reset_index(inplace=False, drop=True)
        return df_

    def iudsna(self, inf_arr, sup_arr):
        conerants2 = []
        p8 = len(inf_arr)
        for i in range(p8):
            conerants2.append(list(np.arange(inf_arr[i], sup_arr[i] + 1)))
        iutucy = []
        for i in range(p8):
            for j in range(p8):
                if i < j:
                    for p in range(len(conerants2[i])):
                        for q in range(len(conerants2[j])):
                            iutucy.append([conerants2[i][p], conerants2[j][q]])
        return iutucy