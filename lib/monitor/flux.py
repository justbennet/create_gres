# lmCmd should be a list with all the arguments needed for the
# lmstat command, e.g.,
# [ '/usr/caen/FLEXlm/bin/lmstat', '-f', feature, '-c', 'port@server' ]
import subprocess as sp
import time

def lmQuery(lmCmd):
    '''\
    lmQuery:  Takes a list with the elements needed to run lmstat against
    a license daemon, runs the query up to five times to get a valid result,
    and passes back a list with the return code and lmstat reply.'''
    lmRet = [1, []]
    lmCount = 0
    try:
        result = []
        lm_out = sp.check_output(lmCmd, stderr=sp.STDOUT)
        result = [ 0, lm_out ]
        # print "Result is ", result
        return result
    except sp.CalledProcessError, err:
        # Need result to have the same format as result in success
        lmRet = [ err.returncode, err.output ]
        lmCount += lmCount
        # print "\n\n\nException lmRet is ", lmRet
        return lmRet
    # end try
#end def lmQuery

import smtplib
from email.mime.text import MIMEText
from flux import *

def sendNotice(toAddr, fromAddr, subjText, msgText):
    smtpHost = 'localhost'

    msg = MIMEText(msgText)
    msg['Subject'] = subjText
    msg['From']    = fromAddr
    msg['To']      = toAddr

    try:
        s = smtplib.SMTP('localhost')
    except Exception, err:
        "Error establishing SMTP connection to localhost\n" + \
        "%s: %s." % ( smtpHost, str(err) )
        return False
    # end try

    try:
        s.sendmail(fromAddr, [toAddr], msg.as_string())
        s.quit()
    except Exception, err:
        print "Error sending mail to %s: %s." % \
        (toAddr, str(err))
        return False
    # end try
# end def sendNotice

