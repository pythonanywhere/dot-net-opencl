from os.path import abspath, dirname, join
dllPath = join(dirname(abspath(__file__)), "DotNetOpenCL", "DotNetOpenCL", "bin", "Release")

import sys
sys.path.append(dllPath)

import clr
clr.AddReference("DotNetOpenCL")

from DotNetOpenCL import CL
from System import Array, IntPtr

errorCode, numPlatforms = CL.clGetPlatformIDs(0, None)
print "Error code", errorCode
print "Number of platforms", numPlatforms

platforms = Array.CreateInstance(IntPtr, numPlatforms)
errorCode, numPlatformsReturned = CL.clGetPlatformIDs(numPlatforms, platforms)
print "Number of platforms returned", numPlatformsReturned
print "Platform array", platforms
for i in range(numPlatformsReturned):
	print "Platform #%s: %s" % (i, platforms[i])