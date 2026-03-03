import sys
import pyperclip
import emoji

def main():
    if len(sys.argv) < 2:
        print("Usage: emoji-search <keyword>")
        sys.exit(1)

    search_term = sys.argv[1]
    # emojize converts an alias like :fire: into 🔥
    result = emoji.emojize(f":{search_term}:", language='alias')

    
    if result != f":{search_term}:":
        pyperclip.copy(result)
        print(f"{result} copied to clipboard!")
    else:
        print(f"No emoji found for '{search_term}'")

if __name__ == "__main__":
    main()