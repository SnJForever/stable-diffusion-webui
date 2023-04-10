
from torch.hub import download_url_to_file

MODEL_PATH='/content/gdrive/MyDrive/stable-diffusion-webui/models/Stable-diffusion'
LORA_PATH='/content/gdrive/MyDrive/stable-diffusion-webui/models/Lora'

# SD 1.5
download_url_to_file('https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt', MODEL_PATH+'/v1-5-pruned-emaonly.ckpt', hash_prefix=None, progress=True)

# 模型 https://civitai.com/models/6424/chilloutmix
download_url_to_file('https://civitai.com/api/download/models/11745', MODEL_PATH+'chilloutmix-Ni-pruned-fp32-fix.safetensors', hash_prefix=None, progress=True)

# https://civitai.com/models/4823/deliberate
download_url_to_file('https://civitai.com/api/download/models/15236', MODEL_PATH+'/deliberate_v2.safetensors', hash_prefix=None, progress=True)

# https://civitai.com/models/10415/3-guofeng3
download_url_to_file('https://civitai.com/api/download/models/36644', MODEL_PATH+'/3Guofeng3_v33.safetensors', hash_prefix=None, progress=True)

# https://civitai.com/models/26578/xsarchitectural-17sciencefictioncityonmars
download_url_to_file('https://civitai.com/api/download/models/31884', MODEL_PATH+'/xsarchitectural_v11.safetensors', hash_prefix=None, progress=True)

# https://civitai.com/models/27530/xsarchitectural-21futuretechnologycity
download_url_to_file('https://civitai.com/api/download/models/32964', MODEL_PATH+'/xsarchitectural_.safetensors', hash_prefix=None, progress=True)

# 墨心 https://civitai.com/models/12597/moxin
download_url_to_file('https://civitai.com/api/download/models/14856', LORA_PATH+'Moxin_10.safetensors', hash_prefix=None, progress=True)

# 舒克走马 https://civitai.com/api/download/models/20143
download_url_to_file('https://civitai.com/api/download/models/20143', LORA_PATH+'sukezouma11.safetensors', hash_prefix=None, progress=True)
