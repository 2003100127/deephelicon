__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from deephelicon.util.Position import Position


class Separation(Position):

    def __init__(self, df, first=None, second=None, is_sort=False, target=None, seq_sep_inferior=None, seq_sep_superior=None):
        super(Separation, self).__init__(seq_sep_inferior, seq_sep_superior)
        self.df = df
        self.seq_sep_inferior = seq_sep_inferior
        self.seq_sep_superior = seq_sep_superior
        self.first = first
        self.second = second
        self.is_sort = is_sort
        self.target = target

    def extract(self):
        df_ = self.df
        if self.seq_sep_inferior is not None and self.seq_sep_superior is None:
            query = (df_[self.second] - df_[self.first] > self.seq_sep_inferior)
        elif self.seq_sep_inferior is None and self.seq_sep_superior is not None:
            query = (df_[self.second] - df_[self.first] < self.seq_sep_superior)
        elif self.seq_sep_inferior is not None and self.seq_sep_superior is not None:
            ss_inf = df_[self.second] - df_[self.first] > self.seq_sep_inferior
            ss_sup = df_[self.second] - df_[self.first] < self.seq_sep_superior
            query = (ss_inf & ss_sup)
        else:
            query = (0 < df_[self.second] - df_[self.first])
        df_ = df_.loc[query].sort_values(
            by=[self.first, self.second],
            ascending=True
        )
        if self.is_sort:
            df_ = df_.loc[query].sort_values([self.target], ascending=False)
        else:
            df_ = df_.loc[query]
        df_ = df_.reset_index(inplace=False, drop=True)
        return df_
