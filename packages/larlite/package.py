##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install larlite
#
# You can edit this file again by typing:
#
#     spack edit larlite
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import subprocess
import shutil
import os


class Larlite(Package):
  homepage = "https://github.com/larlight/larlite"
  url      = "https://github.com/larlight/larlite/archive/v06_20_00.tar.gz"

  version('06_20_00', 'd5a5788e01cddf57d0b197188ab14847')
  depends_on('llvm@3.9.1')
  depends_on('root@6.06.08%llvm@3.9.1')
  
  def setup_environment(self, spack_env, run_env):
    with working_dir(self.prefix):
        command = ['bash', '-c', 'source config/setup.sh']
        proc = subprocess.Popen(command)

  def setup_dependent_environment(self, spack_env, run_env, dspec):
    with working_dir(self.prefix):
        command = ['bash', '-c', 'source config/setup.sh']
        proc = subprocess.Popen(command)

  def install(self, spec, prefix):
    mkdirp(prefix)
    src_dir = os.getcwd()
    files_to_move =os.listdir(src_dir)
    for _file in files_to_move:
      if os.path.isdir(_file):
        shutil.copytree(os.path.join(src_dir,_file), os.path.join(prefix, _file))
      else:
        shutil.copy(os.path.join(src_dir,_file), os.path.join(prefix, _file))
    #os.chdir(prefix)
    with working_dir(prefix):
        command = ['bash', '-c', 'source config/setup.sh']
        proc = subprocess.Popen(command)
        make()
    #os.chdir(src_dir)
