import time
import pygetwindow as gw
import pyautogui
import ctypes

# 你程序窗口的关键标题（可模糊匹配）
WINDOW_KEYWORD = "SCUMServer"

def activate_target_window():
    windows = gw.getWindowsWithTitle(WINDOW_KEYWORD)
    if not windows:
        print(f"❌ 没找到包含关键词 '{WINDOW_KEYWORD}' 的窗口")
        return False

    window = windows[0]
    window.activate()
    print(f"✅ 已激活窗口: {window.title}")
    time.sleep(0.5)
    return True

def click_window_center():
    width, height = pyautogui.size()
    pyautogui.click(x=width//2, y=height//2)
    time.sleep(0.2)

def send_ctrl_c_low_level():
    # 模拟 Ctrl + C
    VK_CONTROL = 0x11
    VK_C = 0x43
    KEYEVENTF_KEYDOWN = 0x0000
    KEYEVENTF_KEYUP = 0x0002

    ctypes.windll.user32.keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYDOWN, 0)
    ctypes.windll.user32.keybd_event(VK_C, 0, KEYEVENTF_KEYDOWN, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(VK_C, 0, KEYEVENTF_KEYUP, 0)
    ctypes.windll.user32.keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0)
    print("✅ 已通过低级方式发送 Ctrl+C")

if __name__ == "__main__":
    if activate_target_window():
        click_window_center()
        time.sleep(0.2)
        send_ctrl_c_low_level()
        time.sleep(0.5)
        send_ctrl_c_low_level()
