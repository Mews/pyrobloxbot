# Contributing to pyrobloxbot

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help out. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for maintainers and smooth out the experience for all involved. We all look forward to your contributions! 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Refer this project in your project's readme if you use it
> - Share it with other people

## Table of Contents

- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Improving The Documentation](#improving-the-documentation)



## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://pyrobloxbot.readthedocs.io/en/latest/).

Before you ask a question, it is best to search for existing [Issues](https://github.com/Mews/pyrobloxbot/issues) that might help you. In case you have found a suitable issue and still need clarification, you can then post a new issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [issue](https://github.com/Mews/pyrobloxbot/issues/new?labels=question).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions, depending on what seems relevant.

We will then take care of the issue as soon as possible.

Make sure to pay attention to any activity in any issues you create, so as to make taking care of them as fast as possible.

## I Want To Contribute

> ### Legal Notice
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project licence.

### Reporting Bugs

#### How Do I Submit a Good Bug Report?

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be reported thorugh [security advisories](https://github.com/mews/pyrobloxbot/security/advisories/new).

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://pyrobloxbot.readthedocs.io/en/latest/). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- See if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/Mews/pyrobloxbot/issues?q=label%3Abug%20is%3Aissue).
- Collect information about the bug:
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Python version
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

Once you have done this:

- Open a [bug issue](https://github.com/mews/pyrobloxbot/issues/new?template=bug.yml).
- Follow the issue template and include all the information you could gather

Once it's filed, a maintainer will look at it, try to reproduce it, and decide the best course of action.


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for pyrobloxbot, **including completely new features and minor improvements to existing functionality**.

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://pyrobloxbot.readthedocs.io/en/latest/) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/Mews/pyrobloxbot/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature.

#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/Mews/pyrobloxbot/issues).

To submit a feature request:
- Create an issue using the [feature request template](https://github.com/mews/pyrobloxbot/issues/new?template=feature.yml).
- Make sure to follow the template and describe your feature in detail
- Add all the information that might be relevant to your request


### Your First Code Contribution
The first thing you'll need to do is [fork the repository](https://github.com/Mews/pyrobloxbot/fork). This will create a copy of the repository in your account, which you can edit.

Next, you'll need to clone the repository to your machine, either with
```shell
git clone https://github.com/yourusername/pyrobloxbot.git
```
or, if you have an SSH key set up,
```shell
git clone git@github.com: yourusername/pyrobloxbot.git
```

Next, you can set up a virtual environment and install the project dependencies
```shell
cd pyrobloxbot
python -m venv venv
.\venv\Scripts\activate
pip install -e . --group dev  (you might need to update pip to do this)
```

You're also required to install the pre-commit hooks, using:
```shell
pre-commit install
```

After this, you can create a new branch and commit your changes to it.
Once you're done, you can create a [pull request](https://github.com/Mews/pyrobloxbot/pulls).

Make sure to follow the pull request template, and a maintainer will review it and merge it into the project.

### Improving The Documentation
> This section is a work in progress...

You'll need to install the dependencies for building the docs, using:
```shell
pip install --group docs
```

## Attribution
This guide is based on the [contributing.md](https://contributing.md/generator)!
