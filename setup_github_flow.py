import subprocess
import os
import sys
import time
import re
import threading

env = os.environ.copy()
env['PATH'] = r'C:\Users\LG\AppData\Local\Programs\Git\cmd;C:\Users\LG\AppData\Local\Microsoft\WinGet\Packages\GitHub.cli_Microsoft.Winget.Source_8wekyb3d8bbwe\bin;' + env['PATH']
cwd = r'C:\Users\LG\.gemini\antigravity\scratch\gangnam-casino'

def run_cmd(cmd):
    print(f">> Running: {cmd}", flush=True)
    res = subprocess.run(cmd, shell=True, env=env, cwd=cwd, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout.strip(), flush=True)
    if res.stderr:
        print(res.stderr.strip(), flush=True)
    return res

print("Starting GitHub authentication...", flush=True)
proc = subprocess.Popen('gh auth login --web -h github.com -p https', shell=True, env=env, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

code_found = False

def read_stderr():
    global code_found
    for line in proc.stderr:
        clean = line.strip()
        print(f"[gh] {clean}", flush=True)
        m = re.search(r'one-time code:\s*([A-Z0-9\-]+)', clean)
        if m:
            code = m.group(1)
            code_found = True
            with open(os.path.join(cwd, 'auth_code.txt'), 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"\n==========================================", flush=True)
            print(f"  ONE-TIME CODE: {code}", flush=True)
            print(f"==========================================\n", flush=True)
            # Open browser for user automatically
            subprocess.run('cmd.exe /c start https://github.com/login/device', shell=True)

t = threading.Thread(target=read_stderr, daemon=True)
t.start()

# Wait up to 5 minutes for authentication
start_time = time.time()
while time.time() - start_time < 300:
    ret = proc.poll()
    if ret is not None:
        break
    time.sleep(1)

if proc.poll() != 0:
    print("Authentication timed out or failed.", flush=True)
    sys.exit(1)

print("\nGitHub authentication successful! Setting up Git and Repository...", flush=True)

# 1. Setup git credential helper
run_cmd('gh auth setup-git')

# 2. Get username
user_res = run_cmd('gh api user -q .login')
username = user_res.stdout.strip() if user_res.stdout else 'user'
print(f"Authenticated as GitHub user: {username}", flush=True)

# 3. Create repository and push
repo_create = run_cmd('gh repo create gangnam-casino --public --source=. --remote=origin --push')
if repo_create.returncode != 0:
    print("Repo might already exist, attempting git push directly...", flush=True)
    run_cmd('git push -u origin main')

# 4. Enable GitHub Pages
print("Enabling GitHub Pages...", flush=True)
run_cmd('gh api -X POST repos/:owner/gangnam-casino/pages -f "source[branch]=main" -f "source[path]=/"')

repo_url = f"https://github.com/{username}/gangnam-casino"
pages_url = f"https://{username}.github.io/gangnam-casino/"

with open(os.path.join(cwd, 'deploy_result.txt'), 'w', encoding='utf-8') as f:
    f.write(f"REPO_URL={repo_url}\nPAGES_URL={pages_url}\n")

print("\n========================================================", flush=True)
print(f"  DEPLOYMENT COMPLETE!")
print(f"  GitHub Repository: {repo_url}")
print(f"  Live Website:     {pages_url}")
print("========================================================\n", flush=True)
