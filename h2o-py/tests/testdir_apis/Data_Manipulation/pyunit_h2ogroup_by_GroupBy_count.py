from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.group_by import GroupBy
from h2o.frame import H2OFrame

def h2ogroup_by_GroupBy_count():
    """
    Python API test: h2o.group_by.GroupBy.count(na='all')

    Copied from pyunit_groupby_allOps.py
    """
    h2o_prostate = h2o.import_file(path=pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"))
    by=["CAPSULE", "RACE"]
    groupbyObj = GroupBy(fr=h2o_prostate, by=by)

    counts = groupbyObj.count(na='all')
    assert_is_type(counts, GroupBy)     # check return type

    countsInfo = counts.get_frame()     # look into group by result
    assert_is_type(countsInfo, H2OFrame)
    assert countsInfo.shape == ((h2o_prostate["CAPSULE"].nlevels()[0]*h2o_prostate["RACE"].nlevels()[0]), len(by)+1), \
        "h2o.group_by.GroupBy.count() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ogroup_by_GroupBy_count())
else:
    h2ogroup_by_GroupBy_count()
