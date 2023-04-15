import datetime
import openai
from docopt import docopt

class StrOperation:
	def get_base_date(self, user_input):
		split_input = user_input.split('@')
		if len(split_input) < 2:
			return str(datetime.date.today())
		else:
			return split_input[1].strip()
	
	def extract_code_block(self, text):
		start = '```'
		end = '```'
		rtnstr = ""
		start_idx = text.find(start)
		end_idx = text.find(end, start_idx + len(start))
		if start_idx != -1 and end_idx != -1:
			rtnstr = text[start_idx+len(start):end_idx].strip()
		return rtnstr


class AIChat:
	def __init__(self):
		# 作成したOpenAIのAPIキーを設定する。
		openai.api_key = '< Copy APIKey >'

	def response(self, user_input):
		StrOpe = StrOperation()
		# OpenAIのGPT-3モデルを使用して、応答を生成する。
		# response = openai.Completion.create(
		# 	engine="text-davinci-003",
		# 	prompt=user_input,
		# 	max_tokens=1024,
		# 	temperature=1.0, # 生成する応答の多様性
		# )
		base_date = StrOpe.get_base_date(user_input)
		split_date = base_date.split(',')

		response = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			messages=[
				{"role": "system", "content": "あなたは、私のスケジュール管理者です。" },
				{"role": "system", "content": "問われた内容を実行するためのフローを考えてください。" },
				{"role": "system", "content": "また、そのフローのスケジュールを'タスク','日数','開始日','終了日'の順番でカンマ区切りで答えてください。" },
				{"role": "system", "content": f"スケジュールは{split_date[0].strip()}から{split_date[1].strip()}の期間で考えてください。" },
				# {"role": "system", "content": "解答はCSV形式で答えてください。" },
				{"role": "user", "content": user_input }
			]
		)

		# 応答のテキスト部分を取り出して返す。
		# return response['choices'][0]['text']
		return response["choices"][0]["message"]["content"]

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
		strOpe = StrOperation()

		print('>> AIChat: こんにちは、私はAIChatです。')
		print('>> AIChat: （終わるときは「終了」と入力してください。）')

		while True:
			# ユーザーからの入力を受け取る。
			user_input = input('>> User: ')

			# ユーザーからの入力が「終了」だった場合にプログラムを終了する。
			if user_input == '終了' or user_input == 'exit':
				break

			# chataiからの応答を取得する。
			response = chatai.response(user_input)
			print('>> AIChat: ' + response)

			strcsv = strOpe.extract_code_block(response)
			print('>> AIChat: \n' + strcsv)

		print('>> AIChat: ありがとうございました。')
		print('>> AIChat: またお話ししましょう。')


if __name__ == '__main__':
	main()

