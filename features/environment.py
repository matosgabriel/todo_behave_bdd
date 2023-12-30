from selenium.webdriver import Firefox
from ipdb import spost_mortem


def before_all(ctx):
    ctx.browser = Firefox()


def after_step(ctx, step):
    if ctx.config.userdata.getbool("debug") and step.status == 'failed':
        spost_mortem(step.exc_traceback)


def after_all(ctx):
    ctx.browser.quit()
