# Contributing Guidelines

Thank you for your interest in contributing to our project. Whether it's a bug report, new feature, correction, or additional
documentation, we greatly value feedback and contributions from our community.

Please read through this document before submitting any issues or pull requests to ensure we have all the necessary
information to effectively respond to your bug report or contribution.

## Reporting Bugs/Feature Requests

We welcome you to use the GitHub issue tracker to report bugs, suggest features, or documentation improvements.

When filing an issue, please check existing open, or recently closed, issues to make sure somebody else hasn't already
reported the issue. Please try to include as much information as you can.


## Releases

First you will need to update the `version` in the [`pyproject.toml`](./pyproject.toml) file.
Next you need to merge these changes into the `develop` branch using a pull request.

You need to create a pull request from `develop` to `main` and merge it. This will trigger the GitHub Actions [`release`](.github/workflows/release.yml)
workflow.

All done!
