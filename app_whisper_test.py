from flask import Flask, render_template, request, jsonify
import openai
import os, json, tempfile

app = Flask(__name__, static_folder="./templates", static_url_path="")

# OpenAI APIのセットアップ
openai.api_key = 'YOUR_API_KEY'  # あなたのOpenAI APIキー


@app.route('/upload-audio', methods=['POST'])
def upload_audio():
	try:
		audio_data = request.files['audio'].read()
		with tempfile.NamedTemporaryFile(mode='wb', delete=True, suffix=".wav") as temp_file:
			temp_file.write(audio_data)
			with open(temp_file.name, 'rb') as temp_read_file:
				response = openai.Audio.transcribe("whisper-1", temp_read_file)

		transcription = response['text']
		print(transcription)
		return jsonify({"transcription": transcription})
	except Exception as e:
		print(f"Exception: {str(e)}")
		return jsonify({"error": "Server Error"}), 500

@app.route("/")
def index():
    return render_template("index.html")

# OpenAI APIのセットアップ
import config

if __name__ == '__main__':
	openai.api_key = config.keys["openai_api_key"]
	#app.run(debug=True)
	app.run(host="0.0.0.0", port=8080, debug=True)
