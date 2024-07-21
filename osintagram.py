import argparse
from instagram_api_handler import InstagramAPIHandler
from environment_config import load_configuration
from output_manager import display_user_info
from rich.console import Console

def main():
    console = Console()

    parser = argparse.ArgumentParser(description="Osintagram - Instagram OSINT Tool")
    parser.add_argument('-u', '--username', type=str, help='Instagram username to fetch information for')
    parser.add_argument('--setup', action='store_true', help='Run setup to configure the tool')

    args = parser.parse_args()

    if args.setup:
        from setup import setup
        setup()
        return

    if not args.username:
        console.print("[red]Error: You must specify a username using the -u or --username option.[/red]")
        return

    try:
        session_id = load_configuration()
    except FileNotFoundError as e:
        console.print("[red]Error:[/red] " + str(e))
        console.print("[yellow]Run the setup first using --setup option.[/yellow]")
        return

    api_handler = InstagramAPIHandler(session_id)
    user_info, error = api_handler.fetch_user_information(args.username)
    
    if error:
        console.print(f'[red]Error fetching user info:[/red] {error}')
    else:
        display_user_info(user_info)

if __name__ == '__main__':
    main()
