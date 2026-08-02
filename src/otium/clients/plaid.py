"""Plaid — connected account balances.

Read only. Plaid reports balances as float dollars and reports no yield on
depository accounts, so `Account.apy` is left unknown here and supplied
elsewhere.
"""

from plaid.api.plaid_api import PlaidApi
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest

from ..models import Account


class PlaidClient:
    """Reads connected accounts from Plaid."""

    def __init__(self, api: PlaidApi) -> None:
        """Take the Plaid API this client talks to.

        Args:
            api: A configured plaid_api.PlaidApi

        """
        self._api = api

    def accounts(self, access_token: str) -> list[Account]:
        """Fetch every account on an Item with its current balance.

        Args:
            access_token: The Item's access token

        Returns:
            One Account per connected account, apy unknown

        """
        request = AccountsBalanceGetRequest(access_token=access_token)
        response = self._api.accounts_balance_get(request)
        return [
            Account(
                name=account["name"],
                balance_cents=round(account["balances"]["current"] * 100),
            )
            for account in response["accounts"]
        ]
