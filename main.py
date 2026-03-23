"""
Modular RAG MCP Server - Main Entry Point

This is the entry point for the MCP Server. It initializes the configuration,
sets up logging, and starts the server.
"""

import sys
from pathlib import Path

from src.core.settings import SettingsError, load_settings
from src.observability.logger import get_logger


def main() -> int:
    """
    Main entry point for the MCP Server.
    
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    settings_path = Path("config/settings.yaml")
    try:
        load_settings(settings_path)
    except SettingsError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1

    from src.mcp_server.server import run_stdio_server
    return run_stdio_server()


if __name__ == "__main__":
    sys.exit(main())
