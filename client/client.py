from http.server import BaseHTTPRequestHandler, HTTPServer
import requests, time

def run():
    time.sleep(10)
    while True:
        resp = requests.get("http://172.17.0.1:8468")
        print(resp.content)
        time.sleep(5)

if __name__ == '__main__':
    run()