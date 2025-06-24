import pandas as pd
import networkx as nx
import pickle
import torch
import torch.nn.functional as F
import torch.nn as nn
from torch_geometric.utils import from_networkx
from torch_geometric.nn import SAGEConv


# ------------------------------
# Step 3: Define GNN Model
# ------------------------------
class GNN(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        self.conv1 = SAGEConv(in_channels, hidden_channels)
        self.conv2 = SAGEConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x = self.conv2(x, edge_index)
        return x