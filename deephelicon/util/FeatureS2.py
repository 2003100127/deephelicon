__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
from deephelicon.util.Pair import Pair
from deephelicon.util.PFasta import PFasta as pfasta
from deephelicon.util.Length import Length as plength
from deephelicon.util.Irreflexive import Irreflexive
from deephelicon.util.Console import Console


class FeatureS2:

    def __init__(
            self,
            params,
            verbose=True,
    ):
        self.params = params

        self.console = Console()
        self.console.verbose = verbose

    def offone(
            self,
            prot_name,
            file_chain,
            sequence,
            position,
            window_aa_ids,
            pair_list_uniform,
    ):
        tds = [[] for _ in range(len(position))]
        tds = Irreflexive(
            sequence=sequence,
            window_aa_ids=window_aa_ids,
            window_size=0,
            kind='patch',
            patch_size=7
        ).assign(
            list_2d=tds,
            prot_name=prot_name,
            file_chain=file_chain,
            dhc_suffix=self.params['dhc_suffix'],
            fc_path=None,
            cp_path=None,
            plmc_path=None,
            gdca_path=None,
            mi_path=None,
            dhc_path=self.params['dhc_fp'],
            pair_list_uniform=pair_list_uniform
        )
        return tds

    def generate(self, ):
        self.console.print('======>Features are being assembled...')
        pos_list_pair = plength(5).toPair(len(self.params['sequence']))
        pair_list_uniform = plength().toPair(len(self.params['sequence']))
        position = pfasta(self.params['sequence']).pair(pos_list=pos_list_pair)
        window_aa_ids = Pair(
            sequence=self.params['sequence'],
            position=position,
            window_size=0,
        ).aaid()
        fts = self.offone(
            prot_name=self.params['prot_name'],
            file_chain=self.params['file_chain'],
            sequence=self.params['sequence'],
            position=position,
            window_aa_ids=window_aa_ids,
            pair_list_uniform=pair_list_uniform
        )
        rff = np.array(fts)[:, 0: 441].astype(np.float64)
        ocs = np.array(len(position) * [0]).astype(np.int64)[:, np.newaxis]
        ofd = np.concatenate((rff, ocs), axis=1)
        if self.params['sv_fp']:
            f = open(self.params['sv_fp'] + self.params['prot_name'] + self.params['file_chain'] + self.params['sv_suffix'], 'w')
            for i in ofd:
                k = ' '.join([str(j) for j in i])
                f.write(k + "\n")
            f.close()
        self.console.print('======>Finished assembling features.')
        return ofd