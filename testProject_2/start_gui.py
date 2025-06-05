#!/usr/bin/env python3
"""
启动人车检测系统GUI的辅助脚本
"""

import sys
import os
import subprocess
import time

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    # 构建命令行
    cmd = [sys.executable, os.path.join(current_dir, "p1", "person_car_detector_gui.py")]
    
    # 添加命令行参数
    cmd.extend(sys.argv[1:])
    
    # 创建日志目录
    log_dir = os.path.join(current_dir, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 创建日志文件
    log_file = os.path.join(log_dir, f"gui_log_{int(time.time())}.txt")
    
    # 启动GUI进程，将输出重定向到日志文件
    print(f"启动GUI: {' '.join(cmd)}")
    print(f"日志文件: {log_file}")
    
    with open(log_file, "w") as f:
        process = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)
    
    print(f"GUI已启动，进程ID: {process.pid}")
    
    # 等待一段时间，检查进程是否仍在运行
    time.sleep(2)
    if process.poll() is None:
        print("GUI进程正在运行")
    else:
        print(f"GUI进程已退出，退出码: {process.returncode}")
        print(f"请查看日志文件: {log_file}")
    
    # 返回进程ID
    return process.pid

if __name__ == "__main__":
    main() 