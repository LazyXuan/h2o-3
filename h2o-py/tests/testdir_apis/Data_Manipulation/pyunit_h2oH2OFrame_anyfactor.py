from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_anyfactor():
    """
    Python API test: h2o.frame.H2OFrame.anyfactor()
    """
    python_lists = [[1,1,1,1], [1,1,1,1]]
    h2oframe = h2o.H2OFrame(python_obj=python_lists, na_strings=['NA'])
    assert_is_type(h2oframe, H2OFrame)
    # should return false since all are numbers
    assert not(h2oframe.anyfactor()), "h2o.H2OFrame.anyfactor() command is not working."
    h2oframe[0]=h2oframe[0].asfactor()     # change one column to categorical
    assert h2oframe.anyfactor(), "h2o.H2OFrame.anyfactor() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_anyfactor())
else:
    h2o_H2OFrame_anyfactor()
