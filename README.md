# NEMES 2026 fNIRS workshop
Anatomical registration and analysis pipeline for NEMES 2026.

This tutorial will go though:
- Forward modelling of software-defined montage
- Photogrammetric optode co-registration
- Forward modelling of registered montage

## Preparing Python

The notebook is run in Python 3.11.

Environment and Python is handled by `uv`

MacOS, via [Homebrew](https://brew.sh):

~~~
brew install uv
~~~

Windows, via [WinGet](https://github.com/microsoft/winget-cli):

~~~
winget install --id=Astral-sh.uv

or just via powershell

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
~~~

Linux:

~~~
curl -LsSf https://astral.sh/uv/install.sh | sh
~~~

Install Python 3.11:

~~~
uv python install 3.11
~~~

## Installing dependencies

MacOS / Linux:

~~~
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt
~~~

Windows:

~~~
uv venv --python 3.11
.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
~~~

## Installing Cedalion

We will be using the `dev` branch of the toolbox which has some neat unreleased features. You might want to stick to `main` for stability however.

Download the [Cedalion GitHub repository](https://github.com/ibs-lab/cedalion)

~~~
git clone https://github.com/ibs-lab/cedalion.git
cd cedalion
git checkout dev
cd ..
~~~

.. or just switch branch from `main`to `dev` -> press `Code` -> `Download Zip` and unzip it in this folder.

To allow for photon simultation and forward modelling without a CUDA-enabled GPU, we will use the [micro (fast and furious) version of NIRFASTer](https://github.com/milabuob/nirfaster-uFF).

See [Cedalion docs for preparing NIRFASTer](https://doc.ibs.tu-berlin.de/cedalion/doc/dev/dot/_autosummary_dot/cedalion.dot.forward_model.html):

> NOTE: Cedalion currently supports two ways to compute fluence: 1) via monte-carlo simulation using the MonteCarloXtreme (MCX) package, and 2) via the finite element method (FEM) using the NIRFASTer package.

> While MCX is automatically installed using pip, NIRFASTER has to be manually installed runnning <$ bash install_nirfaster.sh CPU # or GPU> from a within your cedalion root directory.

So we will install it first:

~~~
cd cedalion
./install_nirfaster.sh CPU
uv pip install -e .
cd ..
~~~

## Running the notebook

~~~
cd tutorial
jupyter notebook
~~~
