import datetime

class Stopwatch(object):
    ''' Stopwatch helper class for computing and displaying timings.'''

    def __init__(self):
        self.restart()

    def restart(self):
        self.start = datetime.datetime.now()
        self.last = self.start
        return self.start.isoformat(timespec='milliseconds')

    def lap(self):
        now = datetime.datetime.now()
        delta = now - self.last
        elapsed = now - self.start
        self.last = now
        ts = now.isoformat(timespec='milliseconds')
        return ts, delta, elapsed

    def timestamp(self):
        return datetime.datetime.now().isoformat(timespec='milliseconds')
