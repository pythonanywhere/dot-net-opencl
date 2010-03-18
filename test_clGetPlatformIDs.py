from os.path import abspath, dirname, join
dllPath = join(dirname(abspath(__file__)), "DotNetOpenCL", "DotNetOpenCL", "bin", "Release")

import sys
sys.path.append(dllPath)

import clr
clr.AddReference("DotNetOpenCL")

from DotNetOpenCL import CL
from System import IntPtr

errorCode, numPlatforms = CL.clGetPlatformIDs(0, IntPtr.Zero)
print "Error code", errorCode
print "Number of platforms", numPlatforms
