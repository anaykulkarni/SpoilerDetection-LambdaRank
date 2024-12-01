from rich import print as rich_print

import numpy as np

import matplotlib
from matplotlib import pyplot as plt
from matplotlib import cm

RICH_x = np.linspace(1.0, 0.0, 50)
RICH_rgb = (matplotlib.colormaps.get_cmap(plt.get_cmap('RdYlBu'))(RICH_x)[:, :3] * 255).astype(np.int32)[range(5, 50, 5)]


def print_with_probs(words, probs, prefix=None):
  def fmt(x, p, is_first=False):
    ix = int(np.clip(p * RICH_rgb.shape[0], 0, RICH_rgb.shape[0] - 1))
    r, g, b = RICH_rgb[ix]
    if is_first:
      return f'[rgb(0,0,0) on rgb({r},{g},{b})]{x}'
    else:
      return f'[rgb(0,0,0) on rgb({r},{g},{b})] {x}'
  output = []
  if prefix is not None:
    output.append(prefix)
  for i, (x, p) in enumerate(zip(words, probs)):
    output.append(fmt(x, p, is_first=i == 0))
  rich_print(''.join(output))

# # DEMO

# # Show range of colors.

# for i in range(RICH_rgb.shape[0]):
#   r, g, b = RICH_rgb[i]
#   rich_print(f'[bold rgb(0,0,0) on rgb({r},{g},{b})]hello world rgb({r},{g},{b})')

# # Example with words and probabilities.

# words = ['the', 'brown', 'fox']
# probs = [0.14, 0.83, 0.5]
# print_with_probs(words, probs)