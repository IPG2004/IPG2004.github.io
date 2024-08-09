from setuptools import setup, find_packages

setup(
    name="youtube_downloader",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "customtkinter",
        "pytubefix",
    ],
    entry_points={
        'console_scripts': [
            'youtube_downloader=app:main',
        ],
    },
)
