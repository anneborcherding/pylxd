# Copyright (c) 2015 Canonical Ltd
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

import mock
import unittest

from pylxd import api
from pylxd import connection

import fake_api

class LXDUnitTestAlias(unittest.TestCase):
    def setUp(self):
        super(LXDUnitTestAlias, self).setUp()
        self.lxd = api.API()

    def test_alias_list(self):
        with mock.patch.object(connection.LXDConnection, 'get_object') as ms:
            ms.return_value = ('200', fake_api.fake_alias_list())
            self.assertEqual(1, len(self.lxd.alias_list()))