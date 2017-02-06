from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2o_H2OFrame_type():
    """
    Python API test: h2o.frame.H2OFrame.type(col)

    Copied frm pyunit_trim.py
    """
    column_types = ["string","numeric","numeric","numeric","numeric","numeric","numeric","numeric"]
    frame = h2o.import_file(path=pyunit_utils.locate("smalldata/junit/cars_trim.csv"), col_types=column_types)

    for index in range(frame.ncol):
        try:
            assert frame.type(index)==column_types[index], "h2o.H2OFrame.type() command is not working."
        except:
            assert frame.type(index)=="int" or frame.type(index)=="real", "h2o.H2OFrame.type() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_type())
else:
    h2o_H2OFrame_type()
