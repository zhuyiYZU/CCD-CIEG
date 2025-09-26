# -*- coding: utf-8 -*-
import logging
import subprocess
import time
from itertools import product

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # 配置日志记录器
    #train(预测出的数据，正负样本)， shot,
    l = ['tencent']#
    batch_sizes = {32}
    learning_rates = {'2e-5'}
    shots = {20}
    seeds = {23}
    template_id = {0}#换模板时候pipleline_base里面的title = wrapped_example[0][3]['text']也要把3换掉
    verbalizer = {'manual'}
    for n, t, j, i, k, m, v in product(l,template_id, seeds, batch_sizes, learning_rates, shots, verbalizer):
        time_start = time.time()
        cmd = (
            f"python fewshot.py --result_file ./al_result_main.txt "
            f"--dataset {n} --template_id {t} --seed {j} "
            f"--batch_size {i} --shot {m} --learning_rate {k} --verbalizer {v}"
        )

        logging.info(f"Executing command: {cmd}")
        print(cmd)
        try:
            # subprocess.run(cmd, shell=True, check=True)
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            logging.info(f"Command executed successfully: {cmd}")
        except subprocess.CalledProcessError as e:
            # logging.error(f"Command failed: {cmd}. Error: {e.stderr.decode().strip()}")
            logging.error(f"Command failed: {cmd}. Error: {str(e)}")
        time_end = time.time()
        print("运行时间："+str(time_end - time_start)+"秒")
        time.sleep(2)
