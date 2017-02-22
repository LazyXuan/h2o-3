from __future__ import print_function
import sys
sys.path.insert(1,"../../")
from tests import pyunit_utils
from h2o.assembly import *
from h2o.utils.typechecks import assert_is_type

def h2oassembly_greater_than_equal():
    """
    Python API test: H2OAssembly.greater_than_equal(frame1, frame2)
    """
    python_list1 = [[4,4,4,4],[4,4,4,4]]
    python_list2 = [[2,2,2,2], [2,2,2,2]]
    bigframe = h2o.H2OFrame(python_obj=python_list1)
    smallframe = h2o.H2OFrame(python_obj=python_list2)
    resultFrame = H2OAssembly.greater_than_equal(bigframe, smallframe)
    equalFrame = H2OAssembly.greater_than_equal(smallframe, smallframe)

    assert_is_type(resultFrame, H2OFrame)
    assert resultFrame.all(), "H2OAssembly.greater_than_equal() command is not working."
    assert equalFrame.all(), "H2OAssembly.greater_than_equal() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oassembly_greater_than_equal)
else:
    h2oassembly_greater_than_equal()
