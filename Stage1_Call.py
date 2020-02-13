__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import numpy as np
import pandas as pd
import tensorflow as tf
# sys.path.append('./')
from src.Fasta_dhc_rs import fasta_dhc_rs as sfasta
from src.PFasta_dhc_rs import fasta_dhc_rs as pfasta
from src.Length_dhc_rs import length_dhc_rs as sclength
from src.DataInitializer_dhc_rs import dataInitializer_dhc_rs


def stage2_Graph_Call():
    batch_size = 100
    sess = tf.Session()
    saver = tf.train.import_meta_graph(sys.argv[6])
    saver.restore(sess, sys.argv[7])
    tf_graph = tf.get_default_graph()
    x = tf_graph.get_tensor_by_name("x:0")
    prediction = tf_graph.get_tensor_by_name("softmax:0")
    print(
        "Protein: {}".format(sys.argv[1] + sys.argv[2])
    )
    accumulator = []
    x_test, _, num_test_samples = dataInitializer_dhc_rs().input2d(
        sys.argv[5] + sys.argv[1] + sys.argv[2] + sys.argv[9],
        bound_inf=728,
        bound_sup=728,
        sep='\s+'
    )
    num_batch_test = num_test_samples // batch_size
    final_number = num_test_samples % batch_size
    for batch in range(num_batch_test + 1):
        if batch < num_batch_test:
            x_batch_te, _ = dataInitializer_dhc_rs().batchData(
                x_test, _, batch, batch_size
            )
        else:
            x_batch_te = x_test[batch * batch_size: (batch * batch_size + final_number), :]
        feed_dict_test = {x: x_batch_te}
        pred_tmp = sess.run(prediction, feed_dict=feed_dict_test)
        accumulator.append(pred_tmp)
    fasta_fpn = sys.argv[3] + sys.argv[1] + sys.argv[2] + '.fasta'
    sequence = sfasta().getMerged(fasta_fpn)
    pos_list = sclength(int(sys.argv[4])).toPair(len(sequence))
    position = pfasta(sequence).pair(pos_list=pos_list)
    res = np.array(position)[:, [0, 1, 3, 4]]
    pred_data = accumulator[0]
    for i in range(1, len(accumulator)):
        pred_data = np.concatenate((pred_data, accumulator[i]), axis=0)
    pred_data = np.concatenate((res, pred_data[:, [1]]), axis=1)
    return pd.DataFrame(pred_data).to_csv(
        sys.argv[8] + sys.argv[1] + sys.argv[2] + sys.argv[10],
        sep='\t',
        header=None,
        index=False
    )
stage2_Graph_Call()
