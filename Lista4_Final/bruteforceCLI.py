import typer
from functionalities import create_log_list
from bruteforceDetection import detect_bruteforce

app = typer.Typer()


@app.command()
def run_detection(logfile: str = typer.Argument(), consecutive_threshold: int = 10, max_interval_seconds: int = 5, target_single_user: bool = True):
    log_list = create_log_list(logfile, None)
    attacks = detect_bruteforce(log_list)

    if attacks:
        for attack in attacks:
            timestamp, ip, attempts = attack
            typer.echo(f"Attack detected: {timestamp} from {ip}, attempts: {attempts}")
    else:
        typer.echo("No brute-force attacks detected.")


if __name__ == "__main__":
    app()
