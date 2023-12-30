from selenium.webdriver import Firefox
import ipdb


def before_all(ctx):
    ctx.browser = Firefox()


def after_step(ctx, step):
    if step.status == 'failed':
        ipdb.sset_trace()


def after_all(ctx):
    ctx.browser.quit()
