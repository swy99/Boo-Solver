from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from algorithm import Solution
from optical_recognition import OpticalRecognizer
import cv2
app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)
        path = filename
        img = cv2.imread(path)
        offset = (686,1796)
        state = OpticalRecognizer.interp(img, offset=offset)
        plan = Solution.solve(state)
        plan = plan[::-1]
        res = ""
        for i in range(len(plan)):
            res += f"{i+1}. wear [{', '.join(list(plan[i][0]))}] and paint {plan[i][1]}. </br>"
        return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2754)