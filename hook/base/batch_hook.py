
# inner modules 
from utils import TextLogger

def default_batch_hook(batch_idx: int, interval: int, prevHookVals: dict=None, **kargs):
    if prevHookVals is None:
        prevHookVals = {
            "loss_value" : 0,
            "matches" : 0
        }
    keys = kargs.keys()
    if keys.__contains__('text_logger'):
        kargs['text_logger']()


    