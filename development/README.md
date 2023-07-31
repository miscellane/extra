<br>

**LINUX**


<br>

## IntelliJ IDEA

```shell
  # get
  sudo wget -P Downloads https://download.jetbrains.com/idea/ideaIC-2022.3.3.tar.gz
  sudo tar -xzf ideaIC-2022.3.3.tar.gz -C /opt 

  # starting within idea bin
  cd .../bin
  ./idea.sh
```

<br>
<br>

## miniconda

Foremost, check the python version

```shell
  python --version
```


<br>


### get

Subsequently, `get` the [installer](https://docs.conda.io/en/latest/miniconda.html#linux-installers) relative to the system's python version, e.g.,

```shell
  # if python 3.10.*
  sudo wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
  cd Downloads
  sudo chmod +x Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
```


<br>


### Install

Install in the specified directory

```shell
  # Include <-b> for automatic acceptance of the terms & conditions
  sudo bash Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -p /opt/miniconda3

  $ Do you wish the installer to initialize Miniconda3 by running conda init?
  >>> no
```


<br>


### Path Variable

Open `/etc/profile`, i.e.,

```shell
  sudo vi profile
```

and append

```bash
if ! [[ $PATH =~ "/opt/miniconda3/bin" ]]; then
	PATH="/opt/miniconda3/bin:$PATH"
fi
```

The command `i` starts the edit mode, `ESC` exits the mode, and `:wq` saves; [`vi` commands](https://www.cs.colostate.edu/helpdocs/vi.html).  **Exit** the terminal.


<br>


### Set-up

Next, within a new terminal

```shell
  conda init bash
  conda config --set auto_activate_base false
  sudo chown -R $USER:$USER /opt/miniconda3
```

<br>
<br>

## NVIDIA CUDA: A sample Tensorflow/<abbr>GPU</abbr> virtual environment

Foremost, a virtual conda environment for tensorflow - within a WSL (Windows Subsystem for Linux) operating system ...

```shell
conda create --prefix /opt/miniconda3/envs/tensors python=3.11
```

Next, activate the environment then inspect ...

```shell
conda activate tensors
python -m pip list
conda list
```

Next, the core/background installations for tensorflow ... `cudatoolkit` & `cuDNN`

```shell
conda install -c conda-forge cudatoolkit=11.8.0
pip install nvidia-cudnn-cu11==8.6.0.163
```

... hence, the setting-up of their path variables

```shell
# ascertain that this variable has a value
echo $CONDA_PREFIX

# subsequently
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

Now, **install `tensorflow`**

```shell
pip install tensorflow==2.12.*
```

Perhaps [TensorRT](https://www.tensorflow.org/install/pip#windows-wsl2:~:text=improve%20latency%20and%20throughput%20for%20inference)

```shell
pip install --upgrade tensorrt
```

The upcoming sample project depends on ...

```shell
pip install "dask[complete]"
pip install scikit-learn
pip install pytest coverage pylint pytest-cov flake8
```

<br>
<br>

## GIT

```shell
  git config --global user.name ""
  git config --global user.email "...@users.noreply.github.com"
  git config --global core.editor "vim --nofork"
  git config --global init.defaultBranch master

  ssh-keygen -t ed25519 -C "...@users.noreply.github.com"

  cat ~/.ssh/id_ed25519.pub
```

<br>
<br>

## Docker

Foremost, uninstall docker within each WSL (Windows Subsystem for Linux) operating system that will be associated with Docker Desktop

```shell
  for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

[This avoids conflicts](https://docs.docker.com/desktop/wsl/#:~:text=To%20avoid%20any%20potential%20conflicts).



<br> 
<br>

<br> 
<br>

<br> 
<br>

<br> 
<br>
