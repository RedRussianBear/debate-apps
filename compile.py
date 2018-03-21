from os import system as run
import csv

latex_special = ['#', '$', '%', '^', '&', '_', '{', '}', '~']

with open('template.tex', encoding='utf8') as f:
    template = f.read()

with open('applications.csv', encoding='utf8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    field_names = csv_reader.fieldnames

    for row in csv_reader:
        new_source = template

        for field in field_names:
            answer = row[field]

            answer = answer.replace('\\', '\\backslash')
            for character in latex_special:
                answer = answer.replace(character, '\\' + character)

            new_source = new_source.replace('[%s]' % field, answer)

        with open('source/%s-%s.tex' % (row['fname'], row['lname']), 'w', encoding='utf8') as new_source_file:
            new_source_file.write(new_source)

        run('pdflatex -output-directory output "source/%s-%s.tex"' % (row['fname'], row['lname']))
        run('pdflatex -output-directory output "source/%s-%s.tex"' % (row['fname'], row['lname']))
