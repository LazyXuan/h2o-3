from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_moment():
    """
    Python API test: static moment(year=None, month=None, day=None, hour=None, minute=None, second=None, msec=None,
     date=None, time=None
    """
    datetimeF = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/orc/orc2csv/TestOrcFile.testDate2038.csv"))
    datetime=datetimeF[0]
    mktime_datetime = h2o.H2OFrame.moment(year=datetime.year(), month=datetime.month(), day=datetime.day(),
                                          hour=datetime.hour(), minute=datetime.minute(), second=datetime.second(),
                                          msec=0, date=None, time=None)
    assert_is_type(mktime_datetime, H2OFrame)

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_moment())
else:
    h2o_H2OFrame_moment()
