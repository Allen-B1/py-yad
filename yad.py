import subprocess

def dialog(title, text, buttons={0:"Close"}):
	arr = ["yad", "--center", "--text=" + text, "--title=" + title]
	for bid, blabel in buttons:
		arr.append("--button=" + blabel + ":" + bid)
	return subprocess.run(arr)
