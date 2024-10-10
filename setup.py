from setuptools import setup

setup(
    name='commitizen-deno-provider',
    version='0.1.0',
    py_modules=['deno_provider'],
    install_requires=['commitizen'],
    entry_points={
        'commitizen.provider': [
            'deno-provider = deno_provider:DenoProvider',
        ]
    }
)
