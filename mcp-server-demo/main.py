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
             If no notes are available, it returns a message indicating that it isnt there.
    '''
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "No notes yet."

    return f"Here are the latest notes:\n{content}"

def read_monkey_facts():
    """
    Feature 1: Read and display monkey facts from notes.txt
    Returns a list of all monkey facts from the notes file
    """
    try:
        with open('notes.txt', 'r') as file:
            facts = [line.strip() for line in file if line.strip()]
        return facts
    except FileNotFoundError:
        print("Error: notes.txt file not found")
        return []

def search_monkey_facts(keyword: str) -> list:
    """
    Feature 2: Search monkey facts by keyword
    Returns a list of facts containing the given keyword
    """
    facts = read_monkey_facts()
    return [fact for fact in facts if keyword.lower() in fact.lower()]

if __name__ == "__main__":
    # Test the first feature
    facts = read_monkey_facts()
    print("Feature 1: Reading Monkey Facts")
    print("First 3 facts:")
    for fact in facts[:3]:
        print(fact)
    print("\n")
