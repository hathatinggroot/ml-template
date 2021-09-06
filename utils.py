import os
from typing import Any
import datetime
from pytz import timezone

class TextLogger():
    def __init__(self, saveDir) -> None:
        self.saveDir = os.path.join(saveDir, 'log.txt')
    
    def __call__(self, msg: str) -> Any:
        now = datetime.datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")
        with open(self.saveDir, mode='a+', encoding='utf-8') as f:
            print(msg)
            f.writelines(f'\n[{now}]\t{msg}')


def create_path(path: str):
    if os.path.exists(path):
        return
    parent, child = os.path.split(path)
    if not os.path.exists(parent):
        create_path(parent)
    os.mkdir(path)