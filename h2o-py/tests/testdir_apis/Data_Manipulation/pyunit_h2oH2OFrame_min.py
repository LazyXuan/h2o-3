from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from random import randrange
import numpy as np


def h2o_H2OFrame_min():
    """
    Python API test: h2o.frame.H2OFrame.min()
    """
    row_num = randrange(1,10)
    col_num = randrange(1,10)
    python_lists = np.random.randint(-5,5, (row_num, col_num))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)
    assert abs(h2oframe.min()-np.ndarray.min(python_lists)) < 1e-12, "h2o.H2OFrame.min() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_min())
else:
    h2o_H2OFrame_min()
