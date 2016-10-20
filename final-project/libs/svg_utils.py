"""
Utility for SVG manipulation, inspired by the utils from write-rnn-tensorflow to a large extend:
https://github.com/hardmaru/write-rnn-tensorflow
"""

import svgwrite

def initiate(size_x, size_y, filename):
    """Initiate SVG drawing.

    Parameters
    ----------
    size_x : int
        Size along the X axis.
    size_y : int
        Size along the Y axis.
    filename : filesystem filename

    Returns
    -------
    dwg : Drawing object.
    """
    dims = (size_x, size_y)
    dwg = svgwrite.Drawing(filename, size=dims)
    dwg.add(dwg.rect(insert=(0, 0), size=dims,fill='white'))
    return dwg
