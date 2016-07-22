from conans import ConanFile

class glmConan(ConanFile):
    name = "glm"
    version = "0.9.7.6"
    license = "The Happy Bunny License, or the MIT License"
    url = "https://github.com/dlarudgus20/conan-glm"

    def source(self):
        self.run("git clone https://github.com/g-truc/glm --branch 0.9.7.6 --depth 1")

    def package(self):
        self.copy("*", dst="include/glm", src="glm/glm")
