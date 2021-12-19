from os import path
from traceback import format_exc
from logging import error
from conans import ConanFile, tools
from conans.util.files import save

required_conan_version = ">=1.40.3"


class ConanConfiguration(ConanFile):
    requires = [
        ("gtest/1.11.0", "private")
    ]
    settings = "arch", "os", "compiler", "build_type"
    options = {"type": ["interface", "static", "shared"]}
    generators = "cmake_find_package"

    def set_name(self):
        try:
            self.name = path.basename(path.dirname(path.abspath(__file__)))
        except Exception as e:
            error(format_exc())
            raise e

    def set_version(self):
        try:
            self.version = tools.load(path.join(path.dirname(path.abspath(__file__)), "version.txt")).strip()
        except Exception as e:
            error(format_exc())
            raise e

    def generate(self):
        try:
            filename = 'conan-packages.cmake'
            content = ''

            content += 'set("${PROJECT_NAME}_CONAN_PACKAGE_NAMES"\n'
            for dep_name in self.deps_cpp_info.deps:
                content += '    "' + dep_name + '" \n'
            content += ')\n'

            content += 'set("${PROJECT_NAME}_CMAKE_PACKAGE_NAMES"\n'
            for dep_name, dep in self.deps_cpp_info.dependencies:
                content += '    "' + dep.get_name('cmake_find_package') + '" \n'
            content += ')\n'

            content += 'set("${PROJECT_NAME}_CMAKE_PACKAGE_VERSIONS"\n'
            for dep_name, dep in self.deps_cpp_info.dependencies:
                content += '    "' + dep.version + '" \n'
            content += ')\n'

            content += 'set("${PROJECT_NAME}_CMAKE_PACKAGE_PATHS"\n'
            for dep_name, dep in self.deps_cpp_info.dependencies:
                paths = []
                for build_path in dep.build_paths:
                    cmake_path = build_path.replace('\\', '/')
                    if cmake_path.endswith('/'):
                        cmake_path = cmake_path[:-1]
                    paths.append(cmake_path)
                content += '    "' + '<sep>'.join(paths) + '" \n'
            content += ')\n'

            save(filename, content)
        except Exception as e:
            error(format_exc())
            raise e

    def imports(self):
        try:
            self.copy(pattern="*.dll", dst="bin", src="bin")
            self.copy(pattern="*.dylib", dst="lib", src="lib")
        except Exception as e:
            error(format_exc())
            raise e

    def package_info(self):
        try:
            if self.options.type == "interface":
                self.cpp_info.libs = []
            else:
                self.cpp_info.libs = tools.collect_libs(self)
        except Exception as e:
            error(format_exc())
            raise e


if __name__ == "__main__":
    pass
