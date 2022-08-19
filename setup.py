from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'Hypixel SkyBlock Weight Calculator.'

# Setting up
setup(
    name="lilyweight",
    version=VERSION,
    author="timnoot",
    author_email="<hypixelskyhub@gmail.com>",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['aiohttp'],
    keywords=['python', 'hypixel', 'skyblock', 'lily weight', 'weight', 'lappysheep', "lilly"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
    package_data={'lilyweight': ['lilyweight/calcs/*']}
)
