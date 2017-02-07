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
