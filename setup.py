from setuptools import setup, find_packages

setup(
    name="simulateur-trafic-ahmed-hamed-2025",
    version="1.0.0",
    description="Un simulateur de trafic routier en Python permettant de modéliser et analyser le flux de véhicules sur un réseau de routes.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Ahmed Hamed",
    author_email="ahmad.hamed.work@gmail.com",
    url="https://github.com/ahmedhdhd/simulateur_trafic",
    install_requires=[
        "matplotlib>=3.5.0",
        "numpy>=1.21.0",
    ],
    entry_points={
        "console_scripts": [
            "simulateur-trafic=simulateur_trafic.main:main",
        ],
    },
    packages=find_packages(include=["simulateur_trafic", "simulateur_trafic.*"]),
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)
