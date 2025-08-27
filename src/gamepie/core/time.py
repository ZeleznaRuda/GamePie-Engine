'''
wait is a function that checks if a specified amount of time in milliseconds has passed since the last call. It returns a boolean value.
Correct usage is: if gamepie.wait(MS, KEY):
MS is the number of milliseconds that must pass, KEY is the identifier used to track the timer.
The function returns True only if it's called and the specified time has passed since the last call with that key. Otherwise,
it returns False.
wait does not run in the background – time is only checked when the function is called. If it is not called, time is not tracked.
If wait is placed inside another condition (e.g. key is pressed), the time is only checked when that condition is met.
This means waiting can be blocked if the wait function is not called continuously.
It is mainly used for actions that should not be triggered more often than the defined interval.
key type: f"<Name>.{id(<Name>)}:<Event>"
'''
# \033[31m'wait\033[1m(ms, key)\033[31m'\033[0m\n{" " * 32} \033[31m~~~~~~~~~\033[1m^^^\033[31m~\033[0m"
import time
import threading
_wait_cache_ = {}

def wait(ms=None, key=None):
    #/ai
    now = time.time()
    if not key:
        raise NameError(f"'key' has not defined.")
    if not ms:
        raise NameError(f"'ms' has not defined.")
    
    cooldown = _wait_cache_.get(key, 0)
    if now - cooldown >= ms / 1000:
        _wait_cache_[key] = now
        return True
    return False


def asyncWait(ms: int, callback, *args, **kwargs):
    t = threading.Timer(ms/1000, callback, args=args, kwargs=kwargs)
    t.start()
    return t