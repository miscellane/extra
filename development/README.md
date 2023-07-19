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

Open `profile`, i.e.,

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

Next,

```shell
  conda init bash
  conda config --set auto_activate_base false
  sudo chown -R $USER:$USER /opt/miniconda3

```

<br>
<br>

## NVIDIA

In terms of installing  `cudatoolkit` & `cuDNN` within a WSL (Windows Subsystem for Linux) operating system, the a probable approach is

```shell
  conda activate base
  conda install -c anaconda cudatoolkit=11.8.0
  python -m pip install nvidia-cudnn-cu11==8.6.0.163 
```

Beware of the `base` installation.  Then

```shell
  mkdir -p /opt/miniconda3/etc/conda/activate.d

  echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' 
    >> /opt/miniconda3/etc/conda/activate.d/env_vars.sh

  echo 'export LD_LIBRARY_PATH=/opt/miniconda3/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH' 
    >> /opt/miniconda3/etc/conda/activate.d/env_vars.sh
```

Is `CONDA_PREFIX='/opt/miniconda3'` a sensible option?  Subsequently, run

```shell
  source /opt/miniconda3/etc/conda/activate.d/env_vars.sh
```

<br>
<br>

## git

```shell
  git config --global user.name ""
  git config --global user.email "...@users.noreply.github.com"
  git config --global core.editor ""

  ssh-keygen -t ed25519 -C "...@users.noreply.github.com"

  cat ~/.ssh/id_ed25519.pub
```

<br>
<br>

## docker

Uninstall packages

```bash
  for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

```bash
  sudo apt-get update
  sudo apt-get install ca-certificates curl gnupg
```

```bash
  sudo install -m 0755 -d /etc/apt/keyrings
  wget https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  sudo chmod a+r /etc/apt/keyrings/docker.gpg
```


<br> 
<br>

<br> 
<br>

<br> 
<br>

<br> 
<br>
