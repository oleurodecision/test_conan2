from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import load, update_conandata
from conan.tools.scm import Git

from inspect import getsourcefile

import os
import re

class MyFirstLibCppConan(ConanFile):
    package_type = "library"
    #description = None
    #homepage = None
    #url = None
    #license = None
    #author = None
    #topics = None
    #user, channel = None, None
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
        }
    default_options = {
        "shared": False,
        "fPIC": True
    }
    #options_description = 
    #build_policy = # can be never, missing, always
    #upload_policy =
    no_copy_source = True
    #source_folder =
    #export_source_folder =
    #build_folder =
    #package_folder = "install"
    #recipe_folder =
    #removed ? short_paths = True
    #python_requires =
    #python_requires_extend =
    #deprecated =
    #provides =
    #win_bash =

    def _get_infos(self):
        try:
            # TODO how should we do better than this ?
            recipe_root = os.path.dirname(getsourcefile(lambda:0))
            content = load(self, os.path.join(recipe_root, "CMakeLists.txt"))
            infos = re.search(r"project\s*\(\s*(\w+)\s*\bVERSION\s*(\d+(\.\d+)*)", content, re.DOTALL)
            name = infos.group(1).strip()
            version = infos.group(2).strip()
            return name, version
        except Exception:
            return None,None

    #def init(self):
    #    self.output.warning("=== init")

    def set_name(self):
        self.output.warning("=== set_name")
        self.name = self._get_infos()[0]

    def set_version(self):
        self.output.warning("=== set_version")
        self.version = self._get_infos()[1]

    def export(self):
        self.output.warning("=== export")
        git = Git(self, self.recipe_folder)
        scm_url, scm_commit = git.get_url_and_commit()
        # we store the current url and commit in conandata.yml
        update_conandata(self, {"sources": {"commit": scm_commit, "url": scm_url}})

    #def export_sources(self):
    #    self.output.warning("=== export_sources")

    # init is called again when doing some conan create .

    def config_options(self):
        self.output.warning("=== config_options")
        if self.settings.os == "Windows":
            del self.options.fPIC

    #def configure(self):
    #    self.output.warning("=== configure")

    def layout(self):
        self.output.warning("=== layout")
        #cmake_layout(self)
        self.output.warning(f"*** source_folder {self.source_folder}")
        self.output.warning(f"*** export_sources_folder {self.export_sources_folder}")
        self.output.warning(f"*** build_folder {self.build_folder}")
        self.output.warning(f"*** package_folder {self.package_folder}")
        self.output.warning(f"*** recipe_folder {self.recipe_folder}")

        build_dir = os.path.join("builds", str(self.settings.os), str(self.settings.compiler), str(self.settings.compiler.version), str(self.settings.arch), str(self.settings.build_type))
        self.output.warning(f"*** build_dir {build_dir}")

        #package_dir = os.path.join(build_dir, "install")

        cmake_config_path = os.path.join("lib", "cmake", f"{self.name}-{self.version}")
        self.output.warning(f"*** cmake_config_path {cmake_config_path}")

        ## set folders
        ##self.folders.source = ""
        self.folders.build = build_dir
        self.folders.generators = os.path.join(build_dir, "generators")
        ## removed ? self.folders.imports
        ##self.folders.root = None

        ## set cpp package information for package consumption
        ## see also package_info() and self.cpp_info
        self.cpp.package.libs = ["my_first_lib"]
        ##self.cpp.package.bindirs = ["bin"]
        ##self.cpp.package.libdirs = ["lib"]
        ##self.cpp.package.includedirs = ["include"]
        self.cpp.package.builddirs = [cmake_config_path]

        ## set cpp source and build information for editable consumption
        #self.cpp.source.includedirs = ["src/my_first_lib/include"]

        #self.cpp.build.includedirs = [os.path.join(package_dir, "include")]
        #self.cpp.build.libs = ["my_first_lib"]
        #self.cpp.build.libdirs = [os.path.join(package_dir, "lib")]
        self.cpp.build.builddirs = [os.path.join("install", cmake_config_path)]

    #def requirements(self):
    #    self.output.warning("=== requirements")

    #def package_id(self):
    #    self.output.warning("=== package_id")

    def validate(self):
        self.output.warning("=== validate")
        check_min_cppstd(self, "14")

    #def validate_build(self):
    #    self.output.warning("=== validate_build")

    def build_requirements(self):
        self.output.warning("=== build_requirements")
        #self.build_requires()
        #self.test_requires("gtest/1.13.0")

    #def build_id(self):
    #    self.output.warning("=== build_id")

    def source(self):
        self.output.warning("=== source")
        git = Git(self)
        sources = self.conan_data["sources"]
        git.clone(url=sources["url"], target=".")
        git.checkout(commit=sources["commit"])

    def generate(self):
        self.output.warning("=== generate")
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    # removed ?
    #def imports(self):
    #    self.output.warning("=== imports")
    #    self.copy("*.dll", dst="bin", src="bin")

    def build(self):
        self.output.warning("=== build")
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        #cmake.test(target="unit_tests")

    def package(self):
        self.output.warning("=== package")
        self.output.warning(f"*** source_folder {self.source_folder}")
        self.output.warning(f"*** export_sources_folder {self.export_sources_folder}")
        self.output.warning(f"*** build_folder {self.build_folder}")
        self.output.warning(f"*** package_folder {self.package_folder}")
        self.output.warning(f"*** recipe_folder {self.recipe_folder}")
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.output.warning("=== package_info")
        self.cpp_info.set_property("cmake_find_mode", "none")

    # undefined order

    #def system_requirements(self):
    #    self.output.warning("=== system_requirements")

    #def compatibility(self):
    #    self.output.warning("=== compatibility")

    #def deploy(self):
    #    self.output.warning("=== deploy")

