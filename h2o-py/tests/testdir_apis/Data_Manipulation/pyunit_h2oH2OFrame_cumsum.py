from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame


def h2o_H2OFrame_cumsum():
    """
    Python API test: h2o.frame.H2OFrame.cumsum(axis=0)

    Copied from pyunit_cumsum_cumprod_cummin_cummax.py
    """
    python_object=[list(range(1,10)), list(range(1,10))]
    python_object_transpose = np.transpose(python_object)
    foo = h2o.H2OFrame(python_obj=python_object)
    foo_transpose =  h2o.H2OFrame(python_obj=python_object_transpose)

    cumsum_col = foo_transpose.cumsum()   # default
    cumsum_row = foo.cumsum(axis=1)   # row

    # check correct return type
    assert_is_type(cumsum_col, H2OFrame)
    assert_is_type(cumsum_row, H2OFrame)

    # check correct result
    pyunit_utils.assert_corret_frame_operation(foo_transpose, cumsum_col, 'cumsum')
    pyunit_utils.assert_corret_frame_operation(foo, cumsum_row, 'cumsum')

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_cumsum())
else:
    h2o_H2OFrame_cumsum()
