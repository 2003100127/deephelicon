__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
import numpy as np
from src.Irreflexive_dhc_rs import irreflexive_dhc_rs
from src.Pair_dhc_rs import pair_dhc_rs
from src.Fasta_dhc_rs import fasta_dhc_rs as sfasta
from src.PFasta_dhc_rs import fasta_dhc_rs as pfasta
from src.Length_dhc_rs import length_dhc_rs as plength
from src.Reader_dhc_rs import reader_dhc_rs


class stage2_dhc_rs(object):

    def __init__(self, RELEASE):
        self.RELEASE = RELEASE
        self.read = reader_dhc_rs()

    def offone(self, prot_name, file_chain, sequence, position, window_aa_ids, pair_list_uniform):
        tds = [[] for _ in range(len(position))]
        tds = irreflexive_dhc_rs(
            sequence=sequence,
            window_aa_ids=window_aa_ids,
            window_size=0,
            kind='patch',
            patch_size=7
        ).assign(
            list_2d=tds,
            prot_name=prot_name,
            file_chain=file_chain,
            dhc_suffix=self.RELEASE['dhc_suffix'],
            fc_path=None,
            cp_path=None,
            plmc_path=None,
            gdca_path=None,
            mi_path=None,
            dhc_path=self.RELEASE['dhc_path'],
            pair_list_uniform=pair_list_uniform
        )
        return tds

    def generate(self):
        print('Protein {} chain {} starts.'.format(self.RELEASE['prot_name'], self.RELEASE['file_chain']))
        sequence = sfasta().get(
            fasta_path=self.RELEASE['fasta_path'],
            fasta_name=self.RELEASE['prot_name'],
            file_chain=self.RELEASE['file_chain']
        )
        pos_list_pair = plength(5).toPair(len(sequence))
        pair_list_uniform = plength().toPair(len(sequence))
        position = pfasta(sequence).pair(pos_list=pos_list_pair)
        window_aa_ids = pair_dhc_rs(
            sequence=sequence,
            position=position,
            window_size=0,
        ).aaid()
        fts = self.offone(
            prot_name=self.RELEASE['prot_name'],
            file_chain=self.RELEASE['file_chain'],
            sequence=sequence,
            position=position,
            window_aa_ids=window_aa_ids,
            pair_list_uniform=pair_list_uniform
        )
        rff = np.array(fts)[:, 0: 441].astype(np.float64)
        ocs = np.array(len(position) * [0]).astype(np.int64)[:, np.newaxis]
        ofd = np.concatenate((rff, ocs), axis=1)
        f = open(self.RELEASE['sv_path'] + self.RELEASE['prot_name'] + self.RELEASE['file_chain'] + self.RELEASE['sv_suffix'], 'w')
        for i in ofd:
            k = ' '.join([str(j) for j in i])
            f.write(k + "\n")
        f.close()
        return 'Features end.'