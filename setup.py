# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from setuptools import setup, find_packages


setup(
  name='infra_libs',
  version='2.4.1',
  description='Chrome Infra Libraries',
  long_description='Chrome Infra Libraries',
  author='The Chromium Authors',
  author_email='infra-dev@chromium.org',
  url='https://chromium.googlesource.com/infra/infra/+/main/packages/infra_libs',
  classifiers=[
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.9',
  ],
  packages=find_packages(exclude=['*.test']),
  install_requires=[
    'google-api-python-client',
    'google-auth; python_version >= "3.0.0"',
    'google-auth-httplib2; python_version >= "3.0.0"',
    'oauth2client==3.0.0',
    'protobuf',
    'requests',
    'six',
  ],
  package_data={
    '': ['*.md', '*.proto'],
  },
)
