# server.py
from mcp.server.fastmcp import FastMCP
import os
# Create an MCP server
mcp = FastMCP("AI Sticky Notes")
NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    '''
    Append a new note to the sticky note file.
    
    Args:
        message(str): The note content to add.
        
    Returns:
        str: Confirmation message indicating the note has been added.
    '''
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note added successfully!"

@mcp.tool()
def read_notes() -> str:
    '''
    Read all notes from the sticky note file.
    
    Returns:
        str: All notes from the file.
    '''
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "No notes yet."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    '''
    Get the latest note from the sticky note file.
    
    Returns:
        str: The latest note from the file.
        If no notes are available, it returns a message indicating that.
    '''
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."

@mcp.prompt()
def notes_summary_prompt() -> str:
    '''
    Generate a prompt asking the AI to summarize the current notes.
    
    Returns:
        str: A prompt string that includes all notes and asks for a summary.
             If no notes are available, it returns a message indicating that.
    '''
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "No notes yet."
    
    return f"Here are the latest notes:\n{content}"
