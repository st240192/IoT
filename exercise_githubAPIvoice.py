import base64
import requests

GitHub_Token =  'トークンかいてね'
REPO_NAME = 'st240192/IoT'
FILE_PATH = 'voice1.mp3'
UPLOAD_PATH = 'voice1.mp3'
COMMIT_MESSAGE = '音声ファイルを追加したよ'

with open(FILE_PATH, "rb") as f:
    content = base64.b64encode(f.read()).decode()

url = f'https://api.github.com/repos/{REPO_NAME}/contents/{UPLOAD_PATH}'

data = {
    'message': COMMIT_MESSAGE,
    'content': content
}

headers = {
    'Authorization': f'token {GitHub_Token}'
}

res = requests.put(url, json=data, headers=headers)

if res.status_code == 201:
    print('音声をGitHubにアップロードしました！')
    print('URL:',res.json()['content']['html_url'])
else:
    print('エラーが発生しました:')
    print(res.status_code, res.text)
