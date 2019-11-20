from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run('127.0.0.1',threaded=True)

# threaded 开启多线程
# processes = 1 开启多进程  进程数
