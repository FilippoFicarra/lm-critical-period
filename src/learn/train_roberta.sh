#!/bin/bash

EXTRA_FLAGS="$@"
echo $EXTRA_FLAGS

# RUN_APPLICATION="python"
RUN_APPLICATION="torchrun --nproc_per_node 8"

${RUN_APPLICATION} ./src/learn/run_mlm.py \
    --model_type roberta \
    --tokenizer_name "${DATA_DIR}/roberta_tokenizer" \
    --train_file "${DATA_DIR}/raw/train.txt" \
    --validation_file "${DATA_DIR}/raw/validation.txt" \
    --cache_dir "${DATA_DIR}/cache" \
    --run_name ${MODEL_NAME} \
    --seed ${SEED} \
    --report_to wandb \
    --output_dir "./checkpoints/${MODEL_NAME}" \
    --overwrite_output_dir \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --gradient_accumulation_steps 64 \
    --eval_accumulation_steps 64 \
    --max_seq_length 510 \
    --do_train \
    --logging_steps 50 \
    --do_eval \
    --evaluation_strategy "epoch" \
    --save_strategy "steps" \
    --low_cpu_mem_usage \
    --fp16 \
    --ddp_timeout 7200 \
    ${EXTRA_FLAGS}