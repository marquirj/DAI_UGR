#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, redirect, render_template, request
from PIL import Image
import mandelbrot
app = Flask(__name__)

@app.route('/')
def hola():
 return "Ingresa mandelbrot y cada parámetro separado por /, para visualizar mandelbrot"


@app.route('/sol/<x1>/<y1>/<x2>/<y2>/<ancho>/<iteraciones>/<nombreFicheroPNG>',methods=['GET'])

def sol(x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPNG):
	# drawing area
	xa = float(x1)
	xb = float(x2)
	ya = float(y1)
	yb = float(y2)
	maxIt = int(iteraciones)
	# image size
	imgx = int(ancho)
	imgy = int(abs (yb - ya) * imgx / abs(xb - xa));
	
	image = Image.new("RGB", (imgx, imgy))

	for y in range(imgy):
		zy = y * (yb - ya) / (imgy - 1)  + ya
		for x in range(imgx):
			zx = x * (xb - xa) / (imgx - 1)  + xa
			z = zx + zy * 1j
			c = z
			for i in range(maxIt):
				if abs(z) > 2.0: break 
				z = z * z + c

			if (i >= maxIt):
				image.putpixel((x, y), (0, 0, 0))
			else:
				image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
	
	image.save(nombreFicheroPNG, "PNG")
	return "hecho"
if __name__ == '__main__':
	app.run(host='0.0.0.0')
