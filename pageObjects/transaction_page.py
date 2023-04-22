import json

from selenium.webdriver.support import expected_conditions as EC

from Locators.locator import Locators
from core.base_page import BasePage


class TransactionPage(BasePage):

    def convert_str_to_json_format(self, str_data, *locator):
        self.wait.until(EC.presence_of_element_located(locator))
        json_data = json.loads(str_data)
        return json_data

    def get_child_transactions_id_from_main_transactions_json_file(self, json_data):
        transaction_id_list = []
        inputs_key_length = len(json_data["inputs"])
        for i in range(inputs_key_length):
            transaction_id = json_data["inputs"][i]["txid"]
            transaction_id_list.append(transaction_id)
        return transaction_id_list

    def check_if_coinbase_found(self, json_data):
        if len(json_data["inputs"]) == 1:
            for i in range(1):
                is_coinbase = json_data["inputs"][i]["coinbase"]
                if is_coinbase:
                    print("Shortest path of coinbase found! From transaction: ", json_data["txid"])
                    return True
                else:
                    pass
        else:
            pass

    def breadth_first_search_algorithm(self, baseURL, startTransactionId):
        transaction_page = TransactionPage(self.driver, self.wait)
        visited_transaction_id = []
        transaction_id_crawl_list = [startTransactionId]
        for current_transaction_id in transaction_id_crawl_list:
            transaction_page.get(baseURL + current_transaction_id)
            transaction_page.click_on_element(*Locators.JSON_BUTTON)
            json_txt = transaction_page.find_element(*Locators.JSON_TEXT_FIELD).text
            json_data = transaction_page.convert_str_to_json_format(json_txt, *Locators.JSON_TEXT_FIELD)
            transaction_id_child = transaction_page.get_child_transactions_id_from_main_transactions_json_file(json_data)

            if transaction_page.check_if_coinbase_found(json_data):
                visited_transaction_id.append(current_transaction_id)
                print("Number of steps:" + str(len(visited_transaction_id)))
                break
            visited_transaction_id.append(current_transaction_id)
            for next_transaction_id in transaction_id_child:
                transaction_id_crawl_list.append(next_transaction_id)
