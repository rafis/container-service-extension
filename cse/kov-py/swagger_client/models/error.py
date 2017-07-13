# coding: utf-8

"""
    API Specification for the Kubernetes on vSphere (KOV)

    # RESTful API for the Kubernetes on vSphere (KOV) 

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Error(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, message=None, help_url=None, cause=None):
        """
        Error - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'int',
            'message': 'str',
            'help_url': 'str',
            'cause': 'Error'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'help_url': 'helpUrl',
            'cause': 'cause'
        }

        self._code = code
        self._message = message
        self._help_url = help_url
        self._cause = cause

    @property
    def code(self):
        """
        Gets the code of this Error.
        The error code

        :return: The code of this Error.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Error.
        The error code

        :param code: The code of this Error.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this Error.
        The error message

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Error.
        The error message

        :param message: The message of this Error.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def help_url(self):
        """
        Gets the help_url of this Error.
        link to help page explaining the error in more detail

        :return: The help_url of this Error.
        :rtype: str
        """
        return self._help_url

    @help_url.setter
    def help_url(self, help_url):
        """
        Sets the help_url of this Error.
        link to help page explaining the error in more detail

        :param help_url: The help_url of this Error.
        :type: str
        """

        self._help_url = help_url

    @property
    def cause(self):
        """
        Gets the cause of this Error.

        :return: The cause of this Error.
        :rtype: Error
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """
        Sets the cause of this Error.

        :param cause: The cause of this Error.
        :type: Error
        """

        self._cause = cause

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
