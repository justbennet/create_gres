#!/usr/bin/env python

#  This script will generate the text for total and available licenses
#  for software that has queryable licenses daemons (mostly FLEXlm).
#  The list of software tracked, and notes about it, is in the
#  file ../lib/monitor/config.py  -- bennet  26 Feb 2014

import sys, time, os
import subprocess as sp
from tempfile import mkstemp
import syslog
sys.path.append('/opt/moab/licenses/lib')

# This imports daemon[] and lmstat variables
from monitor.config import *
from monitor.flux import *

(tmpFd, tmpFname) = mkstemp(dir=gresDir)
tmpFile = os.fdopen(tmpFd, "w")
# Set tag and facility level for syslog messages
syslog.openlog(ident='gres_mon', facility=syslog.LOG_WARNING)

#  This is the output line this needs to produce
#  GLOBAL UPDATETIME=1391778771 STATE=idle ARES=abaqus:111 CRES=abaqus:229
#  where UPDATETIME is the seconds since the epoch.

for daemon in daemons:
    # Initialize the reply with a failure code to trigger the first query
    lmRet = [1, []]
    feature = daemon[0] ; server = daemon[1] ; gresName = daemon[2]
    licRsvd = int(daemon[3])
    lmCmd = [lmstat, '-f', feature, '-c', server]
    #  The while here breaks if the server doesn't respond.
    lmTryCount = 0
    while lmRet[0] > 0 and lmTryCount < 5:
        lmRet = lmQuery(lmCmd)
        queryTime = int(time.time())
        lmTryCount += 1
        if lmRet[0] == 0:
            break
        else:
            time.sleep(1)
    if lmRet[0] != 0:
        subjText = subjText % feature
        errMsgText = errMsgText % (feature, space.join(lmCmd), lmRet[1])
        tmpFile.write(gresLine % ( queryTime, gresName, 0, gresName, 0 ))
        sendNotice(toAddr, fromAddr, subjText, errMsgText)
    lmReplyText = lmRet[1].splitlines()
    featureUsagePat = 'Users of ' + feature
    for line in lmReplyText:
        if line.find(featureUsagePat) == 0:
            #  lmstat will return success (0) if the server responds.  Need to
            #  check that the total and used license counts are numbers, as they
            #  will not be if the license server didn't return a proper response.
            #  If an error, they are mostly transient, so write message to
            #  syslog and set ADEF and CDEF to 0 and continue.  Next run, they
            #  will most likely get set back to proper counts.  Jobs will not
            #  run if requesting the gres, but there won't be a chance of going
            #  on some sort of hold because the GRES becomes undefined.
            try:
                licTotal = int(line.split()[5])
            except:
                syslog.syslog(feature + ' returned an error, setting ARES=0 CRES=0')
                licTotal = int(0)
            try:
                licUsed  = int(line.split()[10])
            except:
                licUsed = int(0)
            # print feature, ": Total is ", licTotal, " and used is ", licUsed, " and licRsvd is ", licRsvd
            # print "Avail:  ", licTotal-licUsed-licRsvd
            tmpFile.write(gresLine % ( queryTime, gresName, licTotal-licUsed-licRsvd, gresName, licTotal))
            break
tmpFile.close()
syslog.closelog()
os.rename(tmpFname, gresFile)
