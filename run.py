from app import create_app
import sys

app = create_app()

if __name__ == '__main__':
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    app.run(debug=True, host=host, port=port)

