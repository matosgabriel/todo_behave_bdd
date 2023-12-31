from selenium.webdriver import Firefox, Chrome, Edge, Safari
from ipdb import spost_mortem


def before_all(ctx):
    user_browser = ctx.config.userdata.get('browser')

    browsers_list = {
        'firefox': Firefox,
        'chrome': Chrome,
        'edge': Edge,
        'safari': Safari
    }

    ctx.browser = browsers_list[user_browser]()


def after_step(ctx, step):
    if ctx.config.userdata.getbool("debug") and step.status == 'failed':
        spost_mortem(step.exc_traceback)


def after_all(ctx):
    ctx.browser.quit()
