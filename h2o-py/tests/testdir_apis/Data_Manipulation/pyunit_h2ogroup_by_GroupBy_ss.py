from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.group_by import GroupBy
from h2o.frame import H2OFrame

def h2ogroup_by_GroupBy_ss():
    """
    Python API test: h2o.group_by.GroupBy.ss(col=None, na='all')

    Copied from pyunit_groupby_allOps.py
    """
    h2o_iris = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris_wheader.csv"))
    groupbyObj = GroupBy(fr=h2o_iris, by="class")

    opers = groupbyObj.ss(col=None, na='all')
    assert_is_type(opers, GroupBy)     # check return type

    operInfo = opers.get_frame()     # look into group by result
    assert_is_type(operInfo, H2OFrame)
    assert operInfo.shape == (3,5), "h2o.group_by.GroupBy.ss() command is not working."
    assert abs(operInfo[0, "sumSquares_sepal_len"]-1259.09) < 1e-6, "h2o.group_by.GroupBy.ss() command is not working."
    assert abs(operInfo[1, "sumSquares_sepal_wid"]-388.47) < 1e-6, "h2o.group_by.GroupBy.ss() command is not working."
    assert abs(operInfo[2, "sumSquares_petal_wid"]-208.93) < 1e-6, "h2o.group_by.GroupBy.ss() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ogroup_by_GroupBy_ss())
else:
    h2ogroup_by_GroupBy_ss()
