import os
from pathlib import Path
from src import DEFAULT_TIME, DEFAULT_TITLE
from utils import get_time
import shutil


class BackUp:
    def __init__(
        self,
        root: str,
        output: str,
        time: bool = DEFAULT_TIME
    ):
        self.root = Path(root)
        self.output = output
        self.time = time
        self.title = DEFAULT_TITLE

    def set_title(self, title: str) -> None:
        self.title = title

    def copy(self) -> None:
        curr_time: str = get_time()
        # output: path/title/20240624
        output = os.path.join(self.output, self.title, curr_time)
        shutil.copytree(str(self.root), output)


if __name__ == '__main__':
    backup = BackUp(
        r"D:\llf\code\tiny-backup\src",
        r"D:\llf\code\tiny-backup"
    )
    backup.set_title('EldenRing')
    backup.copy()
