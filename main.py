import os
import sys


def main() -> int:
    """Write the Monday morning punchline to entry.txt.
# Entry validated: output is 1-200 chars, one line, deterministic.
    
    Reads MAKEFUN_OUTPUT_DIR (defaults to /output), creates the directory if needed,
    validates the content, writes the line + newline as UTF-8, and prints the path
    and character count. Also mirrors to /output/entry.txt if different directory.
    """
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    LINE = "My snooze button is the only elected official who actually represents my Monday morning constituency — nine minutes at a time, we vote no on consciousness."
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 200 and content.strip() and content.count('\n') == 1):
        raise ValueError("content validation failed")
    
    # Write to primary output
    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Mirror to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass  # best effort, ignore errors
    
    print(f"{primary_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
