class Settings:
    # 检测参数
    CONFIDENCE_THRESHOLD = 0.5
    IOU_THRESHOLD = 0.5
    PERSON_ALARM_THRESHOLD = 3
    
    # 性能参数
    PROCESS_EVERY_N_FRAMES = 2
    DEFAULT_RESOLUTION = "1280x720"
    
    # 文件路径
    MODEL_PATH = "yolo/yolov8n.pt"
    ALARM_SOUND_PATH = "alarm.mp3"