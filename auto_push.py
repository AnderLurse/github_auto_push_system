import subprocess
import os
from datetime import datetime

REPO_PATH = "/root/github_auto_push_system"
os.chdir(REPO_PATH)

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Auto push: {datetime.now()}"])
subprocess.run(["git", "push"])

