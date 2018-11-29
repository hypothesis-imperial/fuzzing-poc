from setuptools import setup

INSTALL_REQUIRES = []
EXTRAS_REQUIRE = {
    "docs": ["sphinx", "zope.interface"],
    "tests": [
        "coverage",
        "hypothesis",
        "pympler",
        "pytest",
        "six",
        "zope.interface",
    ],
}

if __name__ == "__main__":
    setup(
        name='sample-product-poc',
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
    )