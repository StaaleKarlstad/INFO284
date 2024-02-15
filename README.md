# INFO284
NFO284-Group exam

## Project setup

To setup the project, we need to create a virutal environment, install the required dependencies and instantiate the kernel.

1. Open the project root directory in a CLI, first create a virtual environment:

```ps
python -m venv venv
```

2. Activate the virtual environment:

Windows:

```ps
.\venv\Scripts\activate
```

Mac / linux:

```
source venv/bin/activate
```

3. Install the project dependencies:

```ps
pip install -r requirements.txt
```

4. Activate the kernel:

```ps
python -m ipykernel install --user --name=venv
```

Now you can open Jupyter Lab/Notebook. Select venv as kernel when running the code.
