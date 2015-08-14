########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='dproxy',

    version='0.1',
    author='dewayne',
    author_email='dewayne@gigaspaces.com',
    description='plugin that defines dependencies between deployments',

    # This must correspond to the actual packages in the plugin.
    packages=['plugin'],

    license='LICENSE',
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-plugins-common>=3.2", 'cloudify'
    ],
    test_requires=[
        "cloudify-dsl-parser>=3.2"
        "nose"
    ]
)
