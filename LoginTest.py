import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_extension(r"PrinterLogicExtensionv1.0.5.8.crx")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)


class LoginTestCase(unittest.TestCase):

    def test_01_page_opens(self):
        driver.get("http://testtrial.printercloud.com")
        self.assertIn("PrinterLogic", driver.title)

    def test_02_login_ui_loads(self):
        time.sleep(5)
        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window did not load.")

    def test_03_empty_username_and_password_submission_rejected(self):
        time.sleep(1)
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with empty username and password.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

    def test_04_empty_username_submission_rejected(self):
        time.sleep(1)
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        password_entry_form.send_keys('Tijuana2016!')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with no username.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        password_entry_form.clear()

    def test_05_empty_password_submission_rejected(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('condielj')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with no password.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        username_entry_form.clear()

    def test_06_correct_username_with_bad_password_rejected(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('condielj')
        password_entry_form.send_keys('thisis-not-mypassword')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with an incorrect password.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        username_entry_form.clear()
        password_entry_form.clear()

    def test_07_bad_username_with_correct_password_rejected(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('thisis-not-myusername')
        password_entry_form.send_keys('Tijuana2016!')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with incorrect username/password combination.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        username_entry_form.clear()
        password_entry_form.clear()

    def test_08_bad_username_with_bad_password_rejected(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('thisis-not-myusername')
        password_entry_form.send_keys('thisis-not-mypassword')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with incorrect username/password combination.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        username_entry_form.clear()
        password_entry_form.clear()

    def test_09_correct_username_with_similar_password_rejected(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('thisis-not-myusername')
        password_entry_form.send_keys('Tijuana2016!')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with incorrect username/password combination.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        username_entry_form.clear()
        password_entry_form.clear()

    #
    #
    # condIelj was accepted, showing that the username is not case sensitive
    # CONDIELJ was also accepted
    # is this intentional?
    #
    #

    def test_10_similar_username_with_correct_password_rejected(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('condieIj')
        password_entry_form.send_keys('Tijuana2016!')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with incorrect username/password combination.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        username_entry_form.clear()
        password_entry_form.clear()

    def test_11_password_is_case_sensitive(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        password_rejected_div = driver.find_element_by_xpath('//*[@id="logintext"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('condielj')
        password_entry_form.send_keys('TIJUANA2016!')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(1, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window disappeared with incorrect username/password combination.")
        self.assertEqual("Invalid username or password.", password_rejected_div.text,
                         "Invalid submission message failed to display.")

        username_entry_form.clear()
        password_entry_form.clear()

    def test_12_correct_username_with_correct_password_accepted(self):
        time.sleep(1)
        username_entry_form = driver.find_element_by_xpath('//*[@id="relogin_user"]')
        password_entry_form = driver.find_element_by_xpath('//*[@id="relogin_password"]')
        log_in_button = driver.find_element_by_xpath('//*[@id="self_service_portal_login_dialog_login_button"]')

        username_entry_form.send_keys('condielj')
        password_entry_form.send_keys('Tijuana2016!')
        log_in_button.click()
        time.sleep(1)

        self.assertEqual(0, len(driver.find_elements_by_xpath('//*[@id="client"]/div[5]')),
                         "Pop-up window failed to disappear with correct username/password combination.")

    def test_13_user_logged_in(self):
        time.sleep(2)
        user_dropdown = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/a')
        user_dropdown.click()
        time.sleep(1)
        logged_in = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[6]/div/div[1]/strong')
        self.assertEqual(logged_in.text, 'Logged in as:', "User not logged in after successful entry. ")

    def test_14_correct_user_logged_in(self):
        time.sleep(1)
        logged_user = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[6]/div/div[1]')
        self.assertEqual(logged_user.text, 'Logged in as: condielj', "Incorrect user/no user logged in after correct "
                                                                     "entry. ")

        driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
