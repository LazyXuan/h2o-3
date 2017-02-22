from __future__ import print_function
import sys
sys.path.insert(1,"../../")
from tests import pyunit_utils
from h2o.assembly import *
from h2o.utils.typechecks import assert_is_type

def h2oassembly_equal_equal():
  """
  Python API test: H2OAssembly.equal_equal(frame1, frame2)
  """
  python_list1 = [[4,4,4,4],[4,4,4,4]]
  python_list2 = [[2,2,2,2], [2,2,2,2]]
  h2oframe = h2o.H2OFrame(python_obj=python_list1)
  frame_divisor = h2o.H2OFrame(python_obj=python_list2)
  resultFrame = H2OAssembly.equal_equal(h2oframe, frame_divisor)
  sameFrame =  H2OAssembly.equal_equal(h2oframe, h2oframe)
  assert_is_type(resultFrame, H2OFrame)
  assert not(resultFrame.all()), "H2OAssembly.equal_equal() command is not working."
  assert sameFrame.all(), "H2OAssembly.equal_equal() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oassembly_equal_equal)
else:
    h2oassembly_equal_equal()
