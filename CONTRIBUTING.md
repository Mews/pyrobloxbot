# Contributing to pyrobloxbot

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Refer this project in your project's readme if you use it
> - Share it with other people


## Code Contributions

To setup your development environment, you're gonna want to create a virtual environment, and install the package in editable mode, as well as the dev dependencies.
```shell
cd pyrobloxbot
python -m venv venv
.\venv\Scripts\activate
pip install -e . --group dev  (you might need to update pip to do this)
```

You're also required to install the pre-commit hooks, using:
```shell
pre-commit install
pre-commit install --hook-type pre-push
```

After this, you can create a new branch on your fork and commit your changes to it.
Once you're done, you can create a [pull request](https://github.com/Mews/pyrobloxbot/pulls).

Make sure to follow the pull request template, and a maintainer will review it and merge it into the project.

## Improving The Documentation
> This section is a work in progress...

You'll need to install the dependencies for building the docs, using:
```shell
pip install --group docs
```

Then, build the docs by running the following command from the `docs` folder
```shell
.\make html
```

Make sure there are no warnings when building!
