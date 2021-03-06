from setuptools import find_packages, setup


def readme():
    with open("README.md") as f:
        return f.read()


# read version file
exec(open("alibi_detect/version.py").read())

extras_require = {"examples": ["seaborn", "tqdm"]}

setup(
    name="alibi-detect",
    author="Seldon Technologies Ltd.",
    author_email="hello@seldon.io",
    version=__version__,  # type: ignore # noqa F821
    description="Algorithms for outlier detection, concept drift and metrics.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SeldonIO/alibi-detect",
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">3.5.1",
    setup_requires=["pytest-runner"],
    install_requires=[
        "creme",
        "fbprophet",
        "matplotlib",
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "tensorflow>=2",
        "tensorflow_probability>=0.8"
    ],
    tests_require=["pytest", "pytest-cov"],
    extras_require=extras_require,
    test_suite="tests",
    zip_safe=False,
)
