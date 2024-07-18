import torch



def train(device,model,train_loader,optimizer,criterion,transforms):
  loss = 0
  total_correct = 0
  total_samples = 0
  
  model.train()
  for x,y in train_loader:
    x,y = x.to(device),y.to(device)
    output = model(transforms(x))
    if output.dim() > 2:
        output = torch.squeeze(output)
      
    optimizer.zero_grad()
    correct = (torch.argmax(output,dim=1) ==y).sum().item()
    total_correct += correct
    total_samples += y.size(0)
    batch_loss = criterion(output,y)
    loss += batch_loss.item()
    batch_loss.backward()
    optimizer.step()

  accuracy = total_correct/ total_samples
  loss = loss / len(train_loader)
  print('Train - Loss : {:.4f} Accuracy : {:.4f}'.format(loss,accuracy))
    
  

def validate(device,model,valid_loader,criterion,transforms):
  loss = 0
  total_correct = 0
  total_samples = 0
  
  model.eval()
  with torch.no_grad():
    for x,y in valid_loader:
      x,y = x.to(device),y.to(device)
      output =model(transforms(x))
      if output.dim() > 2:
        output = torch.squeeze(output)
      
      correct = (torch.argmax(output,dim=1) ==y).sum().item()
      total_correct += correct
      total_samples += y.size(0)
      loss += criterion(output,y).item()

  accuracy = total_correct/ total_samples
  loss = loss / len(valid_loader)
  print('Valid - Loss : {:.4f} Accuracy : {:.4f}'.format(loss,accuracy))
    