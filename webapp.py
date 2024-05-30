import subprocess

def launch_chromium_kiosk():
    url = "http://192.168.1.198:8080"  # Update with the correct IP address and port
    with open('/dev/null', 'w') as fnull:
        subprocess.run([
            "chromium-browser",
            "--disable-gpu",
            "--kiosk",
            "--app=" + url
        ], stderr=fnull)


if __name__ == "__main__":
    launch_chromium_kiosk()
