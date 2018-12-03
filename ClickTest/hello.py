import click
import requests

all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', \
             'cyan', 'white', 'bright_black', 'bright_red', \
             'bright_green', 'bright_yellow', 'bright_blue', \
             'bright_magenta', 'bright_cyan', 'bright_white'

CLI_URL = 'localhost:5000'

@click.group()
def cli():
    pass

@cli.command()
@click.argument('text')
def md5(text):
    """Reveal MD5 Hash [myhello] [md5] [input]"""
    resp = requests.get(f"http://localhost:5000/md5/{text}")
    print(resp.json())
@cli.command()
@click.argument('n')
def fact(n):
    """Find the Factorial [myhello] [fact] [num_input]"""
    resp = requests.get(f"http://localhost:5000/factorial/{n}")
    print(resp.json())
@cli.command()
@click.argument('finum')
def fib(finum):
    """Find Fibonacci sequence up to a number [myhello] [fib] [num_input]"""
    resp = requests.get(f"http://localhost:5000/fibonacci/{finum}")
    print(resp.json())
@cli.command()
@click.argument('prime')
def isprime(prime):
    """Determine if the number is prime or not [myhello] [isprime] [num_input]"""
    resp = requests.get(f"http://localhost:5000/is-prime/{prime}")
    print(resp.json())
@cli.command()
@click.argument('alert')
def slack(alert):
    """Send a Slack-Alert [myhello] [md5] [input(must be one continous line of text)]"""
    resp = requests.get(f"http://localhost:5000/slack-alert/{alert}")
    print(resp.json())
