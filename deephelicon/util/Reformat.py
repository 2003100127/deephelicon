__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import pandas as pd
from deephelicon.util.Irreflexive import Irreflexive
from deephelicon.util.TMHMM import TMHMM
from deephelicon.util.Segment import Segment
from deephelicon.util.Console import Console


class Reformat:

    def __init__(
            self,
            verbose=True,
    ):
        self.idr = Irreflexive(None, 2, [-1, -1])

        self.console = Console()
        self.console.verbose = verbose

    def run(
            self,
            prot_name,
            file_chain,
            tmhmm_fp,
            file_paths,
            file_suffixs,
            file_ids,
            sv_fp,
            format_rr='CASP14',
    ):
        self.console.print("===>Protein: {} chain: {}".format(prot_name, file_chain))
        self.console.print("======>Reformatting...")
        files = {}
        fps_l = file_paths.split(";")
        fss_l = file_suffixs.split(";")
        fids_l = file_ids.split(";")
        # for k, v in file_paths.items():
        for k, v in enumerate(fps_l):
            files[int(fids_l[k])] = self.idr.dhc(
                dhc_path=v,
                file_name=prot_name,
                file_chain=file_chain,
                file_suffix=fss_l[k],
                sort_=9
            )
        if format_rr == 'CASP14':
            annotation = files[1][[
                'contact_id_1',
                'contact_id_2',
            ]]
        else:
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
        ensemble_[0] = ensemble_[0].astype(float)
        # print(ensemble_)
        l = TMHMM().read(file_path=tmhmm_fp + prot_name + file_chain)['tl']
        u = TMHMM().read(file_path=tmhmm_fp + prot_name + file_chain)['tu']
        if len(l) >= 2:
            pos_list = Segment().toPair(l, u)
            ts = pd.DataFrame()
            asdasd = ensemble_.values.tolist()
            for tt, i in enumerate(pos_list):
                for rr, j in enumerate(asdasd):
                    if format_rr == 'CASP14':
                        if j[0] == i[0] and j[1] == i[1]:
                            ts[tt] = ensemble_.iloc[rr]
                    else:
                        if j[0] == i[0] and j[2] == i[1]:
                            ts[tt] = ensemble_.iloc[rr]
            final_ts = ts.T
            # print(final_ts)
            if format_rr == 'CASP14':
                final_ts = final_ts.sort_values(by=[0], ascending=False).reset_index(drop=True)
                final_ts[0] = final_ts[0].apply(lambda x: '{:.3f}'.format(x))
                final_ts[0] = final_ts[0].astype(float)
                final_ts[0] = final_ts[0].apply(lambda x: '{:g}'.format(x))
                final_ts[0] = final_ts[0].apply(lambda x: x.replace('0.', '.'))
                final_ts['contact_id_1'] = final_ts['contact_id_1'].astype(int)
                final_ts['contact_id_2'] = final_ts['contact_id_2'].astype(int)
                final_ts.to_csv(
                    sv_fp + prot_name + file_chain + '.deephelicon',
                    sep=' ',
                    header=False,
                    index=False,
                )
            else:
                final_ts.to_csv(
                    sv_fp + prot_name + file_chain + '.deephelicon',
                    sep='\t',
                    header=False,
                    index=False,
                )
            return final_ts
        else:
            ensemble_.to_csv(
                sv_fp + prot_name + file_chain + '.deephelicon',
                sep='\t',
                header=False,
                index=False,
            )
            return ensemble_