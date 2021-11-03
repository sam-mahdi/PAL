To install in a virtual environment:
```
python3 -m venv env
source env/bin/activate
```
Then move the PAL folder into your env directory. 

Navigate to the PAL directory

```
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
```

Note, pymol will not install and cause an error (cannot run pymol in the virtual env). 

To run: 

```
python3 PAL.py
```
