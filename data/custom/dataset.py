from torch.utils.data import dataset
from torchvision.datasets import MNIST

# inner module
from data.base.dataset import AbstractDataset

# mnist sample
class MNISTTrainDataset(AbstractDataset):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__(num_classes=num_classes)
        self.mnist = MNIST(root='../raw_data/local/mnist', train=True, download=True)

    def __getitem__(self, index: int) -> tuple:
        return self.mnist[index]
     
    def __len__(self) -> int:
        return len(self.mnist)
        
class MNISTTestDataset(MNISTTrainDataset):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__(num_classes=num_classes)
        self.mnist = MNIST(root='../raw_data/local/mnist', train=False, download=True)
