from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from bokeh.models.widgets import Slider
from bokeh.io import output_notebook, push_notebook

# Generate some data
x = list(range(10))
y = [val**2 for val in x]

# Create the plot
source = ColumnDataSource(data=dict(x=x, y=y))
p = figure(title="Interactive Plot", plot_width=400, plot_height=400)
p.line(x='x', y='y', source=source, line_width=2)

# Define a function to update the plot
def update(power):
    y = [val**power for val in x]
    source.data = dict(x=x, y=y)
    push_notebook()

# Use a Slider to control the power
slider = Slider(start=0, end=4, value=2, step=0.1, title="Power")
slider.on_change('value', lambda attr, old, new: update(new))

# Show the plot
show(column(slider, p), notebook_handle=True)
