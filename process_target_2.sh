#!/bin/bash

set -euo pipefail

target=${1}
build_type=${2:-Release}
build_dir=builds/Linux/gcc/10/x86_64/${build_type}

export PATH=~/Travail/platform/cmake-3.25.2/bin:$PATH

echo "========================"
echo "processing ${target}"
echo "========================"

cd ${target}

echo "________________________________________________"
echo "clean-up"
rm -rf build/ builds/ builds.cmake/ \
	conanbuildinfo.txt conaninfo.txt conan.lock graph_info.json \
	include/ lib/ bin/ install/ \
	CMakeUserPresets.json \
	# end of args

git status

echo "press key"
read

echo "________________________________________________"
echo "calling conan install"
conan install . \
	-pr:b gcc-10 \
	-pr:h gcc-10 \
	-s build_type=${build_type} \
	#--update --build outdated \
	#--build=missing \
	# end of args
echo "press key"
read

echo "________________________________________________"
echo "calling conan build"
conan build . \
	-pr:b gcc-10 \
	-pr:h gcc-10 \
	# end of args
echo "press key"
read

if `conan editable list | fgrep -q ${target}`
then
	echo "________________________________________________"
	echo "calling cmake install"
	cmake --install ${build_dir} \
		--prefix ${build_dir}/install \
		--strip \
		# end of args
else
	echo "________________________________________________"
	echo "calling conan export-pkg"
	conan export-pkg .  \
		-pr:b gcc-10 \
		-pr:h gcc-10 \
		#--output-folder ${build_dir} \
		#-s build_type=${build_type} \
		# end of args
fi

echo "press key"
read
