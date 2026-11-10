# -*- coding: utf-8 -*-
import http.server
import socketserver
import webbrowser
import socket
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {format%args}\n")

if __name__ == '__main__':
    local_ip = get_local_ip()
    print("=" * 65)
    print("🎬 电影学论文语料库 & 论述答题锦囊 本地网站已就绪！")
    print(f"👉 本机电脑访问地址: http://localhost:{PORT}")
    print(f"📱 手机/平板/同WiFi设备访问: http://{local_ip}:{PORT}")
    print("=" * 65)
    print("按 Ctrl + C 即可关闭本地服务器。\n")

    # Open browser automatically on localhost
    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n已成功停止网站服务。")
