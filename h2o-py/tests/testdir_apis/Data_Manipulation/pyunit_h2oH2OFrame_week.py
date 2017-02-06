from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_week():
    """
    Python API test: h2o.frame.H2OFrame.week()
    """
    datetime = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/orc/orc2csv/TestOrcFile.testDate2038.csv"))
    datetime_week = datetime[0].week()
    checkweek = datetime_week == 18.0
    assert_is_type(datetime_week, H2OFrame)    # check return type, should be H2OFrame
    assert checkweek.any(), "h2o.H2OFrame.week() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_week())
else:
    h2o_H2OFrame_week()
