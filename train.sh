PYTORCH_ENABLE_MPS_FALLBACK=1 accelerate launch train_svd.py \
    --config_file="colab-config.yaml" \
    --pretrained_model_name_or_path="stabilityai/stable-video-diffusion-img2vid-xt" \
    --per_gpu_batch_size=1 --gradient_accumulation_steps=1 \
    --max_train_steps=50000 \
    --width=320 \
    --height=240 \
    --checkpointing_steps=1000 --checkpoints_total_limit=1 \
    --learning_rate=1e-5 --lr_warmup_steps=0 \
    --seed=123 \
    --validation_steps=100 \
    --base_folder="/content/gdrive/My Drive/smile"