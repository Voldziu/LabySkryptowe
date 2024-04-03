import typer
from functionalities import create_log_list
from bruteforceDetection import detect_bruteforce

app = typer.Typer()


@app.command()
def run_detection(logfile: str, consecutive_threshold: int = 10, max_interval_seconds: int = 5, target_single_user: bool = True):

    attacks = detect_bruteforce(logfile,
                                consecutive_attempts_threshold=consecutive_threshold,
                                interval_seconds=max_interval_seconds,
                                target_single_user=target_single_user)

    if attacks:
        for attack in attacks:
            start, end , ip, attempts = attack
            typer.echo(f"Attack detected:\nStart of the attack: {start}\nEnd of the attack: {end}\nFrom {ip[0]}\nUsed usernames: {ip[1]}\nAttempts: {attempts}\nDuration: {end-start}\n")
    else:
        typer.echo("No brute-force attacks detected.")


if __name__ == "__main__":
    app()
