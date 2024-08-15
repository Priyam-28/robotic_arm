import rospy
from sensor_msgs.msg import JointState

def control_robot():
    rospy.init_node('robot_control', anonymous=True)
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    joint_state = JointState()
    joint_state.name = ['joint1', 'joint2', 'joint3', 'joint4']
    joint_state.position = [0.0, 0.0, 0.0, 0.0]

    while not rospy.is_shutdown():
        joint_state.header.stamp = rospy.Time.now()
        pub.publish(joint_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        control_robot()
    except rospy.ROSInterruptException:
        pass
