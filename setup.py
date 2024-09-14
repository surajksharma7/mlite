from setuptools import setup, find_packages

setup(
    name='mlite',  # Name of the library
    version='0.0.2',  # Version of the library
    description='A lightweight machine learning library with linear regression functionality',  # Short description
    author='Suraj Kumar Sharma',  # Your name or organization
    author_email='surajksharma2304@gmail.com',  # Your email address
    license='MIT',  # License for the project
    packages=find_packages(),  # Automatically finds all packages inside the directory
    install_requires=[
        'numpy',  # Dependencies required for your library
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
