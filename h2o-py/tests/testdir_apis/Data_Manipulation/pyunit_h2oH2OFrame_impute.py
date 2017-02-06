from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from random import randrange
import numpy as np
from scipy.stats import mode


def h2o_H2OFrame_impute():
    """
    Python API test: h2o.frame.H2OFrame.impute(column=-1, method='mean', combine_method='interpolate', by=None,
    group_by_frame=None, values=None)
    """
    python_lists = np.random.randint(-5,5, (100,3))
    col0 = list(python_lists[:,0])
    col1 = list(python_lists[:,1])
    col2 = list(python_lists[:,2])
    h2oframe = h2o.H2OFrame(python_obj=python_lists, column_types=["int", "int", "enum"])

    row_ind_mean = randrange(0,h2oframe.nrow)       # row and col index that we want to set to NA and impute with mean
    del col0[row_ind_mean]
    impute_mean = np.mean(col0)

    row_ind_median = randrange(0,h2oframe.nrow)      # row and col index that we want to set to NA and impute with median
    del col1[row_ind_median]
    impute_median = np.median(col1)

    row_ind_mode = randrange(0,h2oframe.nrow)       # row and col index that we want to set to NA and impute with mode
    del col2[row_ind_mode]
    impute_mode = mode(col2).__getitem__(0)[0]

    h2oframe[row_ind_mean, 0]=float("nan")      # insert nans into frame
    h2oframe[row_ind_median, 1]=float("nan")
    h2oframe[row_ind_mode, 2]=float("nan")

    h2oframe.impute(column=0, method='mean', by=None, group_by_frame=None, values=None)
    h2oframe.impute(column=1, method='median', combine_method='average', group_by_frame=None, values=None)
    h2oframe.impute(column=2, method='mode')

    # check to make sure correct methods are imputed
    assert abs(h2oframe[row_ind_mean, 0]-impute_mean) < 1e-6, "h2o.H2OFrame.impute() command is not working."
    assert abs(h2oframe[row_ind_median, 1]-impute_median) < 1e-6, "h2o.H2OFrame.impute() command is not working."
    assert abs(int(h2oframe[row_ind_mode, 2])-impute_mode) < 1e-6, "h2o.H2OFrame.impute() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_impute())
else:
    h2o_H2OFrame_impute()
