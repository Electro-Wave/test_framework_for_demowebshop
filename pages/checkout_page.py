from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_DATA = (By.CSS_SELECTOR, '.checkout-data')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_FirstName')
    FAST_NAME_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_LastName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_Email')
    COMPANY_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_Company')
    COUNTRY_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_CountryId')
    STATE_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_StateProvinceId')
    CITY_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_City')
    ADDRESS_1_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_Address1')
    ADDRESS_2_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_Address2')
    POSTAL_CODE_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_ZipPostalCode')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_PhoneNumber')
    FAX_NUMBER_FIELD = (By.CSS_SELECTOR, '#BillingNewAddress_FaxNumber')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#checkout-steps .button-1')
    IN_STORE_PICKUP_CHECKBOX = (By.CSS_SELECTOR, '#PickUpInStore')
    PURCHASE_ORDER = (By.CSS_SELECTOR, '#paymentmethod_3')
    PURCHASE_ORDER_NUMBER_FIELD = (By.CSS_SELECTOR, '#PurchaseOrderNumber')
    CONFIRM_ORDER_FORM = (By.CSS_SELECTOR, '.order-summary-content')
    SECTION_ORDER_COMPLETED = (By.CSS_SELECTOR, '.order-completed')

    def click_button_continue(self, index=0):
        self._find_elements(self.CONTINUE_BUTTON)[index].click()

    def click_checkbox_in_store_pickup(self):
        self._click(self.IN_STORE_PICKUP_CHECKBOX)

    def click_purchase_order(self):
        self._click(self.PURCHASE_ORDER)

    def input_number_order(self, value):
        self._input(self.PURCHASE_ORDER_NUMBER_FIELD, value)

    def should_be_confirm_order(self):
        self._is_present(self.CONFIRM_ORDER_FORM)

    def should_be_order_completed(self):
        self._is_present(self.SECTION_ORDER_COMPLETED)
