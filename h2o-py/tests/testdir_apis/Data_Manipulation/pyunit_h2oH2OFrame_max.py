from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from h2o.utils.typechecks import assert_is_type
from random import randrange
import numpy as np


def h2o_H2OFrame_max():
    """
    Python API test: h2o.frame.H2OFrame.max()
    """
    row_num = randrange(1,10)
    col_num = randrange(1,10)
    python_lists = np.random.randint(-5,5, (row_num, col_num))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)
    assert abs(h2oframe.max()-np.ndarray.max(python_lists)) < 1e-12, "h2o.H2OFrame.max() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_max())
else:
    h2o_H2OFrame_max()
