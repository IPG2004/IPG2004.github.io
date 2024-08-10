from setuptools import setup, find_packages

setup(
    name='pdf_merger',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'customtkinter',
        'pypdf',
    ],
    entry_points={
        'console_scripts': [
            'pdf_merger = src.app:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A PDF merging tool with a graphical interface.',
    license='MIT',
    keywords='pdf merger tkinter',
)