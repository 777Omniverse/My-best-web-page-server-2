from flask import Flask, request, render_template_string
import requests
import os
from time import sleep
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        if token_type == 'single':
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for message1 in messages:
                        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                        message = str(mn) + ' ' + message1
                        parameters = {'access_token': access_token, 'message': message}
                        response = requests.post(api_url, data=parameters, headers=headers)
                        if response.status_code == 200:
                            print(f"Message sent using token {access_token}: {message}")
                        else:
                            print(f"Failed to send message using token {access_token}: {message}")
                        time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {access_token}: {message}")
                    print(e)
                    time.sleep(30)

        elif token_type == 'multi':
            token_file = request.files['tokenFile']
            tokens = token_file.read().decode().splitlines()
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for token in tokens:
                        for message1 in messages:
                            api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                            message = str(mn) + ' ' + message1
                            parameters = {'access_token': token, 'message': message}
                            response = requests.post(api_url, data=parameters, headers=headers)
                            if response.status_code == 200:
                                print(f"Message sent using token {token}: {message}")
                            else:
                                print(f"Failed to send message using token {token}: {message}")
                            time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {token}: {message}")
                    print(e)
                    time.sleep(30)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𓆩๛⃝𝗝𝗮𝗰𝗸𝘀𝗼𝗻 ‣᭄𓆪 😈 FULL TRANSPARENT UI</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            margin: 0;
            min-height: 100vh;
            font-family: 'Courier New', monospace;
            overflow: hidden;
            position: relative;
            color: #fff459; /* Neon yellow text */
        }

        /* Video Background */
        #videoBackground {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            object-fit: cover;
        }

        /* Fully Transparent Container */
        .container-box {
            background: rgba(0, 0, 0, 0); /* 100% Transparent */
            border: 3px solid #ff5959; /* Neon red border */
            border-radius: 10px;
            padding: 20px;
            width: 90%;
            max-width: 500px;
            margin: 50px auto;
            position: relative;
            backdrop-filter: blur(1px); /* Slight blur for better readability */
        }

        /* Transparent Inputs */
        .custom-input {
            background: rgba(0, 0, 0, 0) !important; /* 100% Transparent */
            border: 3px solid #55ff00 !important; /* Neon green border */
            color: #55ff00 !important; /* Neon green text */
            margin: 10px 0;
        }

        .custom-input::placeholder {
            color: #55ff00 !important; /* Neon green placeholder with 40% opacity */
        }

        /* Transparent Buttons */
        .custom-btn {
            background: rgba(0, 0, 0, 0) !important; /* 100% Transparent */
            border: 3px solid #55ff00 !important; /* Neon green border */
            color: #55ff00 !important; /* Neon green text */
            width: 100%;
            margin-top: 15px;
            transition: all 0.3s ease;
        }

        .custom-btn:hover {
            background: rgba(0, 255, 136, 0.1) !important; /* Slight hover effect */
            box-shadow: 0 0 10px #55ff00; /* Neon green glow on hover */
        }

        /* Status Box with Purple Outline */
        .status-box {
            text-align: center;
            margin-top: 20px;
            padding: 10px;
            border: 3px solid #c800ff; /* Neon purple border */
            background: rgba(0, 0, 0, 0); /* 100% Transparent */
            /* Glow removed */
        }

        /* Status Text Color */
        #statusText {
            color: #55ff00; /* Neon green text */
        }

        /* STOP Button Text Color */
        #stopBtn {
            color: #ff0000 !important; /* Red color with higher specificity */
        }
    </style>
</head>
<body>
    <!-- Video Background -->
    <video id="videoBackground" autoplay muted loop>
        <source src="https://github.com/777Omniverse/Video/raw/refs/heads/main/6fe9bebe43492b6ce061a95cd7644de4_t4_resized%20(1).mp4" type="video/mp4">
        Your browser does not support HTML5 video.
    </video>

    <div class="container-box">
        <h3 class="text-center mb-4">𝗖𝗬𝗕𝗘𝗥 𝗔𝗧𝗧𝗔𝗖𝗞 𝗖𝗢𝗡𝗧𝗥𝗢𝗟 v3.0</h3>
        
        <form id="controlForm" action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <select class="form-select custom-input" id="tokenType" name="tokenType">
                    <option value="single">🔑 𝗦𝗶𝗻𝗴𝗹𝗲 𝗧𝗼𝗸𝗲𝗻</option>
                    <option value="multi">🔑🔑 𝗠𝘂𝗹𝘁𝗶 𝗧𝗼𝗸𝗲𝗻</option>
                </select>
            </div>

            <div id="singleTokenSection">
                <input type="text" class="form-control custom-input" name="accessToken"
                    placeholder="🔑 𝙀𝙣𝙩𝙚𝙧 𝘼𝙘𝙘𝙚𝙨𝙨 𝙏𝙤𝙠𝙚𝙣" required>
            </div>

            <div id="multiTokenSection" style="display: none;">
                <input type="file" class="form-control custom-input" name="tokenFile"
                    accept=".txt">
            </div>

            <input type="text" class="form-control custom-input" name="threadId"
                placeholder="🎯 �𝙏𝙖𝙧𝙜𝙚𝙩 𝙄𝙙" required>

            <input type="text" class="form-control custom-input" name="kidx"
                placeholder="👤 𝙃𝙖𝙩𝙚𝙧𝙨 𝙉𝙖𝙢𝙚" required>

            <input type="file" class="form-control custom-input" name="txtFile"
                accept=".txt" required>

            <input type="number" class="form-control custom-input" name="time"
                placeholder="⚡ �𝙎𝙥𝙚𝙚𝙙 (seconds)" min="1" required>

            <div class="d-grid gap-2">
                <button type="submit" class="btn custom-btn" id="startBtn">🚀 𝙎𝙏𝘼𝙍𝙏</button>
                <button type="button" class="btn custom-btn" id="stopBtn" style="display: none;">⛔ 𝙎𝙏𝙊𝙋</button>
            </div>

            <div class="status-box">
                <p id="statusText">STATUS: IDLE</p>
            </div>
        </form>
    </div>

    <script>
        document.getElementById('tokenType').addEventListener('change', function() {
            const showMulti = this.value === 'multi';
            document.getElementById('singleTokenSection').style.display = showMulti ? 'none' : 'block';
            document.getElementById('multiTokenSection').style.display = showMulti ? 'block' : 'none';
        });

        let processInterval;
        document.getElementById('startBtn').addEventListener('click', () => {
            if(!processInterval) {
                const intervalTime = document.querySelector('input[type="number"]').value * 1000;
                processInterval = setInterval(() => {
                    console.log('Command sent!');
                }, intervalTime);
                
                document.getElementById('startBtn').style.display = 'none';
                document.getElementById('stopBtn').style.display = 'block';
                document.getElementById('statusText').innerHTML = 'STATUS: <span style="color:#55ff00">ACTIVE</span>';
            }
        });

        document.getElementById('stopBtn').addEventListener('click', () => {
            clearInterval(processInterval);
            processInterval = null;
            document.getElementById('startBtn').style.display = 'block';
            document.getElementById('stopBtn').style.display = 'none';
            document.getElementById('statusText').innerHTML = 'STATUS: <span style="color:#ff00fb">IDLE</span>';
        });
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 21096))
    app.run(host='0.0.0.0', port=port, debug=True)
