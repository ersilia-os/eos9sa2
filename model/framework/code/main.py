# imports
import os
import csv
import sys
import numpy as np
import gzip
import yaml
from pathlib import Path
from .model import make_ae_model  ## fix path 
from data_preprocess import _normalize

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# generate descriptors
with open(input_file,'r') as f1, open('smiles.txt','w') as f2:
    next(f1)
    for line in f1:
        f2.write(line)
        
vectorize_script_path = os.path.abspath(os.path.join(root, "..", "model/scripts/vectorize.py"))
command = "python " + vectorize_script_path + " --output_core smiles --descriptor rdkit " + input_file
os.system(command)

with gzip.open('smiles.npz', 'rb') as f:
      data = np.load(f)
        
data_path = os.path.abspath(os.path.join(root, "..", "model/data/"))       
idx = ( data_path + 'zinc15_nondrugs_sample_rdkit_mu.npz', data_path + 'zinc15_nondrugs_sample_rdkit_std.npz', data_path + 'zinc15_nondrugs_sample_rdkit_idx.npz')
x = _normalize(data, idx, True)

#load model 
config_path =  os.path.abspath(os.path.join(root, "..", "model/config_files/rdkit_ae_zinc_bayesian.yaml"))
config = yaml.safe_load(config_path.read_text())
config = config['model_params']
input_shape = 199  
output_shape = (1,2)
model, metric = make_ae_model(input_shape, output_shape, config)
   
# run model
proba = model.predict(x)  # slice data, run predictions in a loop
pos_class_proba = [[proba[:,1].tolist()[i]] for i in range(0, len(proba))]

# write output in a .csv file        
header = ['drug-likeness']  
with open(output_file, 'w') as f:
    write = csv.writer(f)
    write.writerow(header)
    write.writerows(pos_class_proba)
