from flask import Flask, app, request, jsonify
import pandas as pd

def create_app():
    app = Flask(__name__)

    @app.route("/convert", methods=['POST'])
    def convert():
        if request.method == "POST":
            json_data = request.json
            if not json_data:
                return {"message": "please provide valid data"}
            df = pd.DataFrame({'label':json_data["alpha"]})
            df['values'] = [check_ascii(sub) for sub in df['label']]
            ascii_values = df['values'].to_json()
            return {"ascii_values": ascii_values}

    def check_ascii(ele):
        if ord(ele) < 96 and ord(ele) < ord('H'):
            return ord(ele) * 10
        elif ord(ele) > 96 and ord(ele) < ord('h'):
            return ord(ele) * 10
        else:
            return 0

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
