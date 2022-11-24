""" Generate images from text using StableDiffusion 2

(c) Tiago Tamagusko, 2022. Version 0.1.0

Usage:
    python text2image.py --prompt "Prompt to generate image" --filename "output"

Example:
    python text2image.py --prompt "A black cat with blue eyes" --filename "cat"

Based on: https://huggingface.co/stabilityai/stable-diffusion-2
"""
from __future__ import annotations

import argparse

import torch
from diffusers import EulerDiscreteScheduler
from diffusers import StableDiffusionPipeline

model_id = 'stabilityai/stable-diffusion-2'

# parse arguments
parser = argparse.ArgumentParser(
    description='Generate images from text using StableDiffusion 2.',
)

parser.add_argument(
    '-p',
    '--prompt',
    type=str,
    default='a photo of an astronaut riding a horse on mars',
    help='Prompt to use for image generation.',
)
parser.add_argument(
    '-f',
    '--filename',
    type=str,
    default='test',
    help='Filename to save the generated image to.',
)

prompt = parser.parse_args().prompt
filename = parser.parse_args().filename

# model wrapper
scheduler = EulerDiscreteScheduler.from_pretrained(
    model_id, subfolder='scheduler',
)
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, scheduler=scheduler, revision='fp16', torch_dtype=torch.float16,
)
pipe = pipe.to('cuda')

image = pipe(prompt, height=768, width=768).images[0]

image.save(f'outputs/{filename}.png')
