from torch import Tensor
from torch.utils.data import Dataset


class AbstractDataset(Dataset):
    X: Tensor
    y: Tensor
    num_classes: int

    def __init__(self, num_classes: int) -> None:
        super().__init__()
        self.num_classes = num_classes

    def __getitem__(self, index: int) -> tuple:
        return self.X[index], self.y[index]

    def __len__(self) -> int:
        return len(self.X)        
        
