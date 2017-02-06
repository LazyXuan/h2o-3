from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame


def h2o_H2OFrame_countmatches():
    """
    Python API test: h2o.frame.H2OFrame.countmatches(pattern)

    Copied from pyunit_countmatches.py
    """
    prostate_frame = h2o.import_file(path=pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"))
    leftover = prostate_frame["DPROS"].cbind(prostate_frame["CAPSULE"]).cbind(prostate_frame["DCAPS"])
    leftover.ascharacter()  # change to string
    matches = leftover.countmatches(['left', 'No', 'Yes'])
    assert_is_type(matches, H2OFrame)
    assert matches.shape == leftover.shape, "h2o.H2OFrame.countmatches() command is not working."
    assert matches.any(), "h2o.H2OFrame.countmatches() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_countmatches())
else:
    h2o_H2OFrame_countmatches()
