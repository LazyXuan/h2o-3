from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_dayOfWeek():
    """
    Python API test: h2o.frame.H2OFrame.dayOfWeek()

    Copied from pyunit_count_temps.py
    """
    datetime = h2o.import_file(path=pyunit_utils.locate("smalldata/parser/orc/orc2csv/TestOrcFile.testDate2038.csv"))
    datetime_dow = datetime[0].dayOfWeek()
    checkdow = datetime_dow == 'Wed'
    assert_is_type(datetime_dow, H2OFrame)    # check return type, should be H2OFrame
    assert checkdow.any(), "h2o.H2OFrame.dayOfWeek() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_dayOfWeek())
else:
    h2o_H2OFrame_dayOfWeek()
