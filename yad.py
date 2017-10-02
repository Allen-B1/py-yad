"""Yet Another Dialog in python

Create advanced dialogs

HOMEPAGE
	https://github.com/allen-b1/

KWARGS
	Keyword arguments:
	 - width: width of window
	 - height: height of window
"""

__name__ = "yad"
__author__ = "Allen-B1"

import subprocess

# Parse KWARGS
def _parse_kwargs(kwargs, data):
	if "width" in kwargs:
		data.append("--width=" + str(kwargs["width"]))
	if "height" in kwargs:
		data.append("--height=" + str(kwargs["height"]))

def dialog(text, title, buttons, **kwargs):
	"""Show basic dialog with custom buttons, where buttons is an array. For **kwargs, see the KWARGS section

	The first button is the default button, and the second one is returned if the user closes the window without clicking a button

	EXAMPLE
		yad.dialog("<b>Lorum ispem</b> dolor...", "Get it?", ["Got it!", "Don't understand"], width=500, height=300)

	RETURNS
		The index of which button was clicked
	"""
	arr = ["yad", "--center", "--text=" + str(text), "--title=" + str(title)]
	_parse_kwargs(kwargs, arr)
	if type(buttons) is list:
		buttons = enumerate(buttons)
	for bid, blabel in buttons:
		arr.append("--button=" + str(blabel) + ":" + str(bid))
	return subprocess.run(arr).returncode

def info(text, title="Info", **kwargs):
	"""Show basic dialog with 'Close' button"""
	dialog(text, title, ["Close"], **kwargs)

def entry(text, title, buttons=["OK", "Cancel"]):
	"""Show dialog with an entry (textbox). text, title, and buttons are the same as yad.dialog

	RETURNS
		What the user entered, or None if the user clicked the second button (i.e. Cancel)
	"""
	arr = ["yad", "--center", "--entry", "--text=" + str(text), "--title=" + str(title)]
	if type(buttons) is list:
		buttons = enumerate(buttons)
	for bid, blabel in buttons:
		arr.append("--button=" + str(blabel) + ":" + str(bid))
	ret = subprocess.run(arr)
	if ret.returncode != 1:
		return ret.stdout
	else:
		return None

def file(text, title="Open File", buttons=["OK", "Cancel"], default_file="/home/"):
	"""Show a filepicker dialog. text, title, and buttons are the same as yad.dialog

	RETURNS
		The path to the file, or None if the user clicked the second button (i.e. Cancel)
	"""
	arr = ["yad", "--center", "--file", "--text=" + str(text), "--title=" + str(title), "--filename=" + default_file]
	if type(buttons) is list:
		buttons = enumerate(buttons)
	for bid, blabel in buttons:
		arr.append("--button=" + str(blabel) + ":" + str(bid))
	ret = subprocess.run(arr)
	if ret.returncode != 1:
		return ret.stdout
	else:
		return None
