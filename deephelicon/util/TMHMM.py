__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import re
import linecache


class TMHMM:

    def read(self, file_path):
        arr = self.format(file_path)
        lpsnp = len(arr)
        tl, tu = [], []
        cl, cu = [], []
        el, eu = [], []
        rl, ru = [], []
        for i in range(lpsnp):
            if arr[i][0] == 'M':
                tl.append(arr[i][1])
                tu.append(arr[i][2])
            elif arr[i][0] == 'i':
                cl.append(arr[i][1])
                cu.append(arr[i][2])
            elif arr[i][0] == 'o':
                el.append(arr[i][1])
                eu.append(arr[i][2])
            else:
                rl.append(arr[i][1])
                ru.append(arr[i][2])
        tmhmm_dict = {
            'cl': cl,
            'cu': cu,
            'tl': tl,
            'tu': tu,
            'el': el,
            'eu': eu,
            'rl': rl,
            'ru': ru,
        }
        return tmhmm_dict

    @classmethod
    def format(cls, file_path):
        line = linecache.getline(file_path + '.tmhmm', 1)
        block1 = re.split(r': ', line)
        block2 = block1[1].split(', ')
        lpsnp = len(block2)
        arr = []
        for i in range(lpsnp):
            tag = block2[i].split(' ')[0]
            beg = block2[i].split(' ')[1]
            end = block2[i].split(' ')[2]
            arr.append([tag, int(beg), int(end)])
        return arr