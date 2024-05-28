from setuptools import setup, find_packages

setup(
    name='trend_data',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'metrics @ git+https://github.com/BobryTeam/metrics.git@pip-deps'
    ],
    author='BobryTeam',
    author_email='sinntexxx@gmail.com',
    description='TrendData data structure',
    url='https://github.com/BobryTeam/trend-data',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
