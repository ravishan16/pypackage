from setuptools import setup, find_packages

setup(name='helloworldcli',
      author='Ravishankar Sivasubramaniam',
      author_email='ravi_siva@live.com',
      version='0.0.1',
      description='Hello World Cli',
      py_modules=['helloworldcli'],
      ext_modules=[],
      packages=find_packages(),
      install_requires=['Click'],
      entry_points='''
        [console_scripts]
        helloworldcli=helloworld:hello
    ''',
      python_requires='>=3.6'
      )