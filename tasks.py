from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def pylint(ctx):
    ctx.run("pylint src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def open_html_report(ctx):
    ctx.run("open htmlcov/index.html")
