from model import MalwareModel
from dataset import MalwareDataset
import torch
from torch.utils.data import DataLoader

dataset = MalwareDataset('data/ClaMP_Integrated-5184.csv')

trainSize = int(0.7 * len(dataset))
testSize = len(dataset) - trainSize
trainDataset, testDataset = torch.utils.data.random_split(dataset, [trainSize, testSize])

trainLoader = DataLoader(trainDataset, batch_size=32, shuffle=True)
testLoader = DataLoader(testDataset, batch_size=32, shuffle=False)
model = MalwareModel(input_size=dataset.xData.shape[1])

loss = torch.nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
epochs = 10

bestTestLoss = float('inf')
patience = 0
maxPatience = 5

for epoch in range(epochs):
    sumTrainLoss, sumTestLoss = 0.0, 0.0
    
    for xBatch, yBatch in trainLoader:
        optimizer.zero_grad()
        yPred = model(xBatch)
        l = loss(yPred, yBatch)
        l.backward()
        optimizer.step()
        sumTrainLoss += l.item()
    
    for xBatch, yBatch in testLoader:
        with torch.no_grad():
            yPred = model(xBatch)
            l = loss(yPred, yBatch)
        sumTestLoss += l.item()
    
    avgTestLoss = sumTestLoss / len(testLoader)
    avgTrainLoss = sumTrainLoss / len(trainLoader)

    if avgTestLoss < bestTestLoss:
        bestTestLoss = avgTestLoss
        patience = 0
        torch.save(model.state_dict(), 'bestModel.pth')
    else:
        patience += 1
        if patience >= maxPatience:
            break
        
    print(f"Epoch {epoch+1}/{epochs}, Train Loss: {sumTrainLoss/len(trainLoader):.4f}, Test Loss: {sumTestLoss/len(testLoader):.4f}")