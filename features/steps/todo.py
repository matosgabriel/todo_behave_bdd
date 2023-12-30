from behave import given, when, then
from selenium.webdriver.common.by import By
from json import loads


@given('that i am in todo page')
def open_todo_page(ctx):
    ctx.browser.get('http://selenium.dunossauro.live/todo_list.html')


@when('create a TODO card')
def create_todo(ctx):
    # import ipdb; ipdb.sset_trace()

    todo_info = loads(ctx.text)

    ctx.browser.find_element(By.ID, 'todo-name').send_keys(todo_info['name'])
    ctx.browser.find_element(
        By.ID, 'todo-desc').send_keys(todo_info['description'])
    ctx.browser.find_element(By.ID, 'todo-submit').click()


@then('this TODO card should be in the stack "{pilha}"')
def check_stack(ctx, pilha):
    # import ipdb; ipdb.sset_trace()

    assert 'run' in ctx.browser.find_element(By.CLASS_NAME, 'body_a').text
