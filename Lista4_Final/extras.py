import typer
from Zad4 import zad4a, zad4b, zad4c
from Zad2 import zad2a, zad2b, zad2c, zad2d

app = typer.Typer()


@app.command()
def hello_world():
    print("hello world")


@app.command()
def func2a(logfile: str):
    print(zad2a(logfile))


@app.command()
def func2b(logfile: str):
    print(zad2b(logfile))


@app.command()
def func2c(logfile: str):
    print(zad2c(logfile))


@app.command()
def func2d(logfile: str):
    print(zad2d(logfile))


@app.command()
def func4a(logfile: str, n: int = 3):
    print(zad4a(file_dir=logfile, n=n))


@app.command()
def func4b(logfile: str, global_: bool = False):
    print(zad4b(file_dir=logfile, global_=global_))


@app.command()
def func4c(logfile: str):
    print(zad4c(logfile))


@app.command()
def set_level(level: str):
    print(f"Setting minimum logging level to {level}")


if __name__ == "__main__":
    app()
