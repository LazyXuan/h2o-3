from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils

def h2o_H2OFrame_all():
    """
    Python API test: h2o.frame.H2OFrame.all()
    """
    python_lists = [[1,1,1,1], [1,1,1,1]]
    h2oframe = h2o.H2OFrame(python_obj=python_lists, na_strings=['NA'])
    h2oframe[0]=h2oframe[0]>0.0
    h2oframe[1]=h2oframe[1]>0.0
    h2oframe[2]=h2oframe[2]>0.0
    h2oframe[3]=h2oframe[3]>0.0
    assert h2oframe.all(), "h2o.H2OFrame.all() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_all())
else:
    h2o_H2OFrame_all()
