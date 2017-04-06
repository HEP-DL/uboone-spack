# uboone-spack
Microboone Deep Learning Spack Repo Overlay

> NOTE: Work in progress. 

This repo holds the package information for uBooNE's Deep Learning infrastructure.

The below steps setup the relevant software for training and inference using this framework.


## Setup

First, locate a directory that can hold ~5 GB. The following series of commands sets up the repository information and environment variables.


~~~ bash
cd /path/to/big/dir
git clone https://github.com/LLNL/spack.git
cd spack
source share/spack/setup-env.sh
cd var/spack/repos
git clone https://github.com/HEP-SF/hep-spack.git
git clone https://github.com/HEP-DL/uboone-spack.git
cd ../../..
spack repo add var/spack/repos/hep-spack
spack repo add var/spack/repos/uboone-spack
~~~

Whenever starting from a fresh terminal, the following command should be run:

~~~ bash
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


### Setting up LArLite


~~~ bash
spack install larlite%gcc@4.7.4
~~~

> NOTE: Issue with permetis, a.k.a the "metis bomb". One
> One of the dependencies a package called metis is hosted by a site with a bad track record for uptime.
> Fortunately, there are mirrors for this kind of occasion.
> Download metis from the following location: http://pkgs.fedoraproject.org/repo/pkgs/metis/metis-5.1.0.tar.gz/md5/5465e67079419a69e0116de24fce58fe/metis-5.1.0.tar.gz
> Then, move this to the "spack" approved directory structure with `mkdir Downloads/metis; mv Downloads/metis-5.1.0.tar.gz Downloads/metis`.
> Finally, add the download location as a mirror with `spack mirror add metis ~/Downloads`
> Obviously, `Downloads` can be replaced with a better location, but for these purposes, this works.


### Setting up caffe

~~~ bash
spack install caffe%gcc@4.7.4 ^opencv@3.2.0 +shared +python
~~~
