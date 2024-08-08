import torch

from diffusers import UNetSpatioTemporalConditionModel, StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video, export_to_gif

unet = UNetSpatioTemporalConditionModel.from_pretrained(
            "outputs/checkpoint-6000",
                subfolder="unet",
                    torch_dtype=torch.float16,
                        low_cpu_mem_usage=False,
                        )
pipe = StableVideoDiffusionPipeline.from_pretrained(
            "stabilityai/stable-video-diffusion-img2vid-xt",
                unet=unet,
                    low_cpu_mem_usage=False,
                        torch_dtype=torch.float16, variant="fp16", local_files_only=True,
                        )
pipe.to("cuda:0")

image = load_image(f'sys.argv[1]')
image = image.resize((320,320))

generator = torch.manual_seed(-1)
with torch.inference_mode():
        frames = pipe(image,
                        num_frames=14,
                        width=320,
                        height=320,
                        decode_chunk_size=8, generator=generator, motion_bucket_id=127, fps=8, num_inference_steps=30).frames[0]
        export_to_video(frames, "generated.mp4", fps=7)