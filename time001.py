import time
import sys

# 尝试导入声音模块（仅Windows支持）
try:
    import winsound
    sound_support = True
except ImportError:
    sound_support = False
    print("提示：当前环境不支持声音提醒，将仅显示文字提醒\n")


def validate_time_input(time_str):
    """验证时间输入是否有效"""
    try:
        time_list = [int(t) for t in time_str.split('-')]
        for t in time_list:
            if t <= 0:
                raise ValueError("时间必须为正整数")
        return time_list
    except ValueError as e:
        raise ValueError(f"时间格式错误：{str(e)}，请使用正整数并用减号分隔（例如4-2-6）")


def validate_loop_count(loop_str):
    """验证循环次数是否有效"""
    try:
        loop_count = int(loop_str)
        if loop_count <= 0:
            raise ValueError("循环次数必须为正整数")
        return loop_count
    except ValueError:
        raise ValueError("循环次数必须为正整数")


def send_reminder(loop_num, reminder_num):
    """发送提醒（文字+可选声音）"""
    reminder_msg = f"⚠️ 第{loop_num}次循环，第{reminder_num}次提醒！"
    print(reminder_msg)
    
    # 播放提示音（仅Windows）
    if sound_support:
        winsound.Beep(1000, 500)  # 1000Hz频率，持续500毫秒


def main():
    print("===== 多时间点循环提醒工具 =====")
    
    # 获取并验证时间序列
    while True:
        time_input = input("请输入时间点序列（用减号分隔，例如4-2-6）：")
        try:
            time_list = validate_time_input(time_input)
            break
        except ValueError as e:
            print(f"输入错误：{e}，请重新输入\n")
    
    # 获取并验证循环次数
    while True:
        loop_input = input("请输入循环次数（正整数）：")
        try:
            loop_count = validate_loop_count(loop_input)
            break
        except ValueError as e:
            print(f"输入错误：{e}，请重新输入\n")
    
    # 显示提醒计划
    total_time = sum(time_list) * loop_count
    print(f"\n提醒计划已设置：")
    print(f"时间点序列：{time_list} 秒")
    print(f"循环次数：{loop_count} 次")
    print(f"总时长：约 {total_time} 秒")
    print("开始执行提醒计划...（按Ctrl+C可强制退出）\n")
    
    # 执行提醒
    try:
        for loop in range(1, loop_count + 1):
            print(f"--- 第{loop}次循环开始 ---")
            for idx, t in enumerate(time_list, 1):
                print(f"等待 {t} 秒后将进行第{idx}次提醒...")
                time.sleep(t)  # 等待指定秒数
                send_reminder(loop, idx)
            print(f"--- 第{loop}次循环结束 ---\n")
        
        print("🎉 所有提醒已完成！")
    
    except KeyboardInterrupt:
        print("\n程序已被手动终止")
        sys.exit(0)


if __name__ == "__main__":
    main()
