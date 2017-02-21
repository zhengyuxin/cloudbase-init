# Copyright 2014 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cloudbaseinit import conf as cloudbaseinit_conf
from cloudbaseinit.utils import classloader

CONF = cloudbaseinit_conf.CONF


def load_plugins():
    plugins = {}
    cl = classloader.ClassLoader()
    for class_path in CONF.user_data_plugins:
        plugin = cl.load_class(class_path)()
        plugins[plugin.get_mime_type()] = plugin
    return plugins
