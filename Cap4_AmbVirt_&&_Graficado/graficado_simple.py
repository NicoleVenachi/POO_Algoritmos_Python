from bokeh.plotting import figure, output_file, show

#  figure, ventana a grficar
#  Ourtup file, nombre de archivo como output i.e html
#  swow, servidor html que muestre html


if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_values = int(input('Cuantos valores deseas graficar? \t'))
    x_vals = list(range(total_values))
    y_vals = [input(f'valor para {x} Y(x) \t') for x in x_vals]

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
