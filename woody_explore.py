import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List

def is_populated(row:pd.Series)->List:
    return type(row)