from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_mktime():
    """
    Python API test: static mktime(year=1970, month=0, day=0, hour=0, minute=0, second=0, msec=0)
    Deprecated, use moment() instead.
    """
    datetimeF = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/orc/orc2csv/TestOrcFile.testDate2038.csv"))
    datetime=datetimeF[0]
    mktime_datetime = h2o.H2OFrame.mktime(year=datetime.year(), month=datetime.month(), day=datetime.day(), hour=datetime.hour(), minute=datetime.minute(), second=datetime.second(), msec=0)
    diff = 2789999999.0
    assert_is_type(mktime_datetime, H2OFrame)
    assert abs(datetime[0,0]+diff-mktime_datetime[0,0]) < 1e-6, "h2o.H2OFrame.mktime() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_mktime())
else:
    h2o_H2OFrame_mktime()
