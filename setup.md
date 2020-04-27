# Set up

* Download the project:

```
git clone https://github.com/evgenyneu/asp3231_project.git
```

* Change working directory:

```
cd asp3231_project
```

* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

* Create a Conda environment:

```
conda create --name obsastro2020 python=3.7
```

* Activate the environment:

```
conda activate obsastro2020
```

* Install Python libraries listed in `requirements.txt` file:

```
pip install -r requirements.txt
```

### Cleaning up

When you finished running the code, stop Jupyter with <Ctrl-C> and remove the Conda environment:

```
conda deactivate
conda env remove -n obsastro2020
```
