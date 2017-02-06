from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from h2o.utils.typechecks import assert_is_type
from random import randrange
import numpy as np


def h2o_H2OFrame_isfactor():
    """
    Python API test: h2o.frame.H2OFrame.isfactor()
    """
    row_num = randrange(1,10)
    col_num = randrange(1,10)
    python_lists = np.random.randint(-5,5, (row_num, col_num))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)
    newFrame = h2oframe.asfactor()
    clist = newFrame.isfactor()

    assert_is_type(clist, list)     # check return type
    assert sum(clist)==col_num, "h2o.H2OFrame.isfactor() command is not working."  # check return result


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_isfactor())
else:
    h2o_H2OFrame_isfactor()
