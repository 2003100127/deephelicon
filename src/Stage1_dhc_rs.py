__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import numpy as np
from src.Plmc_dhc_rs import plmc_dhc_rs as cmplmc
from src.Irreflexive_dhc_rs import irreflexive_dhc_rs
from src.Pair_dhc_rs import pair_dhc_rs
from src.Fasta_dhc_rs import fasta_dhc_rs as sfasta
from src.PFasta_dhc_rs import fasta_dhc_rs as pfasta
from src.Length_dhc_rs import length_dhc_rs as plength
from src.Reader_dhc_rs import reader_dhc_rs


class stage1_dhc_rs(object):

    def __init__(self, RELEASE):
        self.RELEASE = RELEASE
        self.read = reader_dhc_rs()

    def offone(self, prot_name, file_chain, sequence, position, window_aa_ids):
        tds = [[] for _ in range(len(position))]
        ecps = cmplmc()
        tds = ecps.Jij(
            list_2d=tds,
            position=position,
            prot_name=prot_name,
            file_chain=file_chain,
            param_path=self.RELEASE['plmc_param_path'],
        )
        tds = irreflexive_dhc_rs(
            sequence=sequence,
            window_aa_ids=window_aa_ids,
            window_size=1,
        ).assign(
            list_2d=tds,
            prot_name=prot_name,
            file_chain=file_chain,
            dhc_suffix=None,
            fc_path=self.RELEASE['fc_path'],
            cp_path=self.RELEASE['cp_path'],
            plmc_path=self.RELEASE['plmc_path'],
            gdca_path=self.RELEASE['gdca_path']
        )
        return tds

    def generate(self):
        print('Protein {} chain {} starts.'.format(self.RELEASE['prot_name'], self.RELEASE['file_chain']))
        fasta_fpn = self.RELEASE['fasta_path'] + self.RELEASE['prot_name'] + self.RELEASE['file_chain'] + '.fasta'
        sequence = sfasta().getMerged(fasta_fpn)
        pos_list = plength(4).toPair(len(sequence))
        num_samples = len(pos_list)
        position = pfasta(sequence).pair(pos_list=pos_list)
        window_aa_ids = pair_dhc_rs(
            sequence=sequence,
            position=position,
            window_size=1,
        ).aaid()
        fts = self.offone(
            prot_name=self.RELEASE['prot_name'],
            file_chain=self.RELEASE['file_chain'],
            sequence=sequence,
            position=position,
            window_aa_ids=window_aa_ids
        )
        rff = np.array(fts)[:, 0: 728].astype(np.float64)
        lll = np.array(len(position) * [0]).astype(np.int64)
        ocs = np.zeros((num_samples, 2))
        ocs[np.arange(num_samples), lll] = 1
        ofd = np.concatenate((rff, ocs), axis=1)
        f = open(self.RELEASE['sv_path'] + self.RELEASE['prot_name'] + self.RELEASE['file_chain'] + self.RELEASE['sv_suffix'], 'w')
        for i in ofd:
            k = ' '.join([str(j) for j in i])
            f.write(k + "\n")
        f.close()
        return 'Features end.'