# birthchartSVG

Birthchart SVG is a chart generator based on Kerykeion and Openastro.
Like the titles says it prints out SVG file of a kerykeion object,
it's very easy to use.

```python
# Install:
>>> pip3 install birthchartSVG

#Import:
>>> import birthchartSVG as br
>>> import kerykeion as kr

# Generate a kerykeion:
# Arguments: "Name", year, month, day, local hour, minuts, "city", nat=nation)
>>> kanye = kr.Calculator("Kanye", 1977, 6, 8, 8, 45, "Atlanta")

# Pass the the kerykeion object and make the instance:
>>> kanyeSVG = br.MakeInstance(kanye)

# Set the output directory for the SVG:
>>> kanyeSVG.set_dir = "/Users/{YourName}"

#Generate the SVG:
>>> kanyeSVG.makeSVG()


SVG generated successfully!

```

![alt text](https://raw.githubusercontent.com/g-battaglia/birthchartSVG/master/birthchartSVG/data/template/sample.svg)

## Documentation

Just like in the exemple, first make an instance and then use the makeSVG() to generate the SVG chart.
The file generated has the name you inserted followed by Chart.svg

## Installation

BirtchartSVG is Python 3 package, make sure you have Python 3 installed on your system.

## Development

You can clone this repository or download a zip file using the right side buttons.
