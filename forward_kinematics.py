import numpy as np


def forward_kinematics_2dof(theta1, theta2, L1=1.0, L2=1.0):
    """
    2-DOF 平面机械臂正运动学

    参数:
        theta1: 关节1角度 (弧度)
        theta2: 关节2角度 (弧度, 相对于连杆1)
        L1, L2: 连杆长度 (默认 1.0)

    返回:
        (x, y): 末端在世界坐标系中的位置
    """
    x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
    y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)
    return x, y


if __name__ == "__main__":
    # 测试1: 两个关节都是0,机械臂完全伸直沿x轴
    x, y = forward_kinematics_2dof(0, 0)
    print(f"θ1=0°,   θ2=0°:   末端 = ({x:.3f}, {y:.3f})")

    # 测试2: 关节1转90°,机械臂竖直向上
    x, y = forward_kinematics_2dof(np.pi / 2, 0)
    print(f"θ1=90°,  θ2=0°:   末端 = ({x:.3f}, {y:.3f})")

    # 测试3: 关节1=0°, 关节2=90°, 第一节水平,第二节竖直
    x, y = forward_kinematics_2dof(0, np.pi / 2)
    print(f"θ1=0°,   θ2=90°:  末端 = ({x:.3f}, {y:.3f})")