from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def get_weather(location: str) -> str:
    """Gets the weather for a given location.
    
    Args:
        location (str): The location (city, country, etc.)
    
    Returns:
        str: A short weather description.
    """
    return f"The weather in {location} is Sunny ☀️"
