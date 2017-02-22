from __future__ import print_function
import sys
sys.path.insert(1,"../../")
from tests import pyunit_utils
from h2o.assembly import *
from h2o.utils.typechecks import assert_is_type

def h2oassembly_greater_than():
  """
  Python API test: H2OAssembly.greater_than(frame1, frame2)
  """
  python_list1 = [[4,4,4,4],[4,4,4,4]]
  python_list2 = [[2,2,2,2], [2,2,2,2]]
  bigframe = h2o.H2OFrame(python_obj=python_list1)
  smallframe = h2o.H2OFrame(python_obj=python_list2)
  resultFrame = H2OAssembly.greater_than(bigframe, smallframe)
  equalFrame = H2OAssembly.greater_than(smallframe, smallframe)

  assert_is_type(resultFrame, H2OFrame)
  assert resultFrame.all(), "H2OAssembly.greater_than() command is not working."
  assert not(equalFrame.all()), "H2OAssembly.greater_than() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oassembly_greater_than)
else:
    h2oassembly_greater_than()
