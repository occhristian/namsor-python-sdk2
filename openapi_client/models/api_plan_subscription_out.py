# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.5
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class APIPlanSubscriptionOut(object):
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
        'api_key': 'str',
        'plan_started': 'int',
        'prior_plan_started': 'int',
        'plan_ended': 'int',
        'tax_rate': 'float',
        'plan_name': 'str',
        'plan_base_fees_key': 'str',
        'plan_status': 'str',
        'plan_quota': 'int',
        'price_usd': 'float',
        'price_overage_usd': 'float',
        'price': 'float',
        'price_overage': 'float',
        'currency': 'str',
        'currency_factor': 'float',
        'stripe_customer_id': 'str',
        'stripe_status': 'str',
        'stripe_subscription': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'plan_started': 'planStarted',
        'prior_plan_started': 'priorPlanStarted',
        'plan_ended': 'planEnded',
        'tax_rate': 'taxRate',
        'plan_name': 'planName',
        'plan_base_fees_key': 'planBaseFeesKey',
        'plan_status': 'planStatus',
        'plan_quota': 'planQuota',
        'price_usd': 'priceUSD',
        'price_overage_usd': 'priceOverageUSD',
        'price': 'price',
        'price_overage': 'priceOverage',
        'currency': 'currency',
        'currency_factor': 'currencyFactor',
        'stripe_customer_id': 'stripeCustomerId',
        'stripe_status': 'stripeStatus',
        'stripe_subscription': 'stripeSubscription',
        'user_id': 'userId'
    }

    def __init__(self, api_key=None, plan_started=None, prior_plan_started=None, plan_ended=None, tax_rate=None, plan_name=None, plan_base_fees_key=None, plan_status=None, plan_quota=None, price_usd=None, price_overage_usd=None, price=None, price_overage=None, currency=None, currency_factor=None, stripe_customer_id=None, stripe_status=None, stripe_subscription=None, user_id=None):  # noqa: E501
        """APIPlanSubscriptionOut - a model defined in OpenAPI"""  # noqa: E501

        self._api_key = None
        self._plan_started = None
        self._prior_plan_started = None
        self._plan_ended = None
        self._tax_rate = None
        self._plan_name = None
        self._plan_base_fees_key = None
        self._plan_status = None
        self._plan_quota = None
        self._price_usd = None
        self._price_overage_usd = None
        self._price = None
        self._price_overage = None
        self._currency = None
        self._currency_factor = None
        self._stripe_customer_id = None
        self._stripe_status = None
        self._stripe_subscription = None
        self._user_id = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if plan_started is not None:
            self.plan_started = plan_started
        if prior_plan_started is not None:
            self.prior_plan_started = prior_plan_started
        if plan_ended is not None:
            self.plan_ended = plan_ended
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if plan_name is not None:
            self.plan_name = plan_name
        if plan_base_fees_key is not None:
            self.plan_base_fees_key = plan_base_fees_key
        if plan_status is not None:
            self.plan_status = plan_status
        if plan_quota is not None:
            self.plan_quota = plan_quota
        if price_usd is not None:
            self.price_usd = price_usd
        if price_overage_usd is not None:
            self.price_overage_usd = price_overage_usd
        if price is not None:
            self.price = price
        if price_overage is not None:
            self.price_overage = price_overage
        if currency is not None:
            self.currency = currency
        if currency_factor is not None:
            self.currency_factor = currency_factor
        if stripe_customer_id is not None:
            self.stripe_customer_id = stripe_customer_id
        if stripe_status is not None:
            self.stripe_status = stripe_status
        if stripe_subscription is not None:
            self.stripe_subscription = stripe_subscription
        if user_id is not None:
            self.user_id = user_id

    @property
    def api_key(self):
        """Gets the api_key of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The api_key of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this APIPlanSubscriptionOut.


        :param api_key: The api_key of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def plan_started(self):
        """Gets the plan_started of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The plan_started of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: int
        """
        return self._plan_started

    @plan_started.setter
    def plan_started(self, plan_started):
        """Sets the plan_started of this APIPlanSubscriptionOut.


        :param plan_started: The plan_started of this APIPlanSubscriptionOut.  # noqa: E501
        :type: int
        """

        self._plan_started = plan_started

    @property
    def prior_plan_started(self):
        """Gets the prior_plan_started of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The prior_plan_started of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: int
        """
        return self._prior_plan_started

    @prior_plan_started.setter
    def prior_plan_started(self, prior_plan_started):
        """Sets the prior_plan_started of this APIPlanSubscriptionOut.


        :param prior_plan_started: The prior_plan_started of this APIPlanSubscriptionOut.  # noqa: E501
        :type: int
        """

        self._prior_plan_started = prior_plan_started

    @property
    def plan_ended(self):
        """Gets the plan_ended of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The plan_ended of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: int
        """
        return self._plan_ended

    @plan_ended.setter
    def plan_ended(self, plan_ended):
        """Sets the plan_ended of this APIPlanSubscriptionOut.


        :param plan_ended: The plan_ended of this APIPlanSubscriptionOut.  # noqa: E501
        :type: int
        """

        self._plan_ended = plan_ended

    @property
    def tax_rate(self):
        """Gets the tax_rate of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The tax_rate of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this APIPlanSubscriptionOut.


        :param tax_rate: The tax_rate of this APIPlanSubscriptionOut.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def plan_name(self):
        """Gets the plan_name of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The plan_name of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this APIPlanSubscriptionOut.


        :param plan_name: The plan_name of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

    @property
    def plan_base_fees_key(self):
        """Gets the plan_base_fees_key of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The plan_base_fees_key of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._plan_base_fees_key

    @plan_base_fees_key.setter
    def plan_base_fees_key(self, plan_base_fees_key):
        """Sets the plan_base_fees_key of this APIPlanSubscriptionOut.


        :param plan_base_fees_key: The plan_base_fees_key of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._plan_base_fees_key = plan_base_fees_key

    @property
    def plan_status(self):
        """Gets the plan_status of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The plan_status of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._plan_status

    @plan_status.setter
    def plan_status(self, plan_status):
        """Sets the plan_status of this APIPlanSubscriptionOut.


        :param plan_status: The plan_status of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._plan_status = plan_status

    @property
    def plan_quota(self):
        """Gets the plan_quota of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The plan_quota of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: int
        """
        return self._plan_quota

    @plan_quota.setter
    def plan_quota(self, plan_quota):
        """Sets the plan_quota of this APIPlanSubscriptionOut.


        :param plan_quota: The plan_quota of this APIPlanSubscriptionOut.  # noqa: E501
        :type: int
        """

        self._plan_quota = plan_quota

    @property
    def price_usd(self):
        """Gets the price_usd of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The price_usd of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: float
        """
        return self._price_usd

    @price_usd.setter
    def price_usd(self, price_usd):
        """Sets the price_usd of this APIPlanSubscriptionOut.


        :param price_usd: The price_usd of this APIPlanSubscriptionOut.  # noqa: E501
        :type: float
        """

        self._price_usd = price_usd

    @property
    def price_overage_usd(self):
        """Gets the price_overage_usd of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The price_overage_usd of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: float
        """
        return self._price_overage_usd

    @price_overage_usd.setter
    def price_overage_usd(self, price_overage_usd):
        """Sets the price_overage_usd of this APIPlanSubscriptionOut.


        :param price_overage_usd: The price_overage_usd of this APIPlanSubscriptionOut.  # noqa: E501
        :type: float
        """

        self._price_overage_usd = price_overage_usd

    @property
    def price(self):
        """Gets the price of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The price of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this APIPlanSubscriptionOut.


        :param price: The price of this APIPlanSubscriptionOut.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def price_overage(self):
        """Gets the price_overage of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The price_overage of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: float
        """
        return self._price_overage

    @price_overage.setter
    def price_overage(self, price_overage):
        """Sets the price_overage of this APIPlanSubscriptionOut.


        :param price_overage: The price_overage of this APIPlanSubscriptionOut.  # noqa: E501
        :type: float
        """

        self._price_overage = price_overage

    @property
    def currency(self):
        """Gets the currency of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The currency of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this APIPlanSubscriptionOut.


        :param currency: The currency of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def currency_factor(self):
        """Gets the currency_factor of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The currency_factor of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: float
        """
        return self._currency_factor

    @currency_factor.setter
    def currency_factor(self, currency_factor):
        """Sets the currency_factor of this APIPlanSubscriptionOut.


        :param currency_factor: The currency_factor of this APIPlanSubscriptionOut.  # noqa: E501
        :type: float
        """

        self._currency_factor = currency_factor

    @property
    def stripe_customer_id(self):
        """Gets the stripe_customer_id of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The stripe_customer_id of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._stripe_customer_id

    @stripe_customer_id.setter
    def stripe_customer_id(self, stripe_customer_id):
        """Sets the stripe_customer_id of this APIPlanSubscriptionOut.


        :param stripe_customer_id: The stripe_customer_id of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._stripe_customer_id = stripe_customer_id

    @property
    def stripe_status(self):
        """Gets the stripe_status of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The stripe_status of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._stripe_status

    @stripe_status.setter
    def stripe_status(self, stripe_status):
        """Sets the stripe_status of this APIPlanSubscriptionOut.


        :param stripe_status: The stripe_status of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._stripe_status = stripe_status

    @property
    def stripe_subscription(self):
        """Gets the stripe_subscription of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The stripe_subscription of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._stripe_subscription

    @stripe_subscription.setter
    def stripe_subscription(self, stripe_subscription):
        """Sets the stripe_subscription of this APIPlanSubscriptionOut.


        :param stripe_subscription: The stripe_subscription of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._stripe_subscription = stripe_subscription

    @property
    def user_id(self):
        """Gets the user_id of this APIPlanSubscriptionOut.  # noqa: E501


        :return: The user_id of this APIPlanSubscriptionOut.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this APIPlanSubscriptionOut.


        :param user_id: The user_id of this APIPlanSubscriptionOut.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, APIPlanSubscriptionOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
