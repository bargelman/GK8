import pytest

from pageObjects.transaction_page import TransactionPage
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup")
class Test:
    startTransactionId = ReadConfig.getApplicationStartTransactionId()
    baseURL = ReadConfig.getApplicationBaseURL()

    def test_find_shortest_path_to_coinbase(self, setup):
        transaction_page = TransactionPage(self.driver, self.wait)
        transaction_page.breadth_first_search_algorithm(self.baseURL, self.startTransactionId)
