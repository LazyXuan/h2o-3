from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame


def h2o_H2OFrame_cummax():
    """
    Python API test: h2o.frame.H2OFrame.cummax(axis=0)

    Copied from pyunit_cumsum_cumprod_cummin_cummax.py
    """
    python_object=[list(range(10)), list(range(10))]
    python_object_transpose = np.transpose(python_object)
    foo = h2o.H2OFrame(python_obj=python_object)
    foo_transpose =  h2o.H2OFrame(python_obj=python_object_transpose)

    cummax_col = foo_transpose.cummax()   # default
    cummax_row = foo.cummax(axis=1)   # row

    # check correct return type
    assert_is_type(cummax_col, H2OFrame)
    assert_is_type(cummax_row, H2OFrame)

    # check correct result
    pyunit_utils.compare_frames(cummax_col, foo_transpose, 0, tol_time=0, tol_numeric=1e-6, strict=False, compare_NA=False)
    pyunit_utils.compare_frames(cummax_row, foo, 0, tol_time=0, tol_numeric=1e-6, strict=False, compare_NA=False)

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_cummax())
else:
    h2o_H2OFrame_cummax()
