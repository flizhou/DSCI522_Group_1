# author: Fanli Zhou
# date: 2020-01-16

"""This script downloads a data set and stores the data set as a csv file.

Usage: src/download_save_data.py --url=<url> --output=<output> 

Options:
--url=<url>           URL to download the data set
--output=<output>     Local file path to save the data set as a csv file
"""
import pandas as pd
import requests
from docopt import docopt
opt = docopt(__doc__)

def main(url, output):

  try: 
    request = requests.get(url)
    request.status_code == 200
  except Exception as req:
    print("Website at the provided url does not exist.")
    print(req)

  # read data
  data = pd.read_csv(url)

  # save data
  data.to_csv(output, header=False, index=False)


if __name__ == '__main__':
  main(opt['--url'], opt['--output'])
