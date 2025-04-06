__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
from deephelicon.util.Plmc import Plmc as cmplmc
from deephelicon.util.Irreflexive import Irreflexive
from deephelicon.util.PFasta import PFasta as pfasta
from deephelicon.util.Length import Length as plength
from deephelicon.util.Pair import Pair
from deephelicon.util.Console import Console


class FeatureS1:

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
    ):
        tds = [[] for _ in range(len(position))]
        ecps = cmplmc()
        tds = ecps.Jij(
            list_2d=tds,
            position=position,
            prot_name=prot_name,
            file_chain=file_chain,
            param_path=self.params['plmc_param_fp'],
        )
        tds = Irreflexive(
            sequence=sequence,
            window_aa_ids=window_aa_ids,
            window_size=1,
        ).assign(
            list_2d=tds,
            prot_name=prot_name,
            file_chain=file_chain,
            dhc_suffix=None,
            fc_path=self.params['fc_fp'],
            cp_path=self.params['cp_fp'],
            plmc_path=self.params['plmc_fp'],
            gdca_path=self.params['gdca_fp']
        )
        return tds

    def generate(self):
        self.console.print('======>Features are being assembled...')
        pos_list = plength(4).toPair(len(self.params['sequence']))
        num_samples = len(pos_list)
        position = pfasta(self.params['sequence']).pair(pos_list=pos_list)
        window_aa_ids = Pair(
            sequence=self.params['sequence'],
            position=position,
            window_size=1,
        ).aaid()
        fts = self.offone(
            prot_name=self.params['prot_name'],
            file_chain=self.params['file_chain'],
            sequence=self.params['sequence'],
            position=position,
            window_aa_ids=window_aa_ids
        )
        rff = np.array(fts)[:, 0: 728].astype(np.float64)
        lll = np.array(len(position) * [0]).astype(np.int64)
        ocs = np.zeros((num_samples, 2))
        ocs[np.arange(num_samples), lll] = 1
        ofd = np.concatenate((rff, ocs), axis=1)
        if self.params['sv_fp']:
            f = open(self.params['sv_fp'] + self.params['prot_name'] + self.params['file_chain'] + self.params['sv_suffix'], 'w')
            for i in ofd:
                k = ' '.join([str(j) for j in i])
                f.write(k + "\n")
            f.close()
        self.console.print('======>Finished assembling features.')
        return ofd