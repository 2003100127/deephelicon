from setuptools import setup, find_packages

setup(
    name="deephelicon",
    version="0.0.1",
    keywords=["pip", "deephelicon"],
    description="deephelicon",
    long_description="transmembrane protein helical residue-residue contact prediction",
    license="GPL-3.0",

    url="https://github.com/2003100127/deephelicon",
    author="Jianfeng Sun",
    author_email="jianfeng.sunmt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>=3.11,<4',
    install_requires=[
        'numpy==2.1.3',
        'tensorflow==2.19',
        'pandas==2.2.3',
        'joblib==1.4.2',
        'biopython',
        'pyfiglet',
        'click',
        'numba', # EVCouplingsModel
    ],
    entry_points={
        'console_scripts': [
            'deephelicon_s1=deephelicon.predict:rrc_s1',
            'deephelicon_s2=deephelicon.predict:rrc_s2',
            'deephelicon_fmt=deephelicon.predict:op_format',
            'deephelicon_download=deephelicon.predict:download',
        ],
    }
)