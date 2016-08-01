import Image, ImageDraw

import os
import sys
import glob

#ffmpeg -i hotRod.mp4 -r 1 /Volumes/Untitled/Frames/HotRod/output-%0000d.png

inputDir = sys.argv[1]
outputDir = sys.argv[1]
if len(sys.argv) > 2:
	outputDir = sys.argv[2]

frameCount = len([name for name in os.listdir(inputDir) if os.path.isfile(os.path.join(inputDir, name))])

outIm = Image.new("RGB", (frameCount, 2048))
draw = ImageDraw.Draw(outIm)

index = 0
for filename in glob.glob(os.path.join(inputDir, '*.png')):
	im = Image.open(filename)
	print filename
	pix = im.load()
	
	red = 0
	green = 0
	blue = 0
	(x,y) = im.size
	totalCount = x*y
	
	for i in range(0,x):
		for j in range(0,y):
			(r,g,b) = pix[i,j]
			red += r
			green += g
			blue += b
	
	red /= totalCount
	blue /= totalCount
	green /= totalCount

	rgba = (red, green, blue, 255)

	draw.line([(index, 0), (index, 2048)], rgba)
	index += 1

outFile = open(outputDir+"/output_final.png", "w")
outIm.save(outFile, 'PNG')