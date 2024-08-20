import sys
import torch

from diffusers import UNetSpatioTemporalConditionModel, StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video, export_to_gif

checkpoint_path: str = sys.argv[1]
input_image_path: str = sys.argv[2]


unet = UNetSpatioTemporalConditionModel.from_pretrained(
            checkpoint_path,
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

pipe.enable_model_cpu_offload()
pipe.unet.enable_forward_chunking()

image = load_image(input_image_path)
image = image.resize((1024, 576))

generator = torch.manual_seed(-1)
with torch.inference_mode():
        frames = pipe(image,
                        num_frames=60,
                        width=1024,
                        height=576,
                        decode_chunk_size=8, generator=generator, motion_bucket_id=10, fps=8, num_inference_steps=30).frames[0]
        export_to_video(frames, "generated.mp4", fps=7)
