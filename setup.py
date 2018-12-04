from setuptools import setup

long_description = open('README.md').read()

setup(
    name="py-media-id-parser",
    version='0.0.1',
    packages=["media_id_parser"],
    include_package_data=True,
    description="A simple library to return media or post ID's from various social links",
    url="https://github.com/corneliusiv/py-media-id-parser",
    author="Cornelius Hairston",
    author_email="cornelius.hairston@gmail.com",
    license='MIT',
    install_requires=[
        'requests>=2.21,<2.20',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=["any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
