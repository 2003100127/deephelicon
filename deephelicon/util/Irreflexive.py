__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd
from deephelicon.util.BPair import BPair
from deephelicon.util.Reader import Reader as pfreader
from deephelicon.util.Separation import Separation as ppssep


class Irreflexive(BPair):

    def __init__(self, sequence=None, window_size=None, window_aa_ids=None, kind='memconp', patch_size=None):
        super(Irreflexive, self).__init__(sequence, window_size, window_aa_ids)
        if kind == 'memconp':
            self.to_dos = [
                [4, -4], [4, 4], [3, -4], [-4, 3], [3, 4],
                [4, 3], [0, -4], [0, 4], [0, -3], [0, 3],
                [-1, 0], [1, 0], [0, 0], [0, -1], [0, 1],
                [3, 0], [-3, 0], [4, 0], [-4, 0], [-3, -4],
                [-4, -3], [-3, 4], [4, -3], [-4, -4], [-4, 4]
            ]
        if kind == 'patch':
            self.to_dos = self.patch(length=patch_size)
        self.num_to_dos = len(self.to_dos)
        self.pfreader = pfreader()

    def pairIds(self):
        n = len(self.sequence)
        num_pending = len(self.to_dos)
        num_aa_in_window = len(self.window_aa_ids[0][0])
        global_pair_ids = [[] for _ in range(self.num_pairs)]
        for i in range(self.num_pairs):
            for j in range(num_aa_in_window):
                if self.window_aa_ids[i][0][j] is None or self.window_aa_ids[i][1][j] is None:
                    for k in range(num_pending):
                        global_pair_ids[i].append([None, None])
                else:
                    for k in range(num_pending):
                        left = self.window_aa_ids[i][0][j] - self.to_dos[k][0]
                        right = self.window_aa_ids[i][1][j] - self.to_dos[k][1]
                        left_inf = left < 1
                        left_sup = left > n
                        right_inf = right < 1
                        right_sup = right > n
                        reflexive = left == right
                        if left_inf or left_sup or right_inf or right_sup or reflexive:
                            global_pair_ids[i].append([None, None])
                        else:
                            if left < right:
                                global_pair_ids[i].append([left, right])
                            else:
                                global_pair_ids[i].append([right, left])
        return global_pair_ids

    def assign(self, list_2d, prot_name, file_chain, dhc_suffix, fc_path=None, cp_path=None, plmc_path=None, gdca_path=None, mi_path=None, dhc_path=None, pair_list_uniform=None):
        list_2d_ = list_2d
        global_pair_ids = self.pairIds()
        pairs_left = []
        pairs_right = []
        for i in range(self.num_pairs):
            for j in range(self.num_to_dos * (2 * self.window_size + 1)):
                pairs_left.append(global_pair_ids[i][j][0])
                pairs_right.append(global_pair_ids[i][j][1])
        mark = len(pairs_left)
        if fc_path is not None:
            evfold_dict = self.freecontact(
                fc_path=fc_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=5
            )
            FCj = 0
            for i in range(mark):
                if i % (self.num_to_dos * (2 * self.window_size + 1)) == 0:
                    FCj += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[FCj - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    list_2d_[FCj - 1].append(evfold_dict[inf][sup])
        if cp_path is not None:
            ccmpred_dict = self.ccmpred(
                cp_path=cp_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=5
            )
            CPj = 0
            for i in range(mark):
                if i % (self.num_to_dos * (2 * self.window_size + 1)) == 0:
                    CPj += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[CPj - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    list_2d_[CPj - 1].append(ccmpred_dict[inf][sup])
        if plmc_path is not None:
            plmc_dict = self.plmc(
                plmc_path=plmc_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=5
            )
            PCj = 0
            for i in range(mark):
                if i % (self.num_to_dos * (2 * self.window_size + 1)) == 0:
                    PCj += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[PCj - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    list_2d_[PCj - 1].append(plmc_dict[inf][sup])
        if gdca_path is not None:
            gdca_dict = self.gdca(
                gdca_path=gdca_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=5
            )
            GDCAj = 0
            for i in range(mark):
                if i % (self.num_to_dos * (2 * self.window_size + 1)) == 0:
                    GDCAj += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[GDCAj - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    list_2d_[GDCAj - 1].append(gdca_dict[inf][sup])
        if mi_path is not None:
            mi_dict = self.mi(
                mi_path=mi_path,
                file_name=prot_name,
                file_chain=file_chain,
                sort_=5
            )
            MIj = 0
            for i in range(mark):
                if i % (self.num_to_dos * (2 * self.window_size + 1)) == 0:
                    MIj += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[MIj - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    list_2d_[MIj - 1].append(mi_dict[inf][sup])
        if dhc_path is not None:
            dhc_dict = self.dhc(
                dhc_path=dhc_path,
                file_name=prot_name,
                file_chain=file_chain,
                file_suffix=dhc_suffix,
                pair_list=pair_list_uniform,
                sort_=5
            )
            TMA165j = 0
            for i in range(mark):
                if i % (self.num_to_dos * (2 * self.window_size + 1)) == 0:
                    TMA165j += 1
                if pairs_left[i] is None or pairs_right[i] is None:
                    list_2d_[TMA165j - 1].append(0)
                else:
                    inf = pairs_left[i]
                    sup = pairs_right[i]
                    list_2d_[TMA165j - 1].append(dhc_dict[inf][sup])
        return list_2d_

    def ttttt(self, arr_2d):
        result = {}
        len_arr = len(arr_2d[0])
        if len_arr == 3:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2]})
        else:
            for item in arr_2d:
                result.setdefault(item[0], {}).update({item[1]: item[2:]})
        return result

    def weqd(self, recombine):
        arr_2d = recombine.values.tolist()
        dicts = self.ttttt(arr_2d)
        return dicts

    def mi(self, mi_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            mi_path + file_name + file_chain + '.evfold',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'score',
            'FC_score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 5:
            recombine_dict = self.weqd(recombine)
            return recombine_dict

    def freecontact(self, fc_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            fc_path + file_name + file_chain + '.evfold',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'MI_score',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 5:
            recombine_dict = self.weqd(recombine)
            return recombine_dict

    def ccmpred(self, cp_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        file_results = self.pfreader.generic(
            cp_path + file_name + file_chain + '.ccmpred',
            df_sep='\s+',
            is_utf8=True
        )
        results = []
        for i, row in file_results.iterrows():
            for j in range(file_results.shape[1]):
                if i < j:
                    results.append([i + 1, j + 1, row[j]])
        results = pd.DataFrame(results)
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 5:
            recombine_dict = self.weqd(recombine)
            return recombine_dict

    def gdca(self, gdca_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            gdca_path + file_name + file_chain + '.gdca',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'contact_id_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 5:
            recombine_dict = self.weqd(recombine)
            return recombine_dict

    def plmc(self, plmc_path, file_name, file_chain, sort_=0):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            plmc_path + file_name + file_chain + '.plmc',
            df_sep='\s+',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'placeholder',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 5:
            recombine_dict = self.weqd(recombine)
            return recombine_dict

    def dhc(self, dhc_path, file_name, file_chain, file_suffix, pair_list=None, sort_=0):
        self.__sort_ = sort_
        results = self.pfreader.generic(
            dhc_path + file_name + file_chain + file_suffix,
            df_sep='\t',
            is_utf8=True
        )
        results.columns = [
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
            'score'
        ]
        recombine = results[[
            'contact_id_1',
            'contact_id_2',
            'score'
        ]]
        if self.__sort_ == 5:
            recombine = self.sort_3(
                recombine,
                is_sort=False,
                is_uniform=True,
                uniform_df=pd.DataFrame(pair_list),
                indicator=1,
            )
            recombine_dict = self.weqd(recombine)
            return recombine_dict
        elif self.__sort_ == 9:
            return results

    def sort_3(self, recombine, is_sort=False, is_uniform=False, uniform_df=None, indicator=0):
        uconsoo = recombine
        if is_uniform:
            predict_dict = self.weqd(uconsoo)
            uniform_df[2] = indicator
            uniform_list = uniform_df.values.tolist()
            uniform_shape = len(uniform_list)
            for i in range(uniform_shape):
                id_1 = uniform_list[i][0]
                id_2 = uniform_list[i][1]
                try:
                    uniform_list[i][2] = predict_dict[id_1][id_2]
                except KeyError:
                    continue
            uconsoo = pd.DataFrame(uniform_list)
            uconsoo.columns = [
                'contact_id_1',
                'contact_id_2',
                'score'
            ]
        uconsoo = ppssep(
            df=uconsoo,
            first='contact_id_1',
            second='contact_id_2',
            target='score',
            is_sort=is_sort
        ).extract()
        return uconsoo
