<br>

**LINUX**


<br>

### IntelliJ IDEA

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

### miniconda

Foremost, check the python version

```shell
  python --version
```

Subsequently, `get` the [installer](https://docs.conda.io/en/latest/miniconda.html#linux-installers) relative to the system's python version, e.g.,

```shell

  # if python 3.10.*
  sudo wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
  cd Downloads
  sudo chmod +x Miniconda3-py310_23.5.2-0-Linux-x86_64.sh

  # either
  # sudo bash Miniconda3-py310_23.5.2-0-Linux-x86_64.sh  -p /opt/miniconda3
  # sudo bash Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -b  -p /opt/miniconda3
  sudo bash Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -b  -p /opt/miniconda3

```




<br> 
<br>

<br> 
<br>

<br> 
<br>

<br> 
<br>
