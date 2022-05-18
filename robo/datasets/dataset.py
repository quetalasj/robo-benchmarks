from abc import ABC, abstractmethod


class Dataset(ABC):

    @abstractmethod
    def download(self):
        raise NotImplementedError

    @abstractmethod
    def remove(self):
        raise NotImplementedError
    