#!/usr/bin/env python

from tempfile import NamedTemporaryFile
import os
import json
import subprocess

HIGHCHART_EXECUTABLE_PATH= os.path.join(
    os.path.dirname(__file__), 
    'node_modules/.bin/highcharts-export-server')

EXAMPLE_CHART_DEFINITION = {
  "xAxis": {
    "categories": [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec"
    ]
  },
  "series": [
    {
      "data": [
        29.9,
        71.5,
        106.4,
        129.2,
        144,
        176,
        135.6,
        148.5,
        216.4,
        194.1,
        95.6,
        54.4
      ]
    }
  ]
}

def run_highcharts(infile,outfile):
    command = [HIGHCHART_EXECUTABLE_PATH, '-infile', infile.name, '-outfile', outfile.name]
    proc = subprocess.Popen(command, stderr=subprocess.STDOUT)
    proc.communicate()
    success = proc.returncode == 0
    return success

def render_chart_to_png(chart_definition):
    """takes a highchart definition and renders it to a png file.
    returns the path to file. 
    NOTE: the CALLER of this function owns the generated file and 
    is responsible for deleting it.
    """

    outfile = NamedTemporaryFile(mode='r',delete=False, prefix='highcharts-outfile-', suffix='.png')
    outfile.close()

    with NamedTemporaryFile(prefix='highcharts-infile-') as infile:
        json.dump(chart_definition,infile)
        infile.flush()

        if run_highcharts(infile,outfile):
            return outfile.name
        else:
            raise Exception('failed to create chart')

if __name__ == "__main__":
    png_path = render_chart_to_png(EXAMPLE_CHART_DEFINITION)
    print 'Chart rendered to ', png_path
