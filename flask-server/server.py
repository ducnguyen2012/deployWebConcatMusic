from flask import Flask, request, jsonify, send_from_directory
import os
from conCatFile import conCatFile

app = Flask(__name__)

# Directory where uploaded files will be saved
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Initialize global variable
lastEstimateTime = 0

@app.route('/upload', methods=['POST'])
def upload_file():
    global lastEstimateTime  # Declare that we are using the global variable

    if 'files' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    files = request.files.getlist('files')
    
    if not files:
        return jsonify({'error': 'No file part in request'}), 400

    file_paths = []
    for file in files:
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Save the file to the upload folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        file_paths.append(file_path)

    # Concatenate files using conCatFile
    concat = conCatFile(os.path.join(os.getcwd(), 'uploads\\'))
    estimateTime, res = concat.conCatFileMP3()  # Assuming this method returns the filename of the concatenated file
    lastEstimateTime = estimateTime  # Update the global variable
    print(f"Estimate Time: {lastEstimateTime}")
    print(f"Result: {res}")
    return jsonify({'message': 'Files uploaded and concatenated successfully!', 'result_file': res, 'estimate_time': lastEstimateTime}), 200

@app.route('/DownloadPage', methods=['GET'])
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])  # List files in the upload directory
    fileDownload = os.listdir(app.config['DOWNLOAD_FOLDER'])
    print(f"Files: {fileDownload}")
    print(f"Last Estimate Time: {lastEstimateTime}")
    return jsonify({'Files': fileDownload, 'estimate_time': lastEstimateTime})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)




# from flask import Flask, request, jsonify, send_from_directory
# import os
# from conCatFile import conCatFile

# app = Flask(__name__)

# # Directory where uploaded files will be saved
# UPLOAD_FOLDER = 'uploads'
# DOWNLOAD_FOLDER = 'downloads'
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
    
# if not os.path.exists(DOWNLOAD_FOLDER):
#     os.makedirs(DOWNLOAD_FOLDER)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# # Initialize global variable
# lastEstimateTime = 0

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     global lastEstimateTime  # Declare that we are using the global variable

#     if 'files' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400

#     files = request.files.getlist('files')
    
#     if not files:
#         return jsonify({'error': 'No file part in request'}), 400

#     file_paths = []
#     for file in files:
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'}), 400

#         # Save the file to the upload folder
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
#         file_paths.append(file_path)

#     # Concatenate files using conCatFile
#     concat = conCatFile(os.path.join(os.getcwd(), 'uploads\\'))
#     estimateTime, res = concat.conCatFileMP3()  # Assuming this method returns the filename of the concatenated file
#     lastEstimateTime = estimateTime  # Update the global variable
#     print(res)
#     print(f"Estimated time for concatenation: {estimateTime:.2f} seconds")
#     return jsonify({'message': 'Files uploaded and concatenated successfully!', 'result_file': res, 'Estimate time to finish': lastEstimateTime}), 200

# @app.route('/DownloadPage', methods=['GET'])
# def list_files():
#     files = os.listdir(app.config['UPLOAD_FOLDER'])  # List files in the upload directory
#     fileDownload = os.listdir(app.config['DOWNLOAD_FOLDER'])
#     print(lastEstimateTime)
#     return jsonify({'Files': fileDownload, 'estimate_time': lastEstimateTime})

# @app.route('/download/<filename>', methods=['GET'])
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
