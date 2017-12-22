"""Setup some useful test variables.
"""
import sys
import os

TESTDIR = os.path.dirname(__file__)
ROOTDIR = os.path.join(TESTDIR, os.pardir)

INTEGRATION_FILEDIR = os.path.join(TESTDIR, 'integration')
ENDTOEND_FILEDIR = os.path.join(TESTDIR, 'end-to-end')

sys.path.append(ROOTDIR)
