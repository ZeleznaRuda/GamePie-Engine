import threading

class Thread:
    def __init__(self, func, *args, sync_kill=True, auto_start=True, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.sync_kill = sync_kill
        self._running = False
        self._stop_flag = threading.Event()
        self.thread = threading.Thread(target=self._run, daemon=sync_kill)

        if auto_start:
            self.start()

    def _run(self):
        self._running = True
        try:
            self.func(self._stop_flag, *self.args, **self.kwargs)
        finally:
            self._running = False

    def start(self):
        self.thread.start()

    def is_running(self):
        return self._running

    def kill(self):
        self._stop_flag.set()
        if not self.sync_kill:
            self.thread.join()
