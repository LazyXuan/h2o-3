from __future__ import print_function
import sys
sys.path.insert(1,"../../")
from tests import pyunit_utils
from h2o.assembly import *
from h2o.utils.typechecks import assert_is_type

def lending_club_munging_plus():
  """
  Python API test: H2OAssembly.plus(frame1, frame2)
  """
  python_list1 = [[4,4,4,4],[4,4,4,4]]
  python_list2 = [[2,2,2,2], [2,2,2,2]]
  h2oframe = h2o.H2OFrame(python_obj=python_list1)
  frame_divisor = h2o.H2OFrame(python_obj=python_list2)
  resultFrame = H2OAssembly.plus(h2oframe, frame_divisor)

  assert_is_type(resultFrame, H2OFrame)
  assert (resultFrame==6).all(), "H2OAssembly.plus() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(lending_club_munging_plus)
else:
    lending_club_munging_plus()
