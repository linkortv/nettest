import speedtest

def sptest():
    test = speedtest.Speedtest(secure=1)
    download = test.download()
    upload = test.upload()
    ping = test.results.ping
    return f"Download: {download / 1024 / 1024:.2f} Mbit/s\nUpload: {upload / 1024 / 1024:.2f} Mbit/s\nPing: {ping} ms"

def sptest_short():
    test = speedtest.Speedtest(secure=1)
    download = test.download()
    return f"Speed: {download / 1024 / 1024:.2f} Mbit/s"