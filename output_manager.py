from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box
from rich.panel import Panel

def display_user_info(user_info):
    console = Console()
    user_data = user_info['data']['user']
    
    table = Table(show_header=False, box=box.ROUNDED, expand=False, width=100)
    table.add_column("Field", style="cyan", width=20, no_wrap=True)
    table.add_column("Value", width=80, overflow="fold")

    def get_value_or_na(data, key, subkey=None, preserve_newlines=False):
        value = data.get(key, {}).get(subkey, 'N/A') if subkey else data.get(key, 'N/A')
        if value in [None, 'None', '']:
            return Text("Not provided", style="italic dim")
        if preserve_newlines:
            return Text(str(value), overflow="fold")
        return str(value).replace('\n', ' ').strip()

    def format_bio_links(links):
        if not links or links == 'N/A':
            return Text("Not provided", style="italic dim")
        formatted_links = []
        for link in links:
            title = link.get('title', 'Untitled')
            url = link.get('url', '')
            formatted_links.append(f"{title}: {url}")
        return Text("\n".join(formatted_links), style="blue")

    # Basic Info
    table.add_row("Username", Text(f"@{get_value_or_na(user_data, 'username')}", style="bold green"))
    table.add_row("Full Name", get_value_or_na(user_data, 'full_name'))
    table.add_row("Biography", get_value_or_na(user_data, 'biography', preserve_newlines=True))

    # Links
    table.add_row("Bio Links", format_bio_links(user_data.get('bio_links', [])))
    external_url = get_value_or_na(user_data, 'external_url')
    table.add_row("External URL", external_url)
    table.add_row("FB Profile", get_value_or_na(user_data, 'fb_profile_biolink'))

    # Statistics
    table.add_section()
    table.add_row("Posts", Text(f"{get_value_or_na(user_data, 'edge_owner_to_timeline_media', 'count')}", style="yellow"))
    table.add_row("Followers", Text(f"{get_value_or_na(user_data, 'edge_followed_by', 'count')}", style="magenta"))
    table.add_row("Following", Text(f"{get_value_or_na(user_data, 'edge_follow', 'count')}", style="green"))

    # Account Info
    table.add_section()
    account_type = "Business" if user_data.get('is_business_account', False) else "Personal"
    table.add_row("Account Type", Text(f"{account_type}", style="bold"))
    is_private = "Yes" if user_data.get('is_private', False) else "No"
    table.add_row("Private Account", Text(f"{is_private}", style="bold red" if user_data.get('is_private', False) else "bold green"))

    # Contact Info
    table.add_section()
    table.add_row("Email Address", get_value_or_na(user_data, 'business_email'))
    table.add_row("Phone Number", get_value_or_na(user_data, 'business_phone_number'))
    table.add_row("Category", get_value_or_na(user_data, 'category_name'))

    panel = Panel(table, title=f"[bold]Instagram User Info: {user_data.get('username', 'Unknown User')}[/bold]", expand=False, border_style="yellow")
    console.print(panel)
