import camelot

tables = camelot.read_pdf('foo.pdf', pages = '1')
print(tables)

tables.export('foo.csv', f = 'csv', compress = True)
tables[0].to_csv('foo.csv')
