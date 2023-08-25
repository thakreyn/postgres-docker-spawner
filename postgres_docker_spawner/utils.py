import re
from rich.panel import Panel
from rich.columns import Columns
from rich import print

def to_kebab_case(input_string):
    # Replace spaces with dashes
    kebab_string = input_string.replace(' ', '-')

    # Remove special characters
    kebab_string = re.sub(r'[^\w\s-]', '', kebab_string)

    # Convert to lowercase
    kebab_string = kebab_string.lower()

    return kebab_string

def display_container_information_panels(containers: list):
    """ Takes in a list of containers and generates a column wise panel display for them """
    
    data = list()
    for container in containers:
        data.append(generate_container_data_panel(container))
    print(Columns(data))
        
def generate_container_data_panel(container: str) -> Panel:
    """
        Create a python rich panel to display container information
    """
    
    container_details: str = f"""
    Container ID: {container.id}
    Name: {container.name}
    Status: {container.status}
    Ports: {container.ports}
    """
    return Panel(container_details)