from rich.console import Console
from rich.table import Table

console = Console()


def print_dns(records):
    table = Table(title="DNS Records")

    table.add_column("Type", style="cyan")
    table.add_column("Value", style="magenta")

    for record_type, values in records.items():
        if values:
            for v in values:
                table.add_row(record_type, v)
        else:
            table.add_row(record_type, "-")

    console.print(table)


def print_message(message):
    console.print(f"[bold green]{message}[/bold green]")


def print_trace(steps):
    table = Table(title="DNS Trace")

    table.add_column("Step", style="cyan")
    table.add_column("Details", style="magenta")

    for step, values in steps:
        for v in values:
            table.add_row(step, v)

    console.print(table)
