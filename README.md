# uboone-spack
Microboone Spack Repo Overlay

> NOTE: Work in progress. 

~~~ bash
cd /path/to/big/disk
git clone https://github.com/LLNL/spack.git
cd spack/var/spack/repos
git clone https://github.com/HEP-SF/hep-spack.git
cd -
./spack/bin/spack compiler add /usr/bin/gcc
./spack/bin/spack repo add spack/var/spack/repos/hep-spack
~~~


~~~ bash
source spack/share/spack/setup-env.sh
~~~


~~~ bash
spack install gcc@4.9.3
spack install root@6.06.08%gcc@4.9.3
~~~

~~~ bash
case "$0" in
          -sh|sh|*/sh)  modules_shell=sh ;;
       -ksh|ksh|*/ksh)  modules_shell=ksh ;;
       -zsh|zsh|*/zsh)  modules_shell=zsh ;;
    -bash|bash|*/bash)  modules_shell=bash ;;
esac
module() { eval `$(find <path to spack> -name modulecmd) $modules_shell $*`; }
~~~
