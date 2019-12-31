from conans import ConanFile, CMake, tools


class LibcoapConan(ConanFile):
    name = "libcoap"
    version = "4.3.0"
    license = "BSD"
    author = "Carlos Gomes Martinho kmartinho8@gmail.com"
    url = "https://github.com/obgm/libcoap/issues"
    description = "A CoAP (RFC 7252) implementation in C"
    topics = ("coap")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/gocarlos/libcoap.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="libcoap")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*libcoap.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libcoap"]

