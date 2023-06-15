FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.3.1b1
RUN conda install scikit-learn=0.21.2
RUN pip install tensorflow==1.13.2
RUN pip install keras==2.2.4
RUN pip install imbalanced-learn==0.4.3
RUN pip install git+https://github.com/samoturk/mol2vec
RUN pip install PyYAML==5.2
RUN pip install gensim==3.8.3

WORKDIR /repo
COPY . /repo
