__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import pandas as pd
from src.Reader_dhc_rs import reader_dhc_rs
from src.Irreflexive_dhc_rs import irreflexive_dhc_rs
from src.TMHMM_dhc_rs import tmhmm_dhc_rs
from src.Segment_dhc_rs import segment_dhc_rs


class format_dhc_rs(object):

    def __init__(self):
        self.pfreader = reader_dhc_rs()
        self.idr = irreflexive_dhc_rs(None, 2, [-1, -1])

    def do(self, prot_name, file_chain, file_suffixs, tmhmm_path, file_paths, sv_fp):
        print('{} {}'.format(prot_name, file_chain))
        files = {}
        for k, v in file_paths.items():
            files[k] = self.idr.dhc(
                dhc_path=v,
                file_name=prot_name,
                file_chain=file_chain,
                file_suffix=file_suffixs[k],
                sort_=9
            )
        annotation = files[1][[
            'contact_id_1',
            'aa_1',
            'contact_id_2',
            'aa_2',
        ]]
        for k, each in files.items():
            files[k] = each.rename(columns={'score': 'score' + str(k)})
        each_combine = pd.concat(
            [each['score' + str(u)] for u, each in files.items()],
            axis=1
        )
        mean_each = 0.6 * each_combine['score1'] + 0.4 * each_combine['score2']
        # mean_each = each_combine.mean(axis=1)
        ensemble_ = pd.concat([annotation, mean_each], axis=1)
        l = tmhmm_dhc_rs().read(file_path=tmhmm_path + prot_name + file_chain)['tl']
        u = tmhmm_dhc_rs().read(file_path=tmhmm_path + prot_name + file_chain)['tu']
        if len(l) >= 2:
            pos_list = segment_dhc_rs().toPair(l, u)
            ts = pd.DataFrame()
            asdasd = ensemble_.values.tolist()
            for tt, i in enumerate(pos_list):
                for rr, j in enumerate(asdasd):
                    if j[0] == i[0] and j[2] == i[1]:
                        ts[tt] = ensemble_.iloc[rr]
            ts.T.to_csv(sv_fp + prot_name + file_chain + '.deephelicon', sep='\t', header=None, index=False)
        else:
            ensemble_.to_csv(sv_fp + prot_name + file_chain + '.deephelicon', sep='\t', header=None, index=False)
        return 'Prediction finishes.'