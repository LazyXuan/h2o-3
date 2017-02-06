from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame
from random import randrange
import numpy as np

def h2o_H2OFrame_median():
    """
    Python API test: h2o.frame.H2OFrame.median(na_rm=False)
    """
    row_num = randrange(1,10)
    col_num = randrange(1,10)
    python_lists = np.random.randint(-5,5, (row_num, col_num))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)

    # axis = 0
    h2oMedian = h2oframe.median(na_rm=True)
    assert_is_type(h2oMedian, list)
    numpmedian = list(np.median(python_lists, axis=0))
    pyunit_utils.equal_two_arrays(numpmedian, h2oMedian, 1e-12, 1e-6)

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_median())
else:
    h2o_H2OFrame_median()
