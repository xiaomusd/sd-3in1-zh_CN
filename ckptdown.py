import os

os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/perfect_world/resolve/main/perfectWorld_v2Baked.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Stable-diffusion -o perfectWorld_v2Baked.safetensors")

os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/chilloutmix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Stable-diffusion -o chilloutmix_NiPrunedFp32Fix.safetensors")

os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/Counterfeit-V2.0/resolve/main/Counterfeit-V2.0fp16.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Stable-diffusion -o Counterfeit-V2.0fp16.safetensors")

os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/rhine0613/fashionGirlv50/resolve/main/fashionGirl_v50.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Lora -o fashionGirl_v50.safetensors")
os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/mlida/Cute_girl_mix4/resolve/main/cuteGirlMix4_v10.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Lora -o cuteGirlMix4_v10.safetensors")
os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/xiaolxl/GuoFeng3/resolve/main/GuoFeng3.2_Lora_big_light.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Lora -o GuoFeng3.2_Lora_big_light.safetensors")
os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/tomspy/shojovibe_v11.safetensors/resolve/main/shojovibe_v11.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Lora -o shojovibe_v11.safetensors")
os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/amornlnw7/koreanDollLikeness_v15/resolve/main/koreanDollLikeness_v15.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Lora -o koreanDollLikeness_v15.safetensors")
os.system("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/aimainia/japaneseDollLikeness_v10/resolve/main/japaneseDollLikeness_v10.safetensors -d /root/autodl-tmp/stable-diffusion-webui/models/Lora -o japaneseDollLikeness_v10.safetensors")