"""Unit tests for PlaidClient — mocked PlaidApi, no network."""

from unittest.mock import Mock

import pytest

from .plaid import PlaidClient


class TestPlaidClient:
    """Unit tests for PlaidClient."""

    @pytest.fixture
    def api(self) -> Mock:
        """Stand in for plaid_api.PlaidApi."""
        return Mock()

    def test_accounts_should_map_plaid_dollars_to_cents(self, api: Mock) -> None:
        """Plaid reports balances as float dollars; money is held as int cents."""
        # Arrange
        api.accounts_balance_get.return_value = {
            "accounts": [
                {"name": "Everyday Savings", "balances": {"current": 12400.0}},
            ],
        }
        client = PlaidClient(api)

        # Act
        accounts = client.accounts("access-sandbox-1")

        # Assert
        assert accounts[0].balance_cents == 1_240_000

    def test_accounts_should_leave_apy_unknown(self, api: Mock) -> None:
        """Plaid does not report yields on depository accounts (see readme)."""
        # Arrange
        api.accounts_balance_get.return_value = {
            "accounts": [
                {"name": "Everyday Savings", "balances": {"current": 12400.0}},
            ],
        }
        client = PlaidClient(api)

        # Act
        accounts = client.accounts("access-sandbox-1")

        # Assert
        assert accounts[0].apy is None
