# Drug-likeness prediction with Bayesian neural networks

To define drug-likeness, a set of 2136 approved drugs from DrugBank was taken as drug-like, and three negative datasets were selected from ZINC15 (19M), the Network of Organic Chemistry (6M) and ligands from the Protein Data Bank (13k), respectively. The drug dataset was combined with an equal subsampling of the negative dataset for each experiment, using five different molecular representations (Mold2, RDKit, MCS, EXFP4, Mol2Vec). We have re-trained it following the author’s specifications.

This model was incorporated on 2022-11-09.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9sa2`
- **Slug:** `bayesian-drug-likeness`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Drug-likeness`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Drug-likeness score. Higher score indicates higher drug-likeness

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| drug_likeness | float | high | Drug likeness score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Replicated`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9sa2](https://hub.docker.com/r/ersiliaos/eos9sa2)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9sa2.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9sa2.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/Nanotekton/drugability/tree/v0.1](https://github.com/Nanotekton/drugability/tree/v0.1)
- **Publication**: [https://www.nature.com/articles/s42256-020-0209-y](https://www.nature.com/articles/s42256-020-0209-y)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Non-commercial](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9sa2
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9sa2
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
