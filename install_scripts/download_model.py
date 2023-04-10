from torch.hub import download_url_to_file

MODEL_PATH='/content/stable-diffusion-webui/models/Stable-diffusion'

# SD 1.5
download_url_to_file('https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt', MODEL_PATH+'/v1-5-pruned-emaonly.ckpt', hash_prefix=None, progress=True)

# https://civitai.com/models/4823/deliberate
download_url_to_file('https://civitai.com/api/download/models/15236', MODEL_PATH+'/deliberate_v2.safetensors', hash_prefix=None, progress=True)

# https://civitai.com/models/10415/3-guofeng3
download_url_to_file('https://civitai.com/api/download/models/36644', MODEL_PATH+'/3Guofeng3_v33.safetensors', hash_prefix=None, progress=True)

# https://civitai.com/models/26578/xsarchitectural-17sciencefictioncityonmars
download_url_to_file('https://civitai.com/api/download/models/31884', MODEL_PATH+'/xsarchitectural_v11.safetensors', hash_prefix=None, progress=True)

# https://civitai.com/models/27530/xsarchitectural-21futuretechnologycity
download_url_to_file('https://civitai.com/api/download/models/32964', MODEL_PATH+'/xsarchitectural_.safetensors', hash_prefix=None, progress=True)
