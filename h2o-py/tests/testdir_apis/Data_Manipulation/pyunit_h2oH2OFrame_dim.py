from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
import numpy as np
from random import randrange

def h2o_H2OFrame_dim():
    """
    Python API test: h2o.frame.H2OFrame.dim
    """
    numRow = randrange(1,10)
    numCol = randrange(1,10)
    python_lists = np.random.uniform(-1,1, (numRow, numCol))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)

    assert h2oframe.dim==[numRow, numCol], "h2o.H2OFrame.dim command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_dim())
else:
    h2o_H2OFrame_dim()
