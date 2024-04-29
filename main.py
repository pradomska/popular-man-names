import unicodedata
from jinja2 import Environment, FileSystemLoader
import plotly.express as px
import os
import csv
import argparse


def correct_lastname(name):
    return ''.join(c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')


def read_sorted_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = {correct_lastname(row[0]): int(row[1]) for row in reader}
        data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return data


def generate_html_template(top, top_min, data_set):
    top_lastname = data_set[:top]
    top_min_lastname = data_set[-top_min:]

    labels, sizes = zip(*top_lastname)
    fig = px.pie(names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    fig.write_html('pie_chart.html')

    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('template.html')
    rendered_template = template.render(top=top_lastname, top_min=top_min_lastname)

    return rendered_template


def write_html(file_name, rendered_template):
    with open(file_name, "w", encoding='utf-8') as f:
        f.write(rendered_template)


def is_report_exists(top, top_min):
    if os.path.exists(f'results/report_top_{top}_top_min_{top_min}.html'):
        print(f"Raport dla top={top} i top_min={top_min} został już wygenerowany i umieszczony w lokalizacji.")
        return True
    return False


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generowanie raportu popularności nazwisk w formie HTML')
    parser.add_argument('top', type=int, help='Liczba najpopularniejszych nazwisk do uwzględnienia')
    parser.add_argument('top_min', type=int, help='Liczba najmniej popularnych nazwisk do uwzględnienia')
    parser.add_argument('--force_calc', action='store_true', help='Wymuś ponowne generowanie raportu')
    return parser.parse_args()


def main():
    args = parse_arguments()
    top = args.top
    top_min = args.top_min
    force_calc = args.force_calc
    if not force_calc and is_report_exists(top, top_min):
        return

    data_set = read_sorted_from_csv('nazwiska_męskie_aktualne.csv')
    render_temp = generate_html_template(top, top_min, data_set)
    os.makedirs('results', exist_ok=True)
    write_html(f'results/report_top_{top}_top_min_{top_min}.html', render_temp)


if __name__ == '__main__':
    main()
