import argparse
from robo.datasets.tum.tum import TumDataset

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Datasets management")
    parser.add_argument('-d', dest='dataset', help='dataset name')
    parser.add_argument('-s', dest='sequence', help='sequence name')
    # parser.add_argument('download', type=str, help='download dataset/sequence')
    # parser.add_argument('remove', type=str, help='remove dataset/sequence')



    args = parser.parse_args()
