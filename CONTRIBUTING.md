# Contributing

### Run tests

```bash
python setup.py test
```

### Build Sphinx documentation

```bash
python setup.py build_sphinx
```

### Releases

Please create new releases via GitHub's release functionality or using the
GitHub CLI.

```bash
hub release create origin <version_number>
```

We follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

Make sure to add the changelog of each release into the release description.
