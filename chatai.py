import openai
from docopt import docopt


class AIChat:
	def __init__(self):
		# 作成したOpenAIのAPIキーを設定する。
		openai.api_key = '< Copy APIKey >'

	def response(self, user_input):
		# OpenAIのGPT-3モデルを使用して、応答を生成する。
		response = openai.Completion.create(
			engine="text-davinci-003",
			prompt=user_input,
			max_tokens=1024,
			temperature=0.5, # 生成する応答の多様性
		)

		# 応答のテキスト部分を取り出して返す。
		return response['choices'][0]['text']

def main():
	
	__doc__ = """
Usage:
	chatai.py [--version][--help]
	chatai.py --chat

Options:
	-h --help        ヘルプを表示する。
	--version        バージョンを表示する。
	"""

	args = docopt(__doc__)
	# print(args)

	if args['--version']:
		print('AIChat 1.0')
		return

	if args['--chat']:
		# AIChatのインスタンスを作成する。
		chatai = AIChat()

		print('>> AIChat: こんにちは、私はAIChatです。')
		print('>> AIChat: （終わるときは「終了」と入力してください。）')

		while True:
			# ユーザーからの入力を受け取る。
			user_input = input('>> User: ')

			# ユーザーからの入力が「終了」だった場合にプログラムを終了する。
			if user_input == '終了':
				break

			# chataiからの応答を取得する。
			response = chatai.response(user_input)
			print('>> AIChat: ' + response)

		print('>> AIChat: ありがとうございました。')
		print('>> AIChat: またお話ししましょう。')


if __name__ == '__main__':
	main()

