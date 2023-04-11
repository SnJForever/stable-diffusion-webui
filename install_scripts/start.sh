#!/bin/bash

pip install oss2
pip install fastapi

mkdir -p /content/gdrive/MyDrive/stable-diffusion-webui/models/Stable-diffusion
mkdir -p /content/gdrive/MyDrive/stable-diffusion-webui/models/Lora
mkdir -p /content/stable-diffusion-webui/models/Stable-diffusion
mkdir -p /content/stable-diffusion-webui/models/Lora

# python /content/stable-diffusion-webui/install_scripts/download_model.py

cd /content/stable-diffusion-webui/extensions
# 下载安装webUI简体中文语言包，tagcomplete补全Tag插件、images-browser
git clone https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN
git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete
git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser


# ln -s /content/gdrive/MyDrive/stable-diffusion-webui/models/Stable-diffusion /content/stable-diffusion-webui/models/
# ln -s /content/gdrive/MyDrive/stable-diffusion-webui/models/Lora /content/stable-diffusion-webui/models/

