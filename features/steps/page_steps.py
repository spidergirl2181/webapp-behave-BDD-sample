from behave import *
from nose.tools import assert_equals, assert_true

@given('I am redirected to home page')
def navigate_to_home_page(context):
    assert_equals(context.browser.current_url, "{}".format(context.base_url))

@when('I type {search_text} on search_box on home page and search')
def search_by_text(context, search_text):
    context.page.search_by_keyword(search_text)
    ex = context.page.is_serp_display()
    assert_true(ex)

@then('On search result page I want to see search result of {search_text} is {search_result}')
def verify_search_result(context, search_result, search_text):
    result = str(context.page.content_search(search_text))
    assert_equals(search_result, result)