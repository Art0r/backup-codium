# Backup-codium :cloud: 

Script to handle backup for VSCodium

## Using it

### Upload
```bash
  sudo apt update && sudo apt upgrade -y
  sudo apt install python3-venv zip
  mv ~/.vscode-oss ~/Documentos && mv ~/.config/VSCodium ~/Documentos
  cd ~/Documentos
  zip -r vscopium.zip ./VSCodium ./.vscode-oss
  python3 -m venv venv 
  git https://github.com/Art0r/backup-codium.git
  cd ./backup-codium
  pip install -r requirements.txt
  python main.py
  cd .. && rm -rf ./backup-codium
```

### Download
```bash
```
    
