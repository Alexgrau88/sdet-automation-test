import allure
import time
import pytest

from selenium.common import NoSuchElementException
from Swapcard.pageObjects.HomePage import HomePage
from Swapcard.utils.conftest import chrome_driver, captcha_check, capture_screenshot


@allure.feature("Amazon Test for Swapcard")
@allure.story("Run through steps and verify Review Score and Price")
@allure.title("Amazon Review and Price Test")
def test_swapcard(chrome_driver):
    with allure.step("Open Amazon website"):
        url = "https://www.amazon.com"
        chrome_driver.get(url)
        captcha_check(chrome_driver)
        chrome_driver.implicitly_wait(2)

    homepage = HomePage(chrome_driver)
    try:
        # Test step 1: Go to https://www.amazon.com and expand the 'All' hamburger menu
        with allure.step("Click on page hamburger menu"):
            homepage.get_hamburger_menu().click()
            time.sleep(1)

        # Test step 2: Under 'Shop By Department' open 'Arts & Craft'
        with allure.step("Click on Arts and Crafts"):
            homepage.get_arts_and_crafts().click()
            time.sleep(2)

        # Test step 3: Open 'Beading & Jewelry Making'
        with allure.step("Click on Beading and Jewelry Making"):
            homepage.execute_script("arguments[0].click();", homepage.get_beading_jewelry_making_1())
            time.sleep(2)

        # Test step 4: Open 'Engraving Machines & Tools'
        with allure.step("Navigate through steps to reach Engraving Machines and tools"):
            homepage.get_arts_crafts_sewing().click()
            homepage.get_beading_jewelry_making_2().click()
            homepage.get_engraving_machines_tools().click()

        # Test step 5: Sort by Price: High to Low
        with allure.step("Open sort dropdown"):
            homepage.get_price_sort_dropdown().click()

        with allure.step("Select High to Low"):
            homepage.get_price_dropdown_value().click()

        # Test step 6: For the products that are currently available, open the third one
        with allure.step("Find and click on the third item on the page"):
            homepage.get_third_available_item().click()

        # Test step 7: Check the review score. If it's less than 4, fail the test; otherwise, pass it
        with allure.step("Check Review Score"):
            review_score = homepage.get_review_score()
            review_score_text = float(review_score.text)
            if review_score_text < 4.0:
                # Capture screenshot on failure
                capture_screenshot(chrome_driver, "review_score_failure")
                assert False, f"Test failed: Review score is less than 6.0. Actual score: {review_score_text}"

        # Test step 8: Check the price for the opened item. If it's more than $4000, fail the test; otherwise, pass it
        with allure.step("Check Price"):
            item_price = homepage.get_item_price()
            item_price_text = item_price.text
            final_price = float(item_price_text.replace('$', '').replace(',', ''))

            if final_price > 4000:
                # Capture screenshot on failure
                capture_screenshot(chrome_driver, "price_failure")
                assert False, f"Test failed: Price is more than 4000. Actual price: {final_price}"

    except NoSuchElementException as e:
        capture_screenshot(chrome_driver, "element_not_found_failure")
        pytest.fail(f"Test failed: Element not found. Error: {e}")
    finally:
        pass
