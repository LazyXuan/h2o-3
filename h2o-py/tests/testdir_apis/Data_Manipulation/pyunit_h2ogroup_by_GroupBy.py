from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.group_by import GroupBy

def h2ogroup_by_GroupBy():
    """
    Python API test: h2o.group_by.GroupBy(fr, by)

    Copied from pyunit_groupby_allOps.py
    """
    h2o_prostate = h2o.import_file(path=pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"))
    by=["CAPSULE", "RACE"]
    groupbyObj = GroupBy(fr=h2o_prostate, by=by)
    assert_is_type(groupbyObj, GroupBy)

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ogroup_by_GroupBy())
else:
    h2ogroup_by_GroupBy()
