# thor-alerts
Desktop app for receiving alerts from THOR, written with wxPython.

## Development

### Linux

> [!IMPORTANT]
> To develop on Linux, you will need Python 3.11 or newer and **you must install wxPython from your distrobution's repository**.
> Attempting to install wxPython from pip will attempt to build parts of it from source, which will likely fail.

On Fedora, the package is called `python3-wxpython4`.

Clone the repository and create a venv.

```bash
python3 -m venv .venv/ --system-site-packages
```

Install requirements from `requirements.linux.txt`.

```bash
(.venv) pip install -r requirements.linux.txt
```

## Licenses
The code for this project is licensed under the [MIT License](LICENSE).

`thoricons`, which are found as PNG files in this repository under `/icongenerator/img` and `/assets/icons` are (C) 2024 Eoghan O'Bogail, All Rights Reserved.

## Troubleshooting
### Doesn't minimise to the taskbar in Wayland

You need to launch the program with the `GDK_BACKEND=x11` environment variable set. 
