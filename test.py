from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # NOTE: import FaceRegoc inside function, otherwise might not work with Flask(reason unknown)
    import FaceRecog
    # Get frame or player info from FaceRecog module
    # getFrameOrInfo function will keep yielding jpeg frame until all player information is found
    return Response(FaceRecog.getFrameOrInfo(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

