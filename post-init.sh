#!/bin/bash

echo "[+] Copy toc-extension config to user-settings"
mkdir -p /home/jovyan/work/.jupyter_config/lab/user-settings/@jupyterlab/toc-extension
cp ./.user-settings/@jupyterlab/toc-extension/plugin.jupyterlab-settings /home/jovyan/work/.jupyter_config/lab/user-settings/@jupyterlab/toc-extension/plugin.jupyterlab-settings

echo "[+] Copy docmanager-extension config to user-settings"
mkdir -p /home/jovyan/work/.jupyter_config/lab/user-settings/@jupyterlab/docmanager-extension
cp ./.user-settings/@jupyterlab/docmanager-extension/plugin.jupyterlab-settings /home/jovyan/work/.jupyter_config/lab/user-settings/@jupyterlab/docmanager-extension/plugin.jupyterlab-settings

echo "[+] Copy filebrowser-extension config to user-settings"
mkdir -p /home/jovyan/work/.jupyter_config/lab/user-settings/@jupyterlab/filebrowser-extension
cp ./.user-settings/@jupyterlab/filebrowser-extension/browser.jupyterlab-settings /home/jovyan/work/.jupyter_config/lab/user-settings/@jupyterlab/filebrowser-extension/browser.jupyterlab-settings

echo "[+] Set theme"
mkdir -p /opt/conda/share/jupyter/lab/settings
cat << EOF > /opt/conda/share/jupyter/lab/settings/overrides.json
{
  "@jupyterlab/apputils-extension:themes": {
    "theme": "grundkurs_theme"
  }
}


EOF
