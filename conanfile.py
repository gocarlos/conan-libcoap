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
    options = {
        "shared": [True, False],
        "with_openssl": [True, False],
        "with_gnutls": [True, False],
        "with_tinydtls": [True, False],
        "with_epoll": [True, False],
    }
    default_options = {
        "shared": False,
        "with_openssl": True,
        "with_gnutls": False,
        "with_tinydtls": False,
        "with_epoll": False,
    }
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/gocarlos/libcoap.git")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["WITH_OPENSSL"] = self.options.with_openssl
        cmake.definitions["WITH_GNUTLS"] = self.options.with_gnutls
        cmake.definitions["WITH_TINYDTLS"] = self.options.with_tinydtls
        cmake.definitions["WITH_EPOLL"] = self.options.with_epoll
        cmake.configure(source_folder="libcoap")
        return cmake

    def requirements(self):
        if self.options.with_openssl:
            self.requires.add("openssl/1.1.1d")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["coap"]
        self.cpp_info.name = "coap"
