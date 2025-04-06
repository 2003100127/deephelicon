__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from Bio import SeqIO


class Fasta:

    def get(self, fasta_fpn):
        sequence = []
        for seq in SeqIO.parse(fasta_fpn, "fasta"):
            sequence.append(str(seq.seq))
        sequence = ''.join(sequence)
        if sequence == '':
            print('The sequence is empty.')
        return sequence