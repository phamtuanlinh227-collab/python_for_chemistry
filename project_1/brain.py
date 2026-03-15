# brain.py
import numpy as np

# 1. BỘ ĐIỀU KHIỂN PID
class SmartPID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0
    
    def compute(self, current_temp):
        error = self.setpoint - current_temp
        
        # Chống cộng dồn sai số quá mức (Anti-windup)
        if abs(error) < 15: 
            self.integral += error
            
        P = self.Kp * error
        I = self.Ki * self.integral
        D = self.Kd * (error - self.prev_error)
        
        self.prev_error = error
        
        output = P + I + D
        return max(0, min(100, output)) # Công suất lò chỉ từ 0% đến 100%

# 2. HÀM CHẠY MÔ PHỎNG LÒ PHẢN ỨNG
def run_simulation(target_temp, pid_params, steps=100):
    Kp, Ki, Kd = pid_params
    pid = SmartPID(Kp, Ki, Kd, target_temp)
    
    current_temp = 25.0 # Bắt đầu ở nhiệt độ phòng
    progress = 0.0      # Tiến độ phản ứng ban đầu là 0%
    
    # Lưu lại lịch sử để vẽ biểu đồ
    history = {"time": [], "temp": [], "power": [], "progress": []}
    
    for t in range(steps):
        # Đọc cảm biến (có thêm nhiễu môi trường)
        sensor_temp = current_temp + np.random.normal(0, 0.5)
        
        # PID tính toán công suất cần thiết
        power = pid.compute(sensor_temp)
        
        # Lò sưởi làm tăng nhiệt độ, môi trường làm giảm nhiệt độ
        current_temp += (power * 0.2) - 0.8
        
        # HÓA LÝ: Phản ứng chỉ xảy ra khi nhiệt độ gần đạt mốc lý tưởng
        if abs(current_temp - target_temp) <= 5:
            progress += 1.5 # Tăng tiến độ phản ứng
            
        # Ghi chép số liệu
        history["time"].append(t)
        history["temp"].append(current_temp)
        history["power"].append(power)
        history["progress"].append(min(100, progress)) # Tối đa 100%
        
    return history