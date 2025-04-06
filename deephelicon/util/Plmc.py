__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from itertools import chain
from deephelicon.util.EVCouplingsModel import CouplingsModel

class Plmc:

    def Jij(self, list_2d, position, prot_name, file_chain, param_path):
        pos_ = position
        ec = CouplingsModel(filename=param_path + prot_name + file_chain + '.params')
        abuytts = len(ec.alphabet)
        l0odh = list_2d
        num_pairs = len(pos_)
        for i in range(num_pairs):
            iiuyyy = list(chain.from_iterable(ec.Jij(pos_[i][0], pos_[i][3])))
            for j in range(abuytts * abuytts):
                l0odh[i].append(iiuyyy[j])
        return l0odh