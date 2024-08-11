from setuptools import setup, find_packages

setup(
    name="authentication_system",
    version="1.0.0",
    author="IPG2004",
    author_email="your-email@example.com",
    description="An authentication system using facial recognition and password authentication.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/IPG2004/Authentication-System",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "customtkinter",
        "opencv-python",
        "bcrypt",
    ],
    entry_points={
        'console_scripts': [
            'authentication_system=src.app:main',
        ],
    },
    license='MIT',
    keywords='face recognition login register tkinter',
)