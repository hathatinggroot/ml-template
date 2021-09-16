from torch import Tensor
from torch.utils.data import Dataset, Subset
from sklearn.model_selection import StratifiedKFold
import numpy as np


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

    def get_k_fold(self, k: int = 5):
        skf = StratifiedKFold(n_splits=k)
        folds = []
        for train_indices, valid_indices in skf.split(self.X, self.y):
            folds.append((Subset(self, train_indices), Subset(self, valid_indices)))
    
        return folds





        
