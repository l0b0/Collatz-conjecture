Python skeleton
===

[![Build Status](https://travis-ci.org/l0b0/python-skeleton.svg)](https://travis-ci.org/l0b0/python-skeleton)

How to use for your own project:

1. Clone it to a new directory:

        git clone --recursive git@github.com:l0b0/python-skeleton.git your-project-name
1. See `configuration.mk` for build options
1. If you're using IDEA, replace the references in the configuration:

        project=your-project-name
        sed --in-place "s/python-skeleton/${project}/g;s/python_skeleton/${project//-/_}/g" .idea/*.xml *.iml
        git mv python_skeleton.iml "${project//-/_}.iml"
1. Replace the `python_skeleton` module and test file with your own code

Test
---

    make test

You can also test with a specific version of Python:

    make PYTHON_VERSION=2.7.11 test
