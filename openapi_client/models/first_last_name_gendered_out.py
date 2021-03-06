# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.9
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FirstLastNameGenderedOut(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'likely_gender': 'str',
        'gender_scale': 'float',
        'score': 'float',
        'probability_calibrated': 'float'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'likely_gender': 'likelyGender',
        'gender_scale': 'genderScale',
        'score': 'score',
        'probability_calibrated': 'probabilityCalibrated'
    }

    def __init__(self, id=None, first_name=None, last_name=None, likely_gender=None, gender_scale=None, score=None, probability_calibrated=None):  # noqa: E501
        """FirstLastNameGenderedOut - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._last_name = None
        self._likely_gender = None
        self._gender_scale = None
        self._score = None
        self._probability_calibrated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if likely_gender is not None:
            self.likely_gender = likely_gender
        if gender_scale is not None:
            self.gender_scale = gender_scale
        if score is not None:
            self.score = score
        if probability_calibrated is not None:
            self.probability_calibrated = probability_calibrated

    @property
    def id(self):
        """Gets the id of this FirstLastNameGenderedOut.  # noqa: E501


        :return: The id of this FirstLastNameGenderedOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirstLastNameGenderedOut.


        :param id: The id of this FirstLastNameGenderedOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this FirstLastNameGenderedOut.  # noqa: E501


        :return: The first_name of this FirstLastNameGenderedOut.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this FirstLastNameGenderedOut.


        :param first_name: The first_name of this FirstLastNameGenderedOut.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this FirstLastNameGenderedOut.  # noqa: E501


        :return: The last_name of this FirstLastNameGenderedOut.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this FirstLastNameGenderedOut.


        :param last_name: The last_name of this FirstLastNameGenderedOut.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def likely_gender(self):
        """Gets the likely_gender of this FirstLastNameGenderedOut.  # noqa: E501

        Most likely gender  # noqa: E501

        :return: The likely_gender of this FirstLastNameGenderedOut.  # noqa: E501
        :rtype: str
        """
        return self._likely_gender

    @likely_gender.setter
    def likely_gender(self, likely_gender):
        """Sets the likely_gender of this FirstLastNameGenderedOut.

        Most likely gender  # noqa: E501

        :param likely_gender: The likely_gender of this FirstLastNameGenderedOut.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female", "unknown"]  # noqa: E501
        if likely_gender not in allowed_values:
            raise ValueError(
                "Invalid value for `likely_gender` ({0}), must be one of {1}"  # noqa: E501
                .format(likely_gender, allowed_values)
            )

        self._likely_gender = likely_gender

    @property
    def gender_scale(self):
        """Gets the gender_scale of this FirstLastNameGenderedOut.  # noqa: E501

        Compatibility to NamSor_v1 Gender Scale M[-1..U..+1]F value  # noqa: E501

        :return: The gender_scale of this FirstLastNameGenderedOut.  # noqa: E501
        :rtype: float
        """
        return self._gender_scale

    @gender_scale.setter
    def gender_scale(self, gender_scale):
        """Sets the gender_scale of this FirstLastNameGenderedOut.

        Compatibility to NamSor_v1 Gender Scale M[-1..U..+1]F value  # noqa: E501

        :param gender_scale: The gender_scale of this FirstLastNameGenderedOut.  # noqa: E501
        :type: float
        """

        self._gender_scale = gender_scale

    @property
    def score(self):
        """Gets the score of this FirstLastNameGenderedOut.  # noqa: E501


        :return: The score of this FirstLastNameGenderedOut.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this FirstLastNameGenderedOut.


        :param score: The score of this FirstLastNameGenderedOut.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def probability_calibrated(self):
        """Gets the probability_calibrated of this FirstLastNameGenderedOut.  # noqa: E501


        :return: The probability_calibrated of this FirstLastNameGenderedOut.  # noqa: E501
        :rtype: float
        """
        return self._probability_calibrated

    @probability_calibrated.setter
    def probability_calibrated(self, probability_calibrated):
        """Sets the probability_calibrated of this FirstLastNameGenderedOut.


        :param probability_calibrated: The probability_calibrated of this FirstLastNameGenderedOut.  # noqa: E501
        :type: float
        """

        self._probability_calibrated = probability_calibrated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FirstLastNameGenderedOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
