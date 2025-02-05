import subprocess
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def run_command(command, working_dir=None):
    try:
        result = subprocess.run(command, cwd=working_dir, text=True, capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'{Fore.RED}Error executing command: {e.stderr}'

def git_add(working_dir, file_path):
    print(f'{Fore.YELLOW}[{time.strftime("%Y-%m-%d %H:%M:%S")}] {Style.BRIGHT}Attempting to add file: {file_path}')
    command = ['git', 'add', '-f', file_path]
    output = run_command(command, working_dir)
    print(f'{Fore.GREEN}[{time.strftime("%Y-%m-%d %H:%M:%S")}] {Style.BRIGHT}Output: {output}')
    return output

def git_commit(working_dir, message):
    print(f'{Fore.YELLOW}[{time.strftime("%Y-%m-%d %H:%M:%S")}] {Style.BRIGHT}Committing changes with message: {message}')
    command = ['git', 'commit', '-m', message]
    output = run_command(command, working_dir)
    print(f'{Fore.GREEN}[{time.strftime("%Y-%m-%d %H:%M:%S")}] {Style.BRIGHT}Output: {output}')
    return output

def git_push(working_dir):
    print(f'{Fore.YELLOW}[{time.strftime("%Y-%m-%d %H:%M:%S")}] {Style.BRIGHT}Pushing changes to remote repository')
    command = ['git', 'push']
    output = run_command(command, working_dir)
    print(f'{Fore.GREEN}[{time.strftime("%Y-%m-%d %H:%M:%S")}] {Style.BRIGHT}Output: {output}')
    return output

def main():
    working_dir = 'C:/Users/admin/github/LimeV2-FREE'
    
    # Example of adding a file to the repo
    files_to_add = [
        '.\\LimeV2VENV\\Lib\\site-packages\\setuptools\\tests\\config\\__init__.py',
        '.\\LimeV2VENV\\Lib\\site-packages\\pip\\_vendor\\truststore\\_windows.py',
        '.\\LimeV2VENV\\Lib\\site-packages\\requests\\_internal_utils.py'
    ]

    for file in files_to_add:
        git_add(working_dir, file)
    
    # Commit and push the changes
    commit_message = 'Fixed ignored files issue in LimeV2VENV'
    git_commit(working_dir, commit_message)
    git_push(working_dir)

if __name__ == '__main__':
    main()
