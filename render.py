import cairosvg
import Image
import tempfile
from base64 import b64encode
from os import remove


def render_kinome(plotdataSVG):
    # convert plotted data from svg to png
    plotdataPNG = cairosvg.svg2png(plotdataSVG)
    plotPNG_fd, plotPNG_fname = tempfile.mkstemp()

    # write plotted png overlay to temp file
    with open(plotPNG_fname, 'w') as plotPNG_file:
        plotPNG_file.write(plotdataPNG)

    # open plot, bg as images
    foregroundPNG = Image.open(plotPNG_fname)
    backgroundPNG = Image.open('static/kinome.png')
    backgroundPNG.paste(foregroundPNG, (0, 0), foregroundPNG)

    # save new rendered image to temp file
    renderPNG_fd, renderPNG_fname = tempfile.mkstemp()
    backgroundPNG.save(renderPNG_fname, 'PNG')

    # load rendered png
    with open(renderPNG_fname, 'rb') as renderPNG_file:
        renderPNG = renderPNG_file.read()

    # remove both temp png files
    remove(plotPNG_fname)
    remove(renderPNG_fname)

    return b64encode(renderPNG)
