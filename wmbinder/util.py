
import atexit
import os
import signal
import time

from os.path import join, dirname, exists


def setup_service(path):
    """
    Kill old service instances and write PID file.
    """

    pidfile = join(path, 'run.pid')
    if exists(pidfile):
        try:
            handle = open(pidfile, 'r')
            pid = int(handle.read())
            handle.close()
            os.kill(pid, signal.SIGHUP)
            # Wait until the proces has quit -- otherwise it will remove
            # our pid file and conflict with our bind calls.
            for i in xrange(20): # 4 seconds
                try:
                    os.kill(pid, 0)
                    time.sleep(0.2)
                except OSError:
                    break;
        except Exception as e:
            print('Error killing old wmbinder instance: %s' % e)


    try:
        handle = open(pidfile, 'w')
        handle.write(str(os.getpid()))
        handle.close()
        atexit.register(_remove_pid_file, pidfile)
    except Exception as e:
            print('Error writing pid file: %s' % e)



def _remove_pid_file(pidfile):
    try:
        os.remove(pidfile)
    except Exception as e:
        print('Error removing pid file: %s' % e)

