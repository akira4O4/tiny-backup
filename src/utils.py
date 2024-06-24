import os
import shutil
import time


def backup(root: str, output: str) -> None:
    if os.path.isdir(output):
        shutil.copy(root, output)
    else:
        output = os.path.join(root, output)
        shutil.copy(root, output)


def check_dir_exists(path: str, clean: bool = False) -> None:
    if os.path.exists(path):
        if clean:
            shutil.rmtree(path)
            os.makedirs(path)
    else:
        os.makedirs(path)


def get_time(fmt: str = '%Y%m%d_%H%M%S') -> str:
    # 20221114_173542
    time_str = time.strftime(fmt, time.localtime())
    return str(time_str)


if __name__ == '__main__':
    backup(r"D:\llf\code\tiny-backup\VERSION", r'D:\llf\code\tiny-backup\temp')
