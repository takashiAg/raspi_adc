import threading



class sample_thread(threading.Thread):
    """docstring for TestThread"""

    def __init__(self,Realtime):
        super(sample_thread, self).__init__()
        self.Realtime=Realtime

    def run(self):

