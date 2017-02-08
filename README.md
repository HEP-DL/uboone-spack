# uboone-spack
Microboone Spack Repo Overlay

> NOTE: Work in progress. 

This repo holds the package information for uBooNE's Deep Learning infrastructure.

The below steps setup the relevant software for training and inference using this framework.


## Setup

First, locate a directory that can hold ~5 GB. The following series of commands sets up the repository information and environment variables.


~~~ bash
cd /path/to/big/dir
git clone https://github.com/LLNL/spack.git
cd spack
export PATH=$PATH:$(pwd)/bin
source share/spack/setup-env.sh
cd spack/var/spack/repos
git clone https://github.com/HEP-SF/hep-spack.git
git clone https://github/com/HEP-DL/uboone-spack.git
spack repo add spack/var/spack/repos/hep-spack
~~~

Whenever starting from a fresh terminal, the following commands should be run:


~~~ bash
export PATH=$PATH:<path to spack>/bin
source <path to spack>/share/spack/setup-env.sh
~~~

### Setting up Environment Modules

Modules installed by Spack are natively handled by `LMod` or `Environment Modules`. Since these are readily available on HPC platforms, documentation on setting these up is scarce.

For deployment on non-HPC platforms such as laptops, the following command sets up `Environment Modules.`

~~~ bash
spack install environment-modules
~~~

Now, in order to use `module`, the following lines need to be run from a shell script or (usually) inserted into your `bashrc` or `bash_profile`.

~~~ bash
case "$0" in
          -sh|sh|*/sh)  modules_shell=sh ;;
       -ksh|ksh|*/ksh)  modules_shell=ksh ;;
       -zsh|zsh|*/zsh)  modules_shell=zsh ;;
    -bash|bash|*/bash)  modules_shell=bash ;;
esac
module() { eval `$(find <path to spack> -name modulecmd) $modules_shell $*`; }
~~~

Where, `<path to spack>` should be replaced with the path to spack.


### Setting up LLVM

ROOT is picky about which compiler it uses (for CLING). Issue the following command.

~~~ bash
spack install llvm@3.9.1
~~~

This takes quite some time. This module can used by issuing the command

~~~ bash
spack load llvm@3.9.1
~~~

### Setting up ROOT

ROOT now needs to be setup with the dependency on the correct compiler

~~~ bash
spack install root@6.06.08%llvm@3.9.1
~~~

> WARNING: Watch out for errors of the form:
> ~~~
>curl: (56) Recv failure: Connection reset by peer
==> Fetching from http://ftp.gnu.org/gnu/gcc/gcc-4.9.3/gcc-4.9.3.tar.bz2 failed.
==> Error: FetchError: All fetchers failed for gcc-4.9.3-v5qnhblyippvancig6ax7trapncbmdj2
> ~~~
> The network timeout for spack is set to a hair trigger. Just re-run the install commands, and it should work.

Similarly, this can be loaded with the `spack load` command.


### Starting up LArLite


~~~ bash
spack install larlite%gcc@4.9.4
~~~