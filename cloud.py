from yaspin import yaspin
from prompt_toolkit import print_formatted_text, HTML
from styles import style_ok, style_fail
from dropbox import DropboxOAuth2FlowNoRedirect
from dropbox.exceptions import ApiError, AuthError
import dropbox
import os


class AuthCloud:
    _APP_KEY: str
    _APP_SECRET: str
    _ACCESS_TOKEM: str

    def __init__(self, f):
        self._APP_KEY = "n71c23cqoammtyl"
        self._APP_SECRET = "qc1p8xwsrk6rjoa"
        self.f = f

    def __call__(self, *args, **kwargs):
        auth_flow = DropboxOAuth2FlowNoRedirect(self._APP_KEY, self._APP_SECRET)
        authorize_url = auth_flow.start()
        print("1. Go to: " + authorize_url)
        print("2. Click \"Allow\" (you might have to log in first).")
        print("3. Copy the authorization code.")
        auth_code = input("Enter the authorization code here: ").strip()
        try:
            oauth_result = auth_flow.finish(auth_code)
            self._ACCESS_TOKEN = oauth_result.access_token

        except AuthError as e:
            print('Error: %s' % (e,))
            exit(1)

        return self.f(self, access_token=self._ACCESS_TOKEN)


class ManageCloud:
    def __init__(self):
        pass

    @AuthCloud
    def upload_file(self, access_token: str):
        dbx = dropbox.Dropbox(oauth2_access_token=access_token, timeout=None)
        spinner = yaspin(text='Fazendo o upload...', color='cyan')
        spinner.start()
        try:
            file = open(os.path.join(os.path.expanduser('~'),
                                     'Documentos', 'codium.zip'), 'rb').read()
            dbx.files_upload(file, os.path.join(os.path.expanduser('~'), 'Documentos', 'codium.zip'))
            spinner.stop()
            print_formatted_text(HTML(
                u"<b>></b> <msg>OK</msg> <sub-msg>O upload foi realizado com sucesso</sub-msg>"
            ), style=style_ok)
        except ApiError as e:
            spinner.stop()
            print_formatted_text(HTML(
                u"<b>></b> <msg>Falha</msg> <sub-msg>Ocorreu um erro ao fazer o upload</sub-msg>"
            ), style=style_fail)
            print(e.args)

    @AuthCloud
    def download_file(self, access_token: str):
        print('ainda por ser implementado')