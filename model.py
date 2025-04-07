import torch.nn as nn
class DeepCNN(nn.Module):
    def __init__(self, num_layers, hidden_size, dropout_rate):
        super(DeepCNN, self).__init__()
        layers = []
        in_channels = 1  # Grayscale images

        for _ in range(num_layers):
            layers.append(nn.Conv2d(in_channels, hidden_size, kernel_size=3, padding=1))
            layers.append(nn.ReLU())
            layers.append(nn.MaxPool2d(2, 2))
            layers.append(nn.Dropout(dropout_rate))
            in_channels = hidden_size

        self.cnn_layers = nn.Sequential(*layers)
        self.fc = nn.Linear(hidden_size * (64 // (2 ** num_layers)) ** 2, 2)  # Binary classification

    def forward(self, x):
        x = self.cnn_layers(x)
        x = x.view(x.size(0), -1)  # Flatten
        return self.fc(x)