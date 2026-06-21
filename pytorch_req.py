import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')

devnumber = torch.cuda.current_device() if torch.cuda.is_available() else 'CPU'
print(f'Current device number: {devnumber}')

devName = torch.cuda.get_device_name(devnumber)
print(f'Current device name: {devName}') 