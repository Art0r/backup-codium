from cloud import ManageCloud

op = int(input('Digite 1 para fazer o backup ou 2 para baixar o backup: '))

if op == 1:
    manage = ManageCloud()
    manage.upload_file()
elif op == 2:
    manage = ManageCloud()
    manage.download_file()

