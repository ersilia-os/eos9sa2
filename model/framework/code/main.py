# imports
import os
import csv
import sys
import numpy as np
import gzip
import yaml
from pathlib import Path

ROOT = os.path.abspath(os.path.dirname(__file__))
code_path = os.path.abspath(os.path.join(ROOT, "..", "model"))
sys.path.append(code_path)
from models import make_ae_model   
from data_preprocess import _normalize

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# generate descriptors
f = open(input_file,'r')
lines = f.readlines()[1:]
f.close()

with open('temp.txt', 'w') as f:
      for line in lines:
            f.write(line)

data_path = os.path.abspath(os.path.join(root, "..", "model/data"))     
vectorize_script_path = os.path.abspath(os.path.join(root, "..", "model/scripts/vectorize.py"))
command = "python " + vectorize_script_path + " --output_core " + data_path+"/smiles --descriptor rdkit temp.txt"
os.system(command)

with gzip.open(data_path+"/smiles.npz", 'rb') as f:
      data = np.load(f)

print("Data before normalization",data.shape)
idx = ( data_path + '/zinc15_nondrugs_sample_rdkit_mu.npz', data_path + '/zinc15_nondrugs_sample_rdkit_std.npz', data_path + '/zinc15_nondrugs_sample_rdkit_idx.npz')
x = _normalize(data, idx, True)
print("Data after normalization",x.shape)
#load model 

config_path =  os.path.abspath(os.path.join(root, "..", "model/config_files/rdkit_ae_zinc_bayesian.yaml"))
config = yaml.safe_load(Path(config_path).read_text())
config = config['model_params']
input_shape = 199  
output_shape = (1,2)
model, metric = make_ae_model(input_shape, output_shape, config)
   
# run model
proba = model.predict(x)  # slice data, run predictions in a loop
pos_class_proba = [[proba[:,1].tolist()[i]] for i in range(0, len(proba))]

# write output in a .csv file        
header = ['drug_likeness']  
with open(output_file, 'w') as f:
    write = csv.writer(f)
    write.writerow(header)
    write.writerows(pos_class_proba)
