# MCP-server

# AI Sticky Notes MCP Server

A simple Machine Communication Protocol (MCP) server that manages digital sticky notes.

## Overview

This project demonstrates how to build a functional MCP server that allows you to:

- Add notes to a persistent text file
- Read all stored notes
- Retrieve only the latest note
- Generate prompts for AI summarization of your notes

## Features

### Tools

- **add_note**: Append a new note to your collection
- **read_notes**: View all your saved notes

### Resources

- **notes://latest**: Access your most recent note

### Prompts

- **notes_summary_prompt**: Generate a prompt that includes all your notes for AI summarization

## Getting Started

1. Make sure you have the MCP library installed:

   ```
   uv run mcp install
   ```

2. Run the server:

   ```
   uv run python main.py
   ```

3. Interact with your sticky notes through the MCP interface

## File Structure

- `main.py`: The MCP server implementation
- `notes.txt`: The text file where your notes are stored

## Implementation Details

The server uses a local text file to store notes. The file path is relative to the script location, making it portable across different environments.

Each function includes proper error handling and file existence checks to ensure smooth operation.

4. My prompt asked the AI to give 10 notes about monkeys. It then creates 10 notes about monkeys.

5. I asked the AI to give me a summary of the notes. It then gives me a summary of the notes.

6. I asked the AI to give me the latest note. It then gives me the latest note.
