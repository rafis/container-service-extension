# coding: utf-8

"""
    API Specification for the Kubernetes on vSphere (KOV)

    # RESTful API for the Kubernetes on vSphere (KOV) 

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.task_id import TaskId


class TestTaskId(unittest.TestCase):
    """ TaskId unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskId(self):
        """
        Test TaskId
        """
        model = swagger_client.models.task_id.TaskId()


if __name__ == '__main__':
    unittest.main()
