from setuptools import setup, find_packages

setup(name='pyv1',
      version='0.0.3',
      description='This tool is created to help everyday work with KONE VersionOne Agile portfolio and project management tool',
      url='http://kcofilxkqd001:8888/Henkka/pyv1',
      author='Henri Wenlin',
      author_email='henri.wenlin@kone.com',
      license='Private, internal software',
      packages=find_packages(),
      package_data = {"": ["*.ipynb"],},
      install_requires=[
      "wheel>=0.35.1",      
      "requests>=2.25.0",
      "keyring >= 23.1.0",
      "pandas >= 1.3.2",
      "notebook >= 6.4.3",
      "jupyter-wysiwyg >= 19.10",
      ],
      classifiers=['Programming Language :: Python :: 3'],
      zip_safe=False)
