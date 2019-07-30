# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.5
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.chinese_api import ChineseApi  # noqa: E501
from openapi_client.rest import ApiException


class TestChineseApi(unittest.TestCase):
    """ChineseApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.chinese_api.ChineseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chinese_name_candidates(self):
        """Test case for chinese_name_candidates

        Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming  # noqa: E501
        """
        pass

    def test_chinese_name_candidates_batch(self):
        """Test case for chinese_name_candidates_batch

        Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming  # noqa: E501
        """
        pass

    def test_chinese_name_candidates_gender_batch(self):
        """Test case for chinese_name_candidates_gender_batch

        Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname) ex. Wang Xiaoming.  # noqa: E501
        """
        pass

    def test_chinese_name_gender_candidates(self):
        """Test case for chinese_name_gender_candidates

        Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender ('male' or 'female')  # noqa: E501
        """
        pass

    def test_chinese_name_match(self):
        """Test case for chinese_name_match

        Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming  # noqa: E501
        """
        pass

    def test_chinese_name_match_batch(self):
        """Test case for chinese_name_match_batch

        Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming  # noqa: E501
        """
        pass

    def test_gender_chinese_name(self):
        """Test case for gender_chinese_name

        Infer the likely gender of a Chinese full name ex. 王晓明  # noqa: E501
        """
        pass

    def test_gender_chinese_name_batch(self):
        """Test case for gender_chinese_name_batch

        Infer the likely gender of up to 100 full names ex. 王晓明  # noqa: E501
        """
        pass

    def test_gender_chinese_name_pinyin(self):
        """Test case for gender_chinese_name_pinyin

        Infer the likely gender of a Chinese name in LATIN (Pinyin).  # noqa: E501
        """
        pass

    def test_gender_chinese_name_pinyin_batch(self):
        """Test case for gender_chinese_name_pinyin_batch

        Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).  # noqa: E501
        """
        pass

    def test_parse_chinese_name(self):
        """Test case for parse_chinese_name

        Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name)  # noqa: E501
        """
        pass

    def test_parse_chinese_name_batch(self):
        """Test case for parse_chinese_name_batch

        Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name).  # noqa: E501
        """
        pass

    def test_pinyin_chinese_name(self):
        """Test case for pinyin_chinese_name

        Romanize the Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name)  # noqa: E501
        """
        pass

    def test_pinyin_chinese_name_batch(self):
        """Test case for pinyin_chinese_name_batch

        Romanize a list of Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
