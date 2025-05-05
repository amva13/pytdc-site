
from .tasks import _TASKS, _DESC
from .datasets import _DATASETS, _META

class SinglePredTasks:
    def __init__(self):
        self.tasks = _TASKS
        self.datasets = _DATASETS
        self.meta = _META
        self.desc = _DESC
        