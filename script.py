import subprocess

def get_current_branch():
    try:
        # 'git rev-parse --abbrev-ref HEAD' コマンドを実行して現在のブランチ名を取得
        result = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], universal_newlines=True)
        return result.strip()
    except subprocess.CalledProcessError:
        return None

def main():
    current_branch = get_current_branch()

    if current_branch == 'cat':
        print('hello')
    else:
        print(f'Not on "cat" branch. Switch to "cat" branch to see "hello".')

if __name__ == '__main__':
    main()
