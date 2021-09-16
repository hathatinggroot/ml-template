from data.base.dataset import AbstractDataset
from torch.utils.data import DataLoader, Subset

def get_loader(data_set: AbstractDataset, batch_size: int = 20, num_workers:int = 2):
    return DataLoader(
        data_set,
        batch_size=batch_size,
        num_workers=num_workers
    )

