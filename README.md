# YouTube Ad Skipper
[Watch the demo](https://youtu.be/gYRYjxz8SNo)
A small Python automation script that watches your screen and clicks the **Skip Ad** button on YouTube as soon as it appears.

It works with image recognition: you give it a screenshot of the skip button, and it repeatedly scans the screen for a match. When it finds one, it moves the mouse to that spot and clicks.

## How it works

1. Waits 5 seconds at startup so you can switch to the YouTube window.
2. Every second, takes a screenshot and searches it for `skip2.png` using `pyautogui.locateOnScreen()` (template matching, with a `confidence` threshold handled by OpenCV).
3. If a match is found, it calculates the center of the matched region with `pyautogui.center()`, moves the cursor there, and clicks.
4. Waits 2 seconds after a click so the same button is not clicked twice, then keeps scanning.

## Requirements

- Python 3.8+
- Libraries: `pyautogui`, `opencv-python`, `pillow` (listed in `requirements.txt`)

## Setup and usage

```bash
git clone https://github.com/bhardwaajsingh0/youtube-ad-skipper.git
cd youtube-ad-skipper
pip install -r requirements.txt
python youtube_ad_skipper.py
```

When you see `Bot starting in 5 seconds...`, switch to your YouTube window. Stop the script with `Ctrl + C`.

### The reference image

`skip2.png` is a cropped screenshot of the YouTube skip button taken on my screen. Matching depends on size, scaling and theme, so if the bot does not detect the button on your setup, replace `skip2.png` with your own screenshot of the button (keep the same file name) at the browser zoom and screen resolution you actually use.

## Configuration

| Setting | Where | What it does |
|---|---|---|
| `confidence=0.5` | `locateOnScreen(...)` | How closely the screen must match the image. Higher values (e.g. `0.8`) give fewer false clicks but may miss the button if it looks slightly different. |
| `time.sleep(1)` | end of loop | How often the screen is scanned. |
| `time.sleep(2)` | after click | Pause after clicking to avoid double clicks. |

## Limitations

- Works only when the skip button is visible on screen and looks similar to the reference image (same scale and theme).
- It controls the real mouse, so it will click wherever the button is on screen. Keep the YouTube window visible while it runs.
- When no button is on screen, the library may raise a "not found" exception, which the script catches and prints as `Error:`. This is expected.
- The script only clicks the Skip button when YouTube shows it. It does not block or remove ads.

## Built with

- Python
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- OpenCV (used by PyAutoGUI for the `confidence` matching)

## License

Personal project, built for learning purposes.
