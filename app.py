from flask import Flask, render_template, jsonify, request
import config
import openai
import gpt
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="logs2.log",
    format ="%(asctime)s [%(levelname)s] %(message)s"
)


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods = ['POST', 'GET'])
def index():
    app.logger.info("Hello logs!")
    logging.info("Lol lets log something here. its so easy")
    if request.method == 'POST':
        prompt = request.form['prompt']
        res = {}
        res['answer'] = gpt.generateChatResponse(prompt)
        return jsonify(res), 200
    
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
