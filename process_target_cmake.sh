#!/bin/bash

set -euo pipefail
set -x

export PATH=${HOME}/Travail/platform/cmake-3.25.2/bin:$PATH
GTest_ROOT="${HOME}/.conan/data/gtest/1.13.0/_/_/package/e019a06362b932ca5d1b082b6c112aa150c88de4"
project_root=${PWD}

target=${1}
build_type=${2:-Release}
build_dir=builds.cmake/Linux/gcc/10/x86_64/${build_type}

echo "========================"
echo "processing ${target}"
echo "========================"

cd ${target}

echo "________________________________________________"
echo "clean-up"
rm -rf builds.cmake \
	# end of args

git status

echo "press key"
read

echo "________________________________________________"
echo "calling cmake generate"
cmake -S . -B ${build_dir} \
	-D CMAKE_BUILD_TYPE="${build_type}" \
	-D CMAKE_PREFIX_PATH="${project_root}/my_second_lib/${build_dir}/install;${project_root}/my_first_lib/${build_dir}/install" \
	-D GTest_ROOT="${GTest_ROOT}" \
	# end of args
echo "press key"
read

echo "________________________________________________"
echo "calling cmake build"
cmake --build ${build_dir} \
	--target all \
	--target run_unit_tests \
	# end of args
echo "press key"
read

echo "________________________________________________"
echo "calling cmake install"
cmake --install ${build_dir} \
	--prefix ${build_dir}/install \
	--strip \
	# end of args
echo "press key"
read
