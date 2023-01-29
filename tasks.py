from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def pylint(ctx):
    ctx.run("pylint src", pty=True)