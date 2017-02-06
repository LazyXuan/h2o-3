from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2ocluster_info():
    """
    Python API test: h2o.cluster_info()
    Deprecated, use h2o.cluster().show_status().
    """
    h2o.cluster_info()    # no return type

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ocluster_info)
else:
    h2ocluster_info()
