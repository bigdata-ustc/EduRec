from setuptools import setup

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-flake8',
]

setup(
    name='EduRec',
    version='0.0.1',
    extras_require={
        'test': test_deps,
    },
    install_requires=[
        "EduSim>=0.1.0"
    ],  # And any other dependencies foo needs
    entry_points={
    },
)
