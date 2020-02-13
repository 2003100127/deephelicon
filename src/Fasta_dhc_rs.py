__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
sys.path.append('../')
from Bio import SeqIO
from src.Reader_dhc_rs import reader_dhc_rs


class fasta_dhc_rs(object):

    def __init__(self):
        self.read = reader_dhc_rs()

    def get(self, fasta_path, fasta_name, file_chain):
        sequence = []
        for seq in SeqIO.parse(fasta_path + fasta_name + file_chain + '.fasta', "fasta"):
            # print(seq.seq)
            sequence.append(str(seq.seq))
        sequence = ''.join(sequence)
        if sequence == '':
            print('The sequence is empty.')
        return sequence

    def getMerged(self, fasta_fpn):
        sequence = []
        for seq in SeqIO.parse(fasta_fpn, "fasta"):
            sequence.append(str(seq.seq))
        sequence = ''.join(sequence)
        if sequence == '':
            print('The sequence is empty.')
        return sequence