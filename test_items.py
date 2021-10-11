link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.implicitly_wait(3)
    browser.get(link)
    basket_button=browser.find_element_by_css_selector(".btn-add-to-basket")
    assert basket_button is not None