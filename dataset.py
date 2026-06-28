import torch
import pandas as pd
from torch.utils.data import Dataset
from sklearn.preprocessing import StandardScaler

class MalwareDataset(Dataset):
    def __init__(self, csvPath):
        data = pd.read_csv(csvPath);
        print("Column text:", data.select_dtypes(include=['object']).columns)
        
        x_pandas = data.drop(columns=['class', 'packer_type'])
        y_pandas = data['class']
        
        scaler = StandardScaler()
        x_pandas = pd.DataFrame(scaler.fit_transform(x_pandas), columns=x_pandas.columns)
        
        self.xData = torch.tensor(x_pandas.values, dtype=torch.float32)
        self.yData = torch.tensor(y_pandas.values, dtype=torch.float32).unsqueeze(1)
    
    def __len__(self):
        return len(self.xData)
    
    def __getitem__(self, index):
        return self.xData[index], self.yData[index]