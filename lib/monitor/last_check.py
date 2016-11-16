import os, time

def touch_now(filename, time=None):
    '''This updates the last modified/accessed times for a file.'''
    with open(filename, 'a'):
        os.utime(filename, time)

def send_notice(now):
    '''This is a stub function to stand in for the one that will really
    send mail.
    '''
    readable_time = time.strftime("%Y %b %d %H:%M %p", time.localtime(now))
    print "\nAn error was detected while checking status at %s\n" % (readable_time)    

def touch_now(filename, time=None):
    '''This updates the last modified/accessed times for a file.'''
    with open(filename, 'a'):
        os.utime(filename, time)

def check_last_notice(last_check_file):
    '''Checks the modification time of the filename supplied and returns the
    elapsed time in minutes between the check time and modification time.  If
    the file does not exist, it returns -1
    '''
    # Save current time in seconds from epoch
    now = time.time()
    # We do different things if the semaphore file exits
    if os.path.isfile(last_check_file):
        # File exists
        # Get last modified time from existing file and return as minutes
        last_checked_time = os.path.getmtime(last_check_file)
        last_checked_time = (now - last_checked_time)/60
    else:
        # File does not exist
        last_checked_time = -1
    return last_checked_time

def check_last_notice(last_check_file):
    '''Checks the modification time of the filename supplied and returns the
    elapsed time in minutes between the check time and modification time.  If
    the file does not exist, it returns -1
    '''
    # Save current time in seconds from epoch
    now = time.time()
    # We do different things if the semaphore file exits
    if os.path.isfile(last_check_file):
        # File exists
        # Get last modified time from existing file and return as minutes
        last_checked_time = os.path.getmtime(last_check_file)
        last_checked_time = (now - last_checked_time)/60
    else:
        # File does not exist
        last_checked_time = -1
    return last_checked_time

# We want to send mail if it is the first time, or if at least an hour has
# elapsed since the last messag was sent.
# if last_checked_time > 60 or last_checked_time < 0:
#     send_notice(last_checked_time, last_checked_time)
#     touch_now(semaphore_file)

if __name__ == '__main__':
    #  Tests to be run if invoked as a program rather than being imported.
    # Use temporary files
    import tempfile
    now = time.time()

    print "Checking when file nonexistent"
    # Create a temporary file with a unique name, then delete it, so we know
    # it isn't there.
    test_file_handle, test_file_name = tempfile.mkstemp()
    os.close(test_file_handle)
    os.remove(test_file_name)
    last_checked_time = check_last_notice(test_file_name)
    if last_checked_time < 0:
        print "Passed:  No file."

    print "Checking for file less than 60 minutes old"
    test_file_handle, test_file_name = tempfile.mkstemp()
    os.close(test_file_handle)
    new_time = os.path.getmtime(test_file_name)
    new_time = time.strftime("%Y %b %d %H:%M %p", time.localtime(now))
    print "Timestamp on %s:  %s" % (test_file_name, new_time)
    if last_checked_time < 60:
        print "Passed:  No notice would be sent"
    else:
        print "Failed"
    os.remove(test_file_name)

    print "Checking when file is older than 60 minutes"
    test_file_handle, test_file_name = tempfile.mkstemp()
    os.close(test_file_handle)
    print "Checking when file is older than 60 minutes"
    print "Resetting mtime and atime to 61 minutes ago"
    old_time = os.path.getmtime(test_file_name)
    os.utime(test_file_name, (old_time-3601, old_time-3601))
    old_time = os.path.getmtime(test_file_name)
    old_time = time.strftime("%Y %b %d %H:%M %p", time.localtime(old_time))
    print "Old timestamp on %s:  %s" % (test_file_name, old_time)
    last_checked_time = check_last_notice(test_file_name)
    if last_checked_time > 60:
        touch_now(test_file_name)
        new_time = os.path.getmtime(test_file_name)
        new_time = time.strftime("%Y %b %d %H:%M %p", time.localtime(now))
        print "New timestamp on %s:  %s" % (test_file_name, new_time)
        print "Sending this error message..."
        print "="*78
        send_notice(now)
        print "="*78
    else:
        print "Failed"
    os.remove(test_file_name)

