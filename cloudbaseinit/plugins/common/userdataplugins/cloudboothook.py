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

from oslo_log import log as oslo_logging

from cloudbaseinit.plugins.common.userdataplugins import base


LOG = oslo_logging.getLogger(__name__)


class CloudBootHookPlugin(base.BaseUserDataPlugin):

    def __init__(self):
        super(CloudBootHookPlugin, self).__init__("text/cloud-boothook")

    def process(self, part):
        LOG.info("%s content is currently not supported" %
                 self.get_mime_type())
