# -*- coding: utf-8 -*-
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

base_path = './internlm2-chat-1.8b'

if not os.path.exists(base_path):
    # download repo to the base_path directory using git
    os.system('apt install git')
    os.system('apt install git-lfs')
    os.system(f'git clone https://code.openxlab.org.cn/OpenLMLab/internlm2-chat-1.8b.git {base_path}')
    os.system(f'cd {base_path} && git lfs pull')

    os.system("nohup lmdeploy serve api_server  /root/internlm2-chat-1_8b --model-format hf  --quant-policy 0  --server-name 0.0.0.0 --server-port 23333 --tp 1 &")
    os.system("lmdeploy serve api_client http://localhost:7860")