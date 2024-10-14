cz bump 
python3 -m build --sdist
python3 -m build --wheel
twine upload dist/commitizen_deno_provider-$(cz version -p)*