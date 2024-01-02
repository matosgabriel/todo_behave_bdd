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
    ctx.todo_info = loads(ctx.text)

    ctx.page.todo.create_todo(
        name=ctx.todo_info['name'],
        description=ctx.todo_info['description']
    )


@when('create the following TODO cards')
def create_many_todos(ctx):
    for line in ctx.table.rows:
        parsed_line = dict(line.items())
        ctx.page.todo.create_todo(
            name=parsed_line['name'],
            description=parsed_line['description']
        )


@then('this TODO card should be in the stack "{element}"')
def check_stack(ctx, element):
    # import ipdb; ipdb.sset_trace()
    parsed_element = element.lower().replace(' ', '_')

    page_element = getattr(ctx.page, parsed_element)
    assert any(x.description ==
               ctx.todo_info['description'] for x in page_element.todos)


@then('the following TODO cards should be in the stack "{element}"')
def check_stack(ctx, element):
    # import ipdb; ipdb.sset_trace()
    parsed_element = element.lower().replace(' ', '_')

    created_todos = []
    for line in ctx.table.rows:
        parsed_line = dict(line.items())
        created_todos.append(parsed_line)

    page_element = getattr(ctx.page, parsed_element)
    for todo_card in created_todos:
        assert any(x.description ==
                   todo_card['description'] for x in page_element.todos)
