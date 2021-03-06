# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.9
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.admin_api import AdminApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_credits(self):
        """Test case for add_credits

        Add usage credits to an API Key.  # noqa: E501
        """
        pass

    def test_anonymize(self):
        """Test case for anonymize

        Activate/deactivate anonymization for a source.  # noqa: E501
        """
        pass

    def test_api_status(self):
        """Test case for api_status

        Prints the current status of the classifiers.  # noqa: E501
        """
        pass

    def test_api_usage(self):
        """Test case for api_usage

        Print current API usage.  # noqa: E501
        """
        pass

    def test_api_usage_history(self):
        """Test case for api_usage_history

        Print historical API usage.  # noqa: E501
        """
        pass

    def test_api_usage_history_aggregate(self):
        """Test case for api_usage_history_aggregate

        Print historical API usage (in an aggregated view, by service, by day/hour/min).  # noqa: E501
        """
        pass

    def test_available_plans(self):
        """Test case for available_plans

        List all available plans in the user's preferred currency.  # noqa: E501
        """
        pass

    def test_available_plans1(self):
        """Test case for available_plans1

        List all available plans in the default currency (usd).  # noqa: E501
        """
        pass

    def test_available_services(self):
        """Test case for available_services

        List of API services and usage cost in Units (default is 1=ONE Unit).  # noqa: E501
        """
        pass

    def test_billing_currencies(self):
        """Test case for billing_currencies

        List possible currency options for billing (USD, EUR, GBP, ...)  # noqa: E501
        """
        pass

    def test_billing_history(self):
        """Test case for billing_history

        Read the history billing information (invoices paid via Stripe or manually).  # noqa: E501
        """
        pass

    def test_billing_info(self):
        """Test case for billing_info

        Read the billing information (company name, address, phone, vat ID)  # noqa: E501
        """
        pass

    def test_charge(self):
        """Test case for charge

        Create a Stripe Customer, based on a payment card token (from secure StripeJS) and email.  # noqa: E501
        """
        pass

    def test_corporate_key(self):
        """Test case for corporate_key

        Setting an API Key to a corporate status.  # noqa: E501
        """
        pass

    def test_debug_level(self):
        """Test case for debug_level

        Update debug level for a classifier  # noqa: E501
        """
        pass

    def test_flush(self):
        """Test case for flush

        Flush counters.  # noqa: E501
        """
        pass

    def test_invalidate_cache(self):
        """Test case for invalidate_cache

        Invalidate system caches.  # noqa: E501
        """
        pass

    def test_learnable(self):
        """Test case for learnable

        Activate/deactivate learning from a source.  # noqa: E501
        """
        pass

    def test_namsor_counter(self):
        """Test case for namsor_counter

        Get the overall API counter  # noqa: E501
        """
        pass

    def test_payment_info(self):
        """Test case for payment_info

        Get the Stripe payment information associated with the current google auth session token.  # noqa: E501
        """
        pass

    def test_procure_key(self):
        """Test case for procure_key

        Procure an API Key (sent via Email), based on an auth token. Keep your API Key secret.  # noqa: E501
        """
        pass

    def test_redeploy_ui(self):
        """Test case for redeploy_ui

        Redeploy UI from current dev branch.  # noqa: E501
        """
        pass

    def test_redeploy_ui1(self):
        """Test case for redeploy_ui1

        Redeploy UI from current dev branch.  # noqa: E501
        """
        pass

    def test_remove_user_account(self):
        """Test case for remove_user_account

        Remove the user account.  # noqa: E501
        """
        pass

    def test_remove_user_account_on_behalf(self):
        """Test case for remove_user_account_on_behalf

        Remove (on behalf) a user account.  # noqa: E501
        """
        pass

    def test_shutdown(self):
        """Test case for shutdown

        Stop learning and shutdown system.  # noqa: E501
        """
        pass

    def test_software_version(self):
        """Test case for software_version

        Get the current software version  # noqa: E501
        """
        pass

    def test_source_stats(self):
        """Test case for source_stats

        Print basic source statistics.  # noqa: E501
        """
        pass

    def test_stats(self):
        """Test case for stats

        Print basic system statistics.  # noqa: E501
        """
        pass

    def test_stripe_connect(self):
        """Test case for stripe_connect

        Connects a Stripe Account.  # noqa: E501
        """
        pass

    def test_subscribe_plan(self):
        """Test case for subscribe_plan

        Subscribe to a give API plan, using the user's preferred or default currency.  # noqa: E501
        """
        pass

    def test_subscribe_plan_on_behalf(self):
        """Test case for subscribe_plan_on_behalf

        Subscribe to a give API plan, using the user's preferred or default currency (admin only).  # noqa: E501
        """
        pass

    def test_taxonomy_classes(self):
        """Test case for taxonomy_classes

        Print the taxonomy classes valid for the given classifier.  # noqa: E501
        """
        pass

    def test_update_billing_info(self):
        """Test case for update_billing_info

        Sets or update the billing information (company name, address, phone, vat ID)  # noqa: E501
        """
        pass

    def test_update_limit(self):
        """Test case for update_limit

        Modifies the hard/soft limit on the API plan's overages (default is 0$ soft limit).  # noqa: E501
        """
        pass

    def test_update_payment_default(self):
        """Test case for update_payment_default

        Update the default Stripe card associated with the current google auth session token.  # noqa: E501
        """
        pass

    def test_user_info(self):
        """Test case for user_info

        Get the user profile associated with the current google auth session token.  # noqa: E501
        """
        pass

    def test_verify_email(self):
        """Test case for verify_email

        Verifies an email, based on token sent to that email  # noqa: E501
        """
        pass

    def test_verify_remove_email(self):
        """Test case for verify_remove_email

        Verifies an email, based on token sent to that email  # noqa: E501
        """
        pass

    def test_vet(self):
        """Test case for vet

        Vetting of a source.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
