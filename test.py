# Use files in src folder
from src.data import prepare_data
from src.models import GCN
from src.train import *

# Load the dataset
data = prepare_data(dataset='Cora')

# Define the model
hparams = {
		'input_dim': data.x.size(1),
		'hidden_dim': 16,
		'output_dim': max(data.y).item() + 1
		}
model = GCN(**hparams)

# Train the model
train_error = train_and_val(model, data, num_epochs=150)

# Predictions
log_logits = model(x=data.x, edge_index=data.edge_index) # [2708, 7]
probas = log_logits.exp()  

# Evaluate the model - test set