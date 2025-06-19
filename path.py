import os
import sys
import platform
from pathlib import Path

def add_to_path(path_to_add):
    system = platform.system()
    home = str(Path.home())

    if system == "Windows":
        try:
            import winreg

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS) as key:
                current_path, _ = winreg.QueryValueEx(key, "Path")
                if path_to_add not in current_path:
                    new_path = f"{current_path};{path_to_add}"
                    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                    print("Added to PATH. Please restart your system or log out and back in.")
                else:
                    print("Already in PATH.")
        except Exception as e:
            print(f"Failed to add to PATH on Windows: {e}")

    elif system in ["Linux", "Darwin"]: 
        rc_file = os.path.join(home, ".bashrc")
        if system == "Darwin":
            rc_file = os.path.join(home, ".zprofile")

        export_cmd = f'\n# VAUl3T PATH\nexport PATH="{path_to_add}:$PATH"\n'
        try:
            with open(rc_file, "a") as f:
                f.write(export_cmd)
            print(f"PATH added to {rc_file}. Run `source {rc_file}` or restart your terminal.")
        except Exception as e:
            print(f"Failed to write to {rc_file}: {e}")
    else:
        print("Unsupported OS")

def main():
    choice = input("Add VAUl3T to PATH? (Y/n): ").strip().lower()
    if choice in ["", "y", "yes"]:
        venv_bin = "venv\\Scripts" if platform.system() == "Windows" else "venv/bin"
        abs_path = os.path.abspath(venv_bin)
        add_to_path(abs_path)
    else:
        print("Skipped PATH addition.")

if __name__ == "__main__":
    main()
