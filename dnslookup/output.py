from rich.console import Console

console = Console()

def print_result(result):
    console.print(f"[bold cyan]Domain:[/] {result.domain}")

    for r in result.records:
        console.print(f"[green]{r.type}[/] → {r.value}")

    if result.errors:
        console.print("[red]Errors:[/]")
        for e in result.errors:
            console.print(e)