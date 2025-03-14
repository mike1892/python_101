"""
Python 101
14 Mar 2025
"""

import os


def clear_screen():
    """Clear screen method."""
    os.system("cls" if os.name == "nt" else "clear")
    # os.system("mode con: cols=200 lines=5000")    # For windows only


def main():
    clear_screen()
    print("Hello from python-101!")


if __name__ == "__main__":
    main()
