__author__ = "Jianfeng Sun"
__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL-3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import click
import urllib.request
from pyfiglet import Figlet
import numpy as np
import pandas as pd
from deephelicon import load
from deephelicon.util.Fasta import Fasta as sfasta
from deephelicon.util.PFasta import PFasta as pfasta
from deephelicon.util.Length import Length as sclength
from deephelicon.util.DataInitializer import DataInitializer
from deephelicon.util.FeatureS1 import FeatureS1
from deephelicon.util.FeatureS2 import FeatureS2
from deephelicon.util.Console import Console


vignette1 = Figlet(font='standard')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(short_help=vignette1.renderText('DeepHelicon'), context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--url', default='https://github.com/2003100127/deephelicon/releases/download/model/model.zip', help='URL of deephelicon models')
@click.option('-o', '--sv_fpn', default='./model.zip', help='output path of deephelicon models')
def download(url, sv_fpn):
    download_data(url, sv_fpn)


def download_data(
        url,
        sv_fpn,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('DeepHelicon'))
    console.print('=>Downloading starts...')
    urllib.request.urlretrieve(
        url=url,
        filename=sv_fpn
    )
    console.print('=>downloaded.')
    return 'downloaded.'


class HelpfulCmd(click.Command):
    def format_help(self, ctx, formatter):
        click.echo(vignette1.renderText('DeepHelicon'))
        click.echo(
            '''
            Options:
            -pn, --prot_name              Protein name identifier (e.g., "5w1h")
            -pc, --prot_chain             Protein chain identifier (e.g., "A")
            -fa, --fasta_fp               Path to the FASTA file containing the protein sequence
            -fcfp, --fc_fp                Path to the FreeContact feature file
            -gdcafp, --gdca_fp            Path to the Gaussian DCA feature file
            -cpfp, --cp_fp                Path to the CCMPred feature file
            -plmcfp, --plmc_fp            Path to the PLMC coupling score file
            -plmcparamfp, --plmc_param_fp Path to the PLMC parameter file
            -sv_fp_f, --sv_fp_feature     Path to save the generated input features for the model (default: ./)
            -sv_suf_f, --sv_suffix_feature    Suffix name for the saved feature file (e.g., ".fs1", default: .fs1)
            -m, --model_frozen_fpn        Path to the frozen model (.pb) file for prediction
            -sv_fp_p, --sv_fp_pred        Path to save the model prediction outputs (default: ./)
            -sv_suf_p, --sv_suffix_pred   Suffix name for the saved prediction file (e.g., ".s1", default: .s1)
            -ss_inf, --seq_sep_inferior   Sequence separation inferior limit (default: 4)
            -bs, --batch_size             Batch size used during prediction (default: 100)
            -vb, --verbose                Whether to print detailed logs during processing (default: True)
            '''
        )


@click.command(cls=HelpfulCmd, context_settings=CONTEXT_SETTINGS)
@click.option('-pn', '--prot_name', required=True, help='Protein name identifier (e.g., "5w1h")')
@click.option('-pc', '--prot_chain', required=True, help='Protein chain identifier (e.g., "A")')
@click.option('-fa', '--fasta_fp', required=True, help='Path to the FASTA file containing the protein sequence')
@click.option('-fcfp', '--fc_fp', required=True, help='Path to the freecontact feature file')
@click.option('-gdcafp', '--gdca_fp', required=True, help='Path to the Gaussion DCA feature file')
@click.option('-cpfp', '--cp_fp', required=True, help='Path to the CCMPred feature file')
@click.option('-plmcfp', '--plmc_fp', required=True, help='Path to the PLMC coupling score file')
@click.option('-plmcparamfp', '--plmc_param_fp', required=True, help='Path to the PLMC parameter file')
@click.option('-sv_fp_f', '--sv_fp_feature', default='./', help='Path to save the generated input features for the model')
@click.option('-sv_suf_f', '--sv_suffix_feature', default='.fs1', help='Suffix name for the saved feature file (e.g., ".fs1")')
@click.option('-m', '--model_frozen_fpn', required=True, help='Path to the frozen model (.pb) file for prediction')
@click.option('-sv_fp_p', '--sv_fp_pred', default='./', help='Path to save the model prediction outputs')
@click.option('-sv_suf_p', '--sv_suffix_pred', default='.s1', help='Suffix name for the saved prediction file (e.g., "_pred.csv")')
@click.option('-ss_inf', '--seq_sep_inferior', default=4, help='sequence separation inferior')
@click.option('-bs', '--batch_size', default=100, help='Batch size used during prediction')
@click.option('-vb', '--verbose', default=True, help='Whether to print detailed logs during processing (default: True)')
def rrc_s1(
        prot_name,
        prot_chain,
        fasta_fp,
        fc_fp,
        gdca_fp,
        cp_fp,
        plmc_fp,
        plmc_param_fp,
        sv_fp_feature,
        sv_suffix_feature,
        model_frozen_fpn,
        sv_fp_pred,
        sv_suffix_pred,
        seq_sep_inferior,
        batch_size,
        verbose,
):
    return rrcontact_stage1(
        prot_name=prot_name,
        prot_chain=prot_chain,
        fasta_fp=fasta_fp,
        fc_fp=fc_fp,
        gdca_fp=gdca_fp,
        cp_fp=cp_fp,
        plmc_fp=plmc_fp,
        plmc_param_fp=plmc_param_fp,
        sv_fp_feature=sv_fp_feature,
        sv_suffix_feature=sv_suffix_feature,
        model_frozen_fpn=model_frozen_fpn,
        sv_fp_pred=sv_fp_pred,
        sv_suffix_pred=sv_suffix_pred,
        seq_sep_inferior=seq_sep_inferior,
        batch_size=batch_size,
        verbose=verbose,
)


def rrcontact_stage1(
        prot_name,
        prot_chain,
        fasta_fp,
        fc_fp,
        gdca_fp,
        cp_fp,
        plmc_fp,
        plmc_param_fp,
        sv_fp_feature,
        sv_suffix_feature,
        model_frozen_fpn,
        sv_fp_pred,
        sv_suffix_pred,
        seq_sep_inferior=5,
        batch_size=100,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('DeepHelicon'))

    console.print("===>Protein: {} chain: {}".format(prot_name, prot_chain))

    sequence = sfasta().get(fasta_fpn=fasta_fp + prot_name + prot_chain + '.fasta')

    mat_np = FeatureS1(params={
        'prot_name': prot_name,
        'file_chain': prot_chain,
        'sequence': sequence,
        'fc_fp': fc_fp,
        'gdca_fp': gdca_fp,
        'plmc_fp': plmc_fp,
        'cp_fp': cp_fp,
        'plmc_param_fp': plmc_param_fp,
        'sv_fp': sv_fp_feature,
        'sv_suffix': sv_suffix_feature,
    }).generate()
    # print(mat_np)
    x_test, _, num_test_samples = DataInitializer().input2d(
        mat_np,
        bound_inf=728,
        bound_sup=728,
    )

    import tensorflow as tf
    console.print("===>The model ({}) with frozen graphs converted from tensorflow 1.15.2 is being read...".format(model_frozen_fpn))
    graph = load.frozen_graph(model_frozen_fpn)
    x_tf = graph.get_tensor_by_name("x:0")
    pred_tf = graph.get_tensor_by_name("softmax:0")
    console.print("===>The model is read in, with\ninput: {}\noutput: {}".format(x_tf, pred_tf))
    sess = tf.compat.v1.Session(graph=graph)

    accumulator = []

    num_batch_test = num_test_samples // batch_size
    final_number = num_test_samples % batch_size
    for batch in range(num_batch_test + 1):
        if batch < num_batch_test:
            x_batch_te, _ = DataInitializer().batchData(
                x_test, _, batch, batch_size
            )
        else:
            x_batch_te = x_test[batch * batch_size: (batch * batch_size + final_number), :]
        feed_dict_test = {x_tf: x_batch_te}
        pred_tmp = sess.run(pred_tf, feed_dict=feed_dict_test)
        accumulator.append(pred_tmp)

    pos_list = sclength(seq_sep_inferior).toPair(len(sequence))
    position = pfasta(sequence).pair(pos_list=pos_list)
    res = np.array(position)[:, [0, 1, 3, 4]]
    pred_data = accumulator[0]
    for i in range(1, len(accumulator)):
        pred_data = np.concatenate((pred_data, accumulator[i]), axis=0)
    pred_data = np.concatenate((res, pred_data[:, [1]]), axis=1)

    df = pd.DataFrame(pred_data)
    console.print("======>Predicted probabilities of residue-residue contacts:\n{}".format(df))
    if sv_fp_pred:
        sv_fpn_pred = sv_fp_pred + prot_name + prot_chain + sv_suffix_pred
        df.to_csv(
            sv_fpn_pred,
            sep='\t',
            header=False,
            index=False
        )
        console.print("======>Predictions are saved to {}".format(sv_fpn_pred))
    return df


class HelpfulCmd2(click.Command):
    def format_help(self, ctx, formatter):
        click.echo(vignette1.renderText('DeepHelicon'))
        click.echo(
            '''
            Options:
            -pn, --prot_name              Protein name identifier (e.g., "5w1h")
            -pc, --prot_chain             Protein chain identifier (e.g., "A")
            -fa, --fasta_fp               Path to the FASTA file containing the protein sequence
            -dhcfp, --dhc_fp              Path to save a residue-residue contact file
            -dhc_suf, --dhc_suffix        Suffix name for the saved residue-residue contact prediction file
                                        (e.g., ".s1" or ".s2i1")
            -sv_fp_f, --sv_fp_feature     Path to save the generated structural feature file for the model
                                        (default: "./")
            -sv_suf_f, --sv_suffix_feature
                                        Suffix name for the saved structural feature file
                                        (e.g., ".s2i2", default: ".fs2i1")
            -m, --model_frozen_fpn        Path to the frozen model (.pb file) used for prediction
            -sv_fp_p, --sv_fp_pred        Path to save the model prediction output (default: "./")
            -sv_suf_p, --sv_suffix_pred   Suffix name for the saved prediction file
                                        (e.g., "_pred.csv", default: ".s2i1")
            -ss_inf, --seq_sep_inferior   Inferior threshold for sequence separation filtering
                                        (residue pairs partitioned less than this number will be ignored, default: 5)
            -bs, --batch_size             Batch size used during model inference (default: 100)
            -vb, --verbose                Whether to print detailed logs during processing (default: True)
            '''
        )


@click.command(cls=HelpfulCmd2, context_settings=CONTEXT_SETTINGS)
@click.option('-pn', '--prot_name', required=True, help='Protein name identifier (e.g., "5w1h")')
@click.option('-pc', '--prot_chain', required=True, help='Protein chain identifier (e.g., "A")')
@click.option('-fa', '--fasta_fp', required=True, help='Path to the FASTA file containing the protein sequence')
@click.option('-dhcfp', '--dhc_fp', required=True, help='Path to save a residue-residue contact file')
@click.option('-dhc_suf', '--dhc_suffix', required=True, help='Suffix name for the saved residue-residue contact prediction file (e.g., ".s1" or ".s2i1")')
@click.option('-sv_fp_f', '--sv_fp_feature', default='./', help='Path to save the generated structural feature file for the model')
@click.option('-sv_suf_f', '--sv_suffix_feature', default='.fs2i1', help='Suffix name for the saved structural feature file (e.g., ".s2i2")')
@click.option('-m', '--model_frozen_fpn', required=True, help='Path to the frozen model (.pb file) used for prediction')
@click.option('-sv_fp_p', '--sv_fp_pred', default='./', help='Path to save the model prediction output')
@click.option('-sv_suf_p', '--sv_suffix_pred', default='.s2i1', help='Suffix name for the saved prediction file (e.g., "_pred.csv")')
@click.option('-ss_inf', '--seq_sep_inferior', default=5, help='Inferior threshold for sequence separation filtering (e.g., residue pairs partitioned less than this number will be ignored)')
@click.option('-bs', '--batch_size', default=100, help='Batch size used during model inference')
@click.option('-vb', '--verbose', default=True, help='Whether to print detailed logs during processing (default: True)')
def rrc_s2(
        prot_name,
        prot_chain,
        fasta_fp,
        dhc_fp,
        dhc_suffix,
        sv_fp_feature,
        sv_suffix_feature,
        model_frozen_fpn,
        sv_fp_pred,
        sv_suffix_pred,
        seq_sep_inferior,
        batch_size,
        verbose,
):
    return rrcontact_stage2(
        prot_name=prot_name,
        prot_chain=prot_chain,
        fasta_fp=fasta_fp,
        dhc_fp=dhc_fp,
        dhc_suffix=dhc_suffix,
        sv_fp_feature=sv_fp_feature,
        sv_suffix_feature=sv_suffix_feature,
        model_frozen_fpn=model_frozen_fpn,
        sv_fp_pred=sv_fp_pred,
        sv_suffix_pred=sv_suffix_pred,
        seq_sep_inferior=seq_sep_inferior,
        batch_size=batch_size,
        verbose=verbose,
    )


def rrcontact_stage2(
        prot_name,
        prot_chain,
        fasta_fp,
        dhc_fp,
        dhc_suffix,

        sv_fp_feature,
        sv_suffix_feature,

        model_frozen_fpn,

        sv_fp_pred,
        sv_suffix_pred,

        seq_sep_inferior,
        batch_size=100,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('DeepHelicon'))

    console.print("===>Protein: {} chain: {}".format(prot_name, prot_chain))

    sequence = sfasta().get(fasta_fpn=fasta_fp + prot_name + prot_chain + '.fasta')

    mat_np = FeatureS2(params={
        'prot_name': prot_name,
        'file_chain': prot_chain,
        'sequence': sequence,
        'dhc_fp': dhc_fp,
        'dhc_suffix': dhc_suffix,
        'sv_fp': sv_fp_feature,
        'sv_suffix': sv_suffix_feature,
    }).generate()
    # print(mat_np)
    x_test, _, num_test_samples = DataInitializer().input2d(
        mat_np,
        bound_inf=225,
        bound_sup=225,
    )

    import tensorflow as tf
    console.print("===>The model ({}) with frozen graphs converted from tensorflow 1.15.2 is being read...".format(model_frozen_fpn))
    graph = load.frozen_graph(model_frozen_fpn)
    x_tf = graph.get_tensor_by_name("x_1:0")
    pred_tf = graph.get_tensor_by_name("sigmoid:0")
    console.print("===>The model is read in, with\ninput: {}\noutput: {}".format(x_tf, pred_tf))
    sess = tf.compat.v1.Session(graph=graph)

    accumulator = []
    num_batch_test = num_test_samples // batch_size
    final_number = num_test_samples % batch_size
    for batch in range(num_batch_test + 1):
        if batch < num_batch_test:
            x_batch_te, _ = DataInitializer().batchData(
                x_test, _, batch, batch_size
            )
        else:
            x_batch_te = x_test[batch * batch_size: (batch * batch_size + final_number), :]
        feed_dict_test = {x_tf: x_batch_te}
        pred_tmp = sess.run(pred_tf, feed_dict=feed_dict_test)
        accumulator.append(pred_tmp)
    pos_list = sclength(int(seq_sep_inferior)).toPair(len(sequence))
    position = pfasta(sequence).pair(pos_list=pos_list)
    res = np.array(position)[:, [0, 1, 3, 4]]
    pred_data = accumulator[0]
    for i in range(1, len(accumulator)):
        pred_data = np.concatenate((pred_data, accumulator[i]), axis=0)
    pred_data = np.concatenate((res, pred_data[:, [0]]), axis=1)
    df = pd.DataFrame(pred_data)
    console.print("======>Predicted probabilities of residue-residue contacts:\n{}".format(df))
    if sv_fp_pred:
        sv_fpn_pred = sv_fp_pred + prot_name + prot_chain + sv_suffix_pred
        df.to_csv(
            sv_fpn_pred,
            sep='\t',
            header=False,
            index=False
        )
        console.print("======>Predictions are saved to {}".format(sv_fpn_pred))
    return df


class HelpfulCmdr(click.Command):
    def format_help(self, ctx, formatter):
        click.echo(vignette1.renderText('DeepHelicon'))
        click.echo(
            '''
            Options:
            -pn, --prot_name    Protein name identifier (e.g., "5w1h")
            -pc, --prot_chain   Protein chain identifier (e.g., "A")
            -fps, --file_paths  Python dict of input file paths. The files are produced by DeepHelicon at stage 1 and stage 2.
            -fss, --file_suffixs    Python dict of corresponding suffixes for each of the input files (file_paths)
            -fids, --file_ids   IDs of input files
            -tmhmm, --tmhmm_fp  Path to the TMHMM prediction file for transmembrane region annotation
            -sv_fp, --sv_fp Path to save the merged or processed feature file (e.g., .s1, s2i1, s2i2, etc.) (default: ./)
            -fmt, --format_rr   Format of the output file for residue-residue contact predictions. The default is "Normal", but "CASP14" is also supported.
            -vb, --verbose  Whether to print detailed logs during processing (default: True)
            '''
        )


@click.command(cls=HelpfulCmdr, context_settings=CONTEXT_SETTINGS)
@click.option('-pn', '--prot_name', required=True, help='Protein name identifier (e.g., "5w1h")')
@click.option('-pc', '--prot_chain', required=True, help='Protein chain identifier (e.g., "A")')
@click.option('-fps', '--file_paths', required=True, help='Python dict of input file paths. The files are producted by DeepHelicon at stage 1 and stage 2.')
@click.option('-fss', '--file_suffixs', required=True, help='Python dict of corresponding suffixes for each of the input files (file_paths)')
@click.option('-fids', '--file_ids', required=True, help='IDs of input files')
@click.option('-tmhmm', '--tmhmm_fp', required=True, help='Path to the TMHMM prediction file for transmembrane region annotation')
@click.option('-sv_fp', '--sv_fp', default='./', help='Path to save the merged or processed feature file (e.g., .s1, s2i1, s2i2, etc.)')
@click.option('-fmt', '--format_rr', default='Normal', help='Format of the output file for residue-residue contact predictions. The default option is Normal but it can be CASP14.')
@click.option('-vb', '--verbose', default=True, help='Whether to print detailed logs during processing (default: True)')
def op_format(
        prot_name,
        prot_chain,
        file_paths,
        file_suffixs,
        file_ids,
        tmhmm_fp,
        sv_fp,
        format_rr,
        verbose,
):
    return reformat(
        prot_name=prot_name,
        prot_chain=prot_chain,
        file_paths=file_paths,
        file_suffixs=file_suffixs,
        file_ids=file_ids,
        tmhmm_fp=tmhmm_fp,
        sv_fp=sv_fp,
        format_rr=format_rr,
        verbose=verbose,
    )


def reformat(
        prot_name,
        prot_chain,
        file_paths,
        file_suffixs,
        file_ids,
        tmhmm_fp,
        sv_fp,
        format_rr,
        verbose=True,
):
    console = Console()
    console.verbose = verbose
    print(vignette1.renderText('DeepHelicon'))

    from deephelicon.util.Reformat import Reformat
    df = Reformat().run(
        prot_name=prot_name,
        file_chain=prot_chain,
        file_paths=file_paths,
        file_suffixs=file_suffixs,
        file_ids=file_ids,
        tmhmm_fp=tmhmm_fp,
        sv_fp=sv_fp,
        format_rr=format_rr,
    )
    console.print("dataframe: \n{}".format(df))
    return df


if __name__ == "__main__":
    # params_s1 = {
    #     'prot_name': '2wsc',
    #     'prot_chain': '2',
    #     'fasta_fp': '../data/input/',
    #     'fc_fp': '../data/input/',
    #     'gdca_fp': '../data/input/',
    #     'cp_fp': '../data/input/',
    #     'plmc_fp': '../data/input/',
    #     'plmc_param_fp': '../data/input/',
    #     'sv_fp_feature': '../data/',
    #     'sv_suffix_feature': '.fs1',
    #
    #     'model_frozen_fpn': '../data/model/frozen_graph/s1.pb',
    #     'batch_size': 100,
    #     'seq_sep_inferior': 4,
    #     'sv_fp_pred': '../data/output/test/',
    #     'sv_suffix_pred': '.s1',
    # }
    # rrcontact_stage1(
    #     prot_name=params_s1['prot_name'],
    #     prot_chain=params_s1['prot_chain'],
    #     fasta_fp=params_s1['fasta_fp'],
    #     fc_fp=params_s1['fc_fp'],
    #     gdca_fp=params_s1['gdca_fp'],
    #     cp_fp=params_s1['cp_fp'],
    #     plmc_fp=params_s1['plmc_fp'],
    #     plmc_param_fp=params_s1['plmc_param_fp'],
    #     sv_fp_feature=params_s1['sv_fp_feature'],
    #     sv_suffix_feature=params_s1['sv_suffix_feature'],
    #     model_frozen_fpn=params_s1['model_frozen_fpn'],
    #     sv_fp_pred=params_s1['sv_fp_pred'],
    #     sv_suffix_pred=params_s1['sv_suffix_pred'],
    #     seq_sep_inferior=params_s1['seq_sep_inferior'],
    #     batch_size=100,
    #     verbose=True,
    # )

    # params_s2i1 = {
    #     'prot_name': '2wsc',
    #     'prot_chain': '2',
    #     'fasta_fp': '../data/input/',
    #     'dhc_fp': '../data/',
    #     'dhc_suffix': '.s1',
    #     'sv_fp_feature': '../data/',
    #     'sv_suffix_feature': '.fs2i1',
    #
    #     'model_frozen_fpn': '../data/model/frozen_graph/s2i1.pb',
    #     'batch_size': 100,
    #     'seq_sep_inferior': 5,
    #     'sv_fp_pred': '../data/',
    #     'sv_suffix_pred': '.s2i1',
    # }
    # rrcontact_stage2(
    #     prot_name=params_s2i1['prot_name'],
    #     prot_chain=params_s2i1['prot_chain'],
    #     fasta_fp=params_s2i1['fasta_fp'],
    #     dhc_fp=params_s2i1['dhc_fp'],
    #     dhc_suffix=params_s2i1['dhc_suffix'],
    #     sv_fp_feature=params_s2i1['sv_fp_feature'],
    #     sv_suffix_feature=params_s2i1['sv_suffix_feature'],
    #     model_frozen_fpn=params_s2i1['model_frozen_fpn'],
    #     sv_fp_pred=params_s2i1['sv_fp_pred'],
    #     sv_suffix_pred=params_s2i1['sv_suffix_pred'],
    #     seq_sep_inferior=params_s2i1['seq_sep_inferior'],
    #     batch_size=100,
    #     verbose=True,
    # )

    # params_s2i2 = {
    #     'prot_name': '2wsc',
    #     'prot_chain': '2',
    #     'fasta_fp': '../data/input/',
    #     'dhc_fp': '../data/',
    #     'dhc_suffix': '.s2i1',
    #     'sv_fp_feature': '../data/',
    #     'sv_suffix_feature': '.fs2i2',
    #
    #     'model_frozen_fpn': '../data/model/frozen_graph/s2i2.pb',
    #     'batch_size': 100,
    #     'seq_sep_inferior': 5,
    #     'sv_fp_pred': '../data/',
    #     'sv_suffix_pred': '.s2i2',
    # }
    # rrcontact_stage2(params=params_s2i2)

    # params_s2i3 = {
    #     'prot_name': '2wsc',
    #     'prot_chain': '2',
    #     'fasta_fp': '../data/input/',
    #     'dhc_fp': '../data/',
    #     'dhc_suffix': '.s2i2',
    #     'sv_fp_feature': '../data/',
    #     'sv_suffix_feature': '.fs2i3',
    #
    #     'model_frozen_fpn': '../data/model/frozen_graph/s2i3.pb',
    #     'batch_size': 100,
    #     'seq_sep_inferior': 5,
    #     'sv_fp_pred': '../data/',
    #     'sv_suffix_pred': '.s2i3',
    # }
    # rrcontact_stage2(params=params_s2i3)

    # params_s2i4 = {
    #     'prot_name': '2wsc',
    #     'prot_chain': '2',
    #     'fasta_fp': '../data/input/',
    #     'dhc_fp': '../data/',
    #     'dhc_suffix': '.s2i3',
    #     'sv_fp_feature': '../data/',
    #     'sv_suffix_feature': '.fs2i4',
    #
    #     'model_frozen_fpn': '../data/model/frozen_graph/s2i4.pb',
    #     'batch_size': 100,
    #     'seq_sep_inferior': 5,
    #     'sv_fp_pred': '../data/',
    #     'sv_suffix_pred': '.s2i4',
    # }
    # rrcontact_stage2(params=params_s2i4)

    params_reformat = {
        'prot_name': '2wsc',
        'prot_chain': '2',
        'file_paths': {
            1: '../data/',
            2: '../data/',
        },
            'file_suffixs': {
            1: '.s2i3',
            2: '.s2i4',
        },
        'tmhmm_fp': '../data/input/',
        'sv_fp': '../data/',
        'format_rr': 'CASP14',
    }
    reformat(
        prot_name=params_reformat['prot_name'],
        prot_chain=params_reformat['prot_chain'],
        file_paths=params_reformat['file_paths'],
        file_suffixs=params_reformat['file_suffixs'],
        tmhmm_fp=params_reformat['tmhmm_fp'],
        sv_fp=params_reformat['sv_fp'],
        format_rr=params_reformat['format_rr'],
    )