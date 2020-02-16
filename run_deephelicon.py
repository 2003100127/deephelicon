__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import os
import sys
import getopt
import subprocess
from src.Stage1_dhc_rs import stage1_dhc_rs
from src.Stage2_dhc_rs import stage2_dhc_rs
from src.Format_dhc_rs import format_dhc_rs


def usage():
    return """
    DeepHelicon: prediction of inter-helical residue contacts in transmembrane protein.

    Usage: run_deephelicon.py [-n|--name, [sequence name']] [-c|--chain, [sequence chain name]] [-i|--input, [input path]] [-o|--output, [output path]] [-h|--help] [-v|--version]

    Description
                -n, --name      Sequence name. For example, '2wsc'.
                -c, --chain     Sequence chain name. For example, '2'. This can be empty if you prefer a sequnce name like '2wsc2' or '0868'.
                -i, --input     Input path.
                -o, --output    Output path.

    for example:
    python run_deephelicon.py -n 2wsc -c 2 -i ./input/ -o ./output/

    """


def parser():
    opts, args = getopt.getopt(sys.argv[1:], '-h-n:-c:-i:-o:-v',
                               ['help', 'name=', 'chain=', 'input=', 'output=', 'version'])
    # print(opts)
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print(usage())
            sys.exit(0)
        if opt_name in ('-v', '--version'):
            print("*Version: 1.0")
        if opt_name in ('-n', '--name'):
            seq_name = opt_value
        if opt_name in ('-c', '--chain'):
            seq_chain = opt_value
        if opt_name in ('-i', '--input'):
            input = opt_value
        if opt_name in ('-o', '--output'):
            output = opt_value
        # else:
        #     print('wrong usage.')
        #     sys.exit(0)
    return seq_name, seq_chain, input, output

seq_name, seq_chain, input_path, output_path = parser()
# seq_name = '2wsc'
# seq_chain = '2'
# input_path = 'input/'
# output_path = 'output/'

print('generating features in stage 1...')
fstage1 = {
    'prot_name': seq_name,
    'file_chain': seq_chain,
    'fasta_path': input_path,
    'plmc_param_path': input_path,
    'fc_path': input_path,
    'cp_path': input_path,
    'plmc_path': input_path,
    'gdca_path': input_path,
    'sv_suffix': '.fs1',
    'sv_path': input_path,
}
stage1_dhc_rs(fstage1).generate()

print('running model in stage 1...')
s1_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Stage1_Call.py'),
    seq_name,
    seq_chain,
    input_path,
    str(4),
    input_path,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s1/s1.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s1/s1'),
    output_path,
    '.fs1',
    '.dhcs1',
]
subprocess.Popen(s1_in, shell=True).communicate()

print('No.1 generating features in stage 2...')
fstage2_i1 = {
    'prot_name': seq_name,
    'file_chain': seq_chain,
    'fasta_path': input_path,
    'dhc_path': output_path,
    'dhc_suffix': '.dhcs1',
    'sv_suffix': '.fs2i1',
    'sv_path': input_path,
}
stage2_dhc_rs(fstage2_i1).generate()

print('No.1 running model in stage 2...')
s2i1_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Stage2_Call.py'),
    seq_name,
    seq_chain,
    input_path,
    str(5),
    input_path,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i1/s2i1.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i1/s2i1'),
    output_path,
    '.fs2i1',
    '.dhcs2i1'
]
subprocess.Popen(s2i1_in, shell=True).communicate()

print('No.2 generating features in stage 2...')
fstage2_i2 = {
    'prot_name': seq_name,
    'file_chain': seq_chain,
    'fasta_path': input_path,
    'dhc_path': output_path,
    'dhc_suffix': '.dhcs2i1',
    'sv_suffix': '.fs2i2',
    'sv_path': input_path,
}
stage2_dhc_rs(fstage2_i2).generate()

print('No.2 running model in stage 2...')
s2i2_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Stage2_Call.py'),
    seq_name,
    seq_chain,
    input_path,
    str(5),
    input_path,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i2/s2i2.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i2/s2i2'),
    output_path,
    '.fs2i2',
    '.dhcs2i2'
]
subprocess.Popen(s2i2_in, shell=True).communicate()

print('No.3 generating features in stage 2...')
fstage2_i3 = {
    'prot_name': seq_name,
    'file_chain': seq_chain,
    'fasta_path': input_path,
    'dhc_path': output_path,
    'dhc_suffix': '.dhcs2i2',
    'sv_suffix': '.fs2i3',
    'sv_path': input_path,
}
stage2_dhc_rs(fstage2_i3).generate()

print('No.3 running model in stage 2...')
s2i3_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Stage2_Call.py'),
    seq_name,
    seq_chain,
    input_path,
    str(5),
    input_path,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i3/s2i3.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i3/s2i3'),
    output_path,
    '.fs2i3',
    '.dhcs2i3'
]
subprocess.Popen(s2i3_in, shell=True).communicate()

print('No.4 generating features in stage 2...')
fstage2_i4 = {
    'prot_name': seq_name,
    'file_chain': seq_chain,
    'fasta_path': input_path,
    'dhc_path': output_path,
    'dhc_suffix': '.dhcs2i3',
    'sv_suffix': '.fs2i4',
    'sv_path': input_path,
}
stage2_dhc_rs(fstage2_i4).generate()

print('No.4 running model in stage 2...')
s2i4_in = [
    "python",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Stage2_Call.py'),
    seq_name,
    seq_chain,
    input_path,
    str(5),
    input_path,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i4/s2i4.meta'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model/s2i4/s2i4'),
    output_path,
    '.fs2i4',
    '.dhcs2i4',
]
subprocess.Popen(s2i4_in, shell=True).communicate()


file_paths = {
    1: output_path,
    2: output_path,
}
file_suffixs = {
    1: '.dhcs2i3',
    2: '.dhcs2i4',
}
format_dhc_rs().do(
    prot_name=seq_name,
    file_chain=seq_chain,
    file_paths=file_paths,
    file_suffixs=file_suffixs,
    tmhmm_path=input_path,
    sv_fp=output_path,
)