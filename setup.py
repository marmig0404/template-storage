from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='template-store',
    version='0.1.0',
    description='Turn STL files into voxels, images, and videos',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license='GNU GPLv3',
    keywords='stl python voxel',
    author='Christian Pederkoff',
    url='https://github.com/marmig0404/template_store',
    download_url='https://github.com/marmig0404/template_store/releases',
    install_requires=['Pillow'],
    packages=['templatestore'],
    python_requires='>=3',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'templatestore = templatestore.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)