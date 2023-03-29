from http.server import HTTPServer, BaseHTTPRequestHandler

APP_HOST = 'localhost'
APP_PORT = 8000


class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def _htnl(self, message, message2):
        content = (f'<html>'
                   f'<body>'
                   f'<h1>{message}</h1>'
                   f'<h3>{message2}</h3>'
                   f'</body>'
                   f'</html>')
        return content.encode('utf8')

    def do_GET(self):
        self._set_headers()
        message = 'Nihao!!'
        message2 = """Я пиздатый, ахуеный, современный, невъебенный.
                    Шел отдельно, без системы прямо к цели, я бесценен.
                    Цепь танцует вальс на теле, твоя сука на прицеле.
                    Грязный Морти возьмет Грэмми, черт возьми, я стану первым.
                    Молодой скейт-ублюдок, я сжигаю те купюры.
                    И катаюсь с Фарой в туре, так что вытри свои слюни.
                    Выкупай как я ебу их, даже стрельнув холостую.
                    Грязный Морти здесь кастует.
                    Я не пру, я, блять, пиздую."""
        self.wfile.write(self._htnl(message, message2))


def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run_server(handler_class=SimpleGetHandler)
