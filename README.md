# highcharts from Python

A rough sketch on how to wrap the highcharts CLI in a python process. This allows you to do things like export a chart as png from a python server

To run the example program:
```
./make-chart.py
```

## Notes

To install highcharts node module in 'unattended mode':
```
export ACCEPT_HIGHCHARTS_LICENSE=true npm install
```

To generate an example chart directly via the highcharts CLI:
```
$(npm bin)/highcharts-export-server --infile examples/chart.json --outfile /tmp/chart.png
open /tmp/chart.png
```
