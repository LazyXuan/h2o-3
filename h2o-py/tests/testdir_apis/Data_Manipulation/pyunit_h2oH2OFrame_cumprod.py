from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame


def h2o_H2OFrame_cumprod():
    """
    Python API test: h2o.frame.H2OFrame.cumprod(axis=0)

    Copied from pyunit_cumsum_cumprod_cummin_cummax.py
    """
    python_object=[list(range(1,10)), list(range(1,10))]
    python_object_transpose = np.transpose(python_object)
    foo = h2o.H2OFrame(python_obj=python_object)
    foo_transpose =  h2o.H2OFrame(python_obj=python_object_transpose)

    cumprod_col = foo_transpose.cumprod()   # default
    cumprod_row = foo.cumprod(axis=1)   # row

    # check correct return type
    assert_is_type(cumprod_col, H2OFrame)
    assert_is_type(cumprod_row, H2OFrame)

    # check correct result
    pyunit_utils.assert_corret_frame_operation(foo_transpose, cumprod_col, 'cumprod')
    pyunit_utils.compare_frames(cumprod_col, cumprod_row.transpose(), cumprod_col.nrow, tol_time=0, tol_numeric=1e-6)

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_cumprod())
else:
    h2o_H2OFrame_cumprod()
