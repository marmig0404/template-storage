from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='template-storage',
    version='0.1.3',
    description='A module that compresses template images into a store.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license='GNU GPLv3',
    keywords='storage python template compression',
    author='Martin Miglio',
    url='https://github.com/marmig0404/template_storage',
    download_url='https://github.com/marmig0404/template_storage/releases',
    install_requires=['Pillow'],
    packages=['templatestorage'],
    python_requires='>=3',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'templatestorage = templatestorage.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
