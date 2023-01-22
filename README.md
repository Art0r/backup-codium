# Backup-codium :cloud: 

Script to handle backup for VSCodium

## Using it

### Upload
```bash
  sudo apt update && sudo apt upgrade -y
  sudo apt install python3-venv zip
  mv ~/.vscode-oss ~/Documentos && mv ~/.config/VSCodium ~/Documentos
  cd ~/Documentos
  zip -r codium.zip ./VSCodium ./.vscode-oss
  git https://github.com/Art0r/backup-codium.git
  cd ./backup-codium
  python3 -m venv venv
  . venv/bin/activate 
  pip install -r requirements.txt
  python main.py
  # cd .. && rm -rf ./backup-codium
  deactivate
```

### Download
```bash
```
    
