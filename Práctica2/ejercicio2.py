#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/hola')
def hola():
	return render_template('index.html')
if __name__ == '__main__':
	app.run(host='0.0.0.0')
