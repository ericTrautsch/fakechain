# fakechain
a spiritual successor to langchain. build chains to query small language models

## Getting Started

Install the latest from `test.pypi.org`

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ --force-reinstall fakechain
```


## Publishing

Ensure version number is incremented. 

Publishing to `test.pypi.org`
```
poetry publish --build --no-cache -r test-pypi
```

### References/Technologies

1. Python Poetry [https://python-poetry.org/](Python Poetry)
