#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def hola():
	return "Si ingresa Zerjillo, se saludará a ese usuario, si ingresa Pepe, se saludara a ese usuario"
@app.errorhandler(404)
def page_not_found(error):
  return "Pagina no encontrada", 404
@app.route('/user/zerjillo')
def hola_zerjillo():
	return 'Hola Zerjillo'
@app.route('/user/pepe')
def hola_pepe():
	return 'Hola Pepe'
@app.route('/user/<name>')
def redirige(name):
	if name=='zerjillo':
		return redirect(url_for('hello_zerjillo'))
	elif name == 'pepe':
		return redirect(url_for('hello_pepe'))	
	else:
		return redirect(url_for('page_not_found(404)'))
if __name__ == '__main__':
	app.run(host='0.0.0.0')
