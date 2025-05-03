from setuptools import setup, find_packages

setup(
    name="twin_sieve",
    version="0.1.0",
    author="Youcef Hanniche",
    description="A mathematical sieve to generate twin prime numbers based on the form 6k ± 1",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/twin_sieve",  # عدّل لاحقًا إذا نشرت المشروع
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.7',
)
