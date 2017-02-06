from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_sqrt():
    """
    Python API test: h2o.frame.H2OFrame.sqrt()
    """
    python_lists = np.random.uniform(0.01,5, (10,2))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)
    newframe = h2oframe.sqrt()
    assert_is_type(newframe, H2OFrame)      # check return type
    pyunit_utils.assert_corret_frame_operation(h2oframe, newframe, "sqrt")      # check values

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_sqrt())
else:
    h2o_H2OFrame_sqrt()
