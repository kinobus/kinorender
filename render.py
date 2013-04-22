import cairosvg
import Image
import tempfile


def plot_layer_png():
    return None

def render_kinome(plotdataRaw):
    import pdb; pdb.set_trace()
    svg_fd, svg_fname = tempfile.mkstemp()
    with open(svg_fname, 'w') as plotdataSVG:
        plotdataSVG.write(plotdataRaw)
    svgData = cairosvg.svg2png(svg_fname)
    import pdb; pdb.set_trace()
    print svgData
