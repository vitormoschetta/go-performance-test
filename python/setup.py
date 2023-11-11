from setuptools import find_packages, setup

setup(
    name='MyApp',
    version='0.1.0',
    packages=find_packages(),
    url='http://localhost:7000',
    license='',
    author='vitormoschetta',
    description='API for example',
    keywords=['python', 'teste', 'api'],
    # Os pacotes abaixo são instalados quando for executado 'pip install setup.py'
    install_requires=[
        'fastapi',                          # Framework para construir APIs
        'uvicorn',                          # Servidor http local
        'pydantic',                         # Serve para mapear objetos nos requests?
    ]
)