import logging
import os
import time
from urllib.parse import unquote

import requests
from flask import Flask, send_file, abort, request

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'request_record.log')
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d-%H-%M-%S',
                    filename=log_file_path,
                    filemode='a')

app = Flask(__name__)


@app.route('/<path:filename>')
def get_file(filename):
    request_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # ip_addr = request.remote_addr
    ip_addr = request.headers.getlist("X-Forwarded-For")[0]
    user_agent = request.user_agent.string
    logging.warning(
        f'[myrecord]-[TIME:"{request_time}"]-[IPAddr:"{ip_addr}"]-[UA:"{user_agent}"]-'
        f'[GET:"{filename}"]-[LOCATION:"{get_geo_location(ip_addr)}"]')

    requested_file = unquote(filename)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), requested_file)
    print(f" !!! {requested_file} - {file_path} !!! ")

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file_path)
        if ext.lower() in ('.jpg', '.jpeg', '.png'):
            try:
                return send_file(file_path)
            except FileNotFoundError:
                abort(404)
        else:
            abort(404, description='File Not Supported')
    else:
        abort(404, description='File Not Found')


def get_geo_location(ip_address):
    # 使用免费的ipinfo.io服务
    url = f"http://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        # 检查响应状态
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return f"Error: Unable to get location for IP {ip_address}. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=12315)
