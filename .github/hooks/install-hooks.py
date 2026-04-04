"""
BF Git Guardian - Hook Installer
Run once after cloning: python .github/hooks/install-hooks.py

Copies the pre-commit hook into .git/hooks/ so it runs
automatically before every commit.

By Begine Fusion (beginefusion.com)
"""
import os
import sys
import shutil
import stat


def install():
    # Find repo root (walk up from this script's location)
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    git_hooks_dir = os.path.join(repo_root, ".git", "hooks")
    source_hooks_dir = os.path.join(repo_root, ".github", "hooks")

    if not os.path.exists(git_hooks_dir):
        print(f"[ERROR] Not a git repository: {repo_root}")
        print(f"        Run 'git init' first.")
        sys.exit(1)

    # Check for patterns file
    patterns_file = os.path.join(repo_root, ".github", ".sensitive-patterns")
    if not os.path.exists(patterns_file):
        print(f"[WARN] No .sensitive-patterns file found.")
        print(f"       The hook will skip scanning until you create one.")
        print(f"       Expected: .github/.sensitive-patterns")

    hooks = ["pre-commit"]
    installed = 0

    for hook in hooks:
        src = os.path.join(source_hooks_dir, hook)
        dst = os.path.join(git_hooks_dir, hook)

        if not os.path.exists(src):
            print(f"[SKIP] {hook} - source not found")
            continue

        # Backup existing hook if it's not ours
        if os.path.exists(dst):
            with open(dst, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            if "BF Git Guardian" not in content:
                backup = dst + ".backup"
                shutil.copy2(dst, backup)
                print(f"[BACKUP] Existing {hook} saved to {hook}.backup")

        shutil.copy2(src, dst)

        # Make executable
        st = os.stat(dst)
        os.chmod(dst, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

        print(f"[OK] Installed: {hook}")
        installed += 1

    print(f"\n{'=' * 50}")
    print(f"  BF Git Guardian - {installed} hook(s) installed")
    print(f"  Config: .github/.sensitive-patterns")
    print(f"  Every commit is now scanned automatically.")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    install()
