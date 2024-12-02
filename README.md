# thor-alerts
Desktop app for receiving alerts from THOR, written with wxPython.

## Licenses
The code for this project is licensed under the [MIT License](LICENSE).

`thoricons`, which are found as PNG files in this repository under `/icongenerator/img` and `/assets/icons` are (C) 2024 Eoghan O'Bogail, All Rights Reserved.

## Troubleshooting
### Doesn't minimise to the taskbar in Wayland

You need to launch the program with the `GDK_BACKEND=x11` environment variable set. 
