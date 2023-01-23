# Drug-likeness prediction with Bayesian neural networks

To define drug-likeness, a set of 2136 approved drugs from DrugBank was taken as drug-like, and three negative datasets were selected from ZINC15 (19M), the Network of Organic Chemistry (6M) and ligands from the Protein Data Bank (13k), respectively. The drug dataset was combined with an equal subsampling of the negative dataset for each experiment, using five different molecular representations (Mold2, RDKit, MCS, EXFP4, Mol2Vec). We have re-trained it following the author’s specifications.

## Identifiers

* EOS model ID: `eos9sa2`
* Slug: `bayesian-drug-likeness`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Drug-likeness probability

## References

* [Publication](https://www.nature.com/articles/s42256-020-0209-y)
* [Source Code](https://github.com/Nanotekton/drugability/tree/v0.1)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s42256-020-0209-y) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Non-commercial license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!