from setuptools import setup

setup_path = os.path.dirname(__file__)
reqs_file = open(os.path.join(setup_path, 'requirements.txt'), 'r')
reqs = reqs_file.readlines()
reqs_file.close()

setup(
    name='keen-csv',
    version='1.0.0',
    install_requires=reqs,
    packages=['keen-csv']
)
