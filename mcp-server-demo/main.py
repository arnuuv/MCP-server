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

def get_monkey_species_count() -> dict:
    """
    Feature 3: Count occurrences of different monkey species
    Returns a dictionary with species names and their mention count
    """
    facts = read_monkey_facts()
    species_count = {}
    for fact in facts:
        # Extract species names (words ending with 'monkey' or specific species)
        words = fact.lower().split()
        for word in words:
            if 'monkey' in word or word in ['macaque', 'tamarin', 'marmoset', 'mandrill']:
                species_count[word] = species_count.get(word, 0) + 1
    return species_count

def get_monkey_facts_by_length(min_length: int = 0, max_length: int = float('inf')) -> list:
    """
    Feature 4: Filter monkey facts by length
    Returns facts that fall within the specified length range
    """
    facts = read_monkey_facts()
    return [fact for fact in facts if min_length <= len(fact) <= max_length]

def get_endangered_monkey_facts() -> list:
    """
    Feature 5: Extract facts about endangered monkey species
    Returns a list of facts mentioning endangered status
    """
    facts = read_monkey_facts()
    endangered_keywords = ['endangered', 'critically endangered', 'threatened']
    return [fact for fact in facts if any(keyword in fact.lower() for keyword in endangered_keywords)]

def get_monkey_characteristics() -> dict:
    """
    Feature 6: Extract physical characteristics of monkeys
    Returns a dictionary of characteristics and their descriptions
    """
    facts = read_monkey_facts()
    characteristics = {}
    for fact in facts:
        if 'have' in fact.lower() or 'are' in fact.lower():
            # Simple parsing to extract characteristics
            parts = fact.lower().split('have' if 'have' in fact.lower() else 'are')
            if len(parts) > 1:
                characteristic = parts[1].strip()
                characteristics[characteristic] = fact
    return characteristics

def get_monkey_habitats() -> list:
    """
    Feature 7: Extract information about monkey habitats
    Returns a list of facts mentioning habitats or locations
    """
    facts = read_monkey_facts()
    habitat_keywords = ['found in', 'native to', 'live in', 'habitat']
    return [fact for fact in facts if any(keyword in fact.lower() for keyword in habitat_keywords)]

def get_monkey_behavior_facts() -> list:
    """
    Feature 8: Extract facts about monkey behavior
    Returns a list of facts about monkey behavior and social structure
    """
    facts = read_monkey_facts()
    behavior_keywords = ['behavior', 'social', 'live in groups', 'troop', 'communicate']
    return [fact for fact in facts if any(keyword in fact.lower() for keyword in behavior_keywords)]

def get_monkey_size_facts() -> dict:
    """
    Feature 9: Extract information about monkey sizes
    Returns a dictionary of size-related facts
    """
    facts = read_monkey_facts()
    size_facts = {}
    for fact in facts:
        if any(unit in fact.lower() for unit in ['inch', 'pound', 'kg', 'gram', 'meter']):
            # Extract the species name (usually at the start of the fact)
            species = fact.split()[0] if fact.split() else "Unknown"
            size_facts[species] = fact
    return size_facts

if __name__ == "__main__":
    # Test the first feature
    facts = read_monkey_facts()
    print("Feature 1: Reading Monkey Facts")
    print("First 3 facts:")
    for fact in facts[:3]:
        print(fact)
    print("\n")
