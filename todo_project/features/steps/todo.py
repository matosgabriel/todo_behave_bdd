from behave import given, when, then
from selenium.webdriver.common.by import By
from json import loads

from todo_project.pages.pages import PageTodo


@given('that i am in {page} page')
def open_todo_page(ctx, page):
    ctx.page = PageTodo(
        ctx.browser, 'http://selenium.dunossauro.live/todo_list.html')

    ctx.page.open()


@when('create a TODO card')
def create_todo(ctx):
    todo_info = loads(ctx.text)

    ctx.page.todo.create_todo(
        name=todo_info['name'],
        description=todo_info['description']
    )


@then('this TODO card should be in the stack "{element}"')
def check_stack(ctx, element):
    # import ipdb; ipdb.sset_trace()
    parsed_element = element.lower().replace(' ', '_')

    page_element = getattr(ctx.page, parsed_element)
    assert page_element.todos
