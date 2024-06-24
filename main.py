import argparse
from src.args import Args
from loguru import logger

if __name__ == '__main__':
    logger.add("./app.log")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        type=str,
        help='save dir'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='backup output dir'
    )
    parser.add_argument(
        '--time',
        type=int,
        default=1,
        help='time interval (minuter)'
    )
    parse_args = parser.parse_args()
    args = Args(**parse_args.__dict__)
